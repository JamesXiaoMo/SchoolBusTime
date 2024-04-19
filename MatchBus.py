from datetime import datetime
import random


MatsunagaToUnivBuses = []
MatsunagaToUnivBuses_WE = []
UnivToMatsunagaBuses = []
UnivToMatsunagaBuses_WE = []


def load_schedule_file(file_name='schedule.txt'):
    with open(file_name, 'r') as f:
        for line in f:
            if line.replace('\n', '').endswith('*'):
                if line.startswith('+'):
                    RawTime = line.replace('\n', '').replace('+', '').replace('*', '')
                    TimeEncode = int(RawTime.split(':')[0]) * 60 + int(RawTime.split(':')[1])
                    MatsunagaToUnivBuses_WE.append(TimeEncode)
                elif line.startswith('-'):
                    RawTime = line.replace('\n', '').replace('-', '').replace('*', '')
                    TimeEncode = int(RawTime.split(':')[0]) * 60 + int(RawTime.split(':')[1])
                    UnivToMatsunagaBuses_WE.append(TimeEncode)
            else:
                if line.startswith('+'):
                    RwTime = line.replace('\n', '').replace('+', '')
                    TimeEncode = int(RwTime.split(':')[0]) * 60 + int(RwTime.split(':')[1])
                    MatsunagaToUnivBuses.append(TimeEncode)
                elif line.startswith('-'):
                    RwTime = line.replace('\n', '').replace('-', '')
                    TimeEncode = int(RwTime.split(':')[0]) * 60 + int(RwTime.split(':')[1])
                    UnivToMatsunagaBuses.append(TimeEncode)


def match_buses():
    load_schedule_file('schedule.txt')
    CurrentTimeEncode = datetime.now().hour * 60 + datetime.now().minute
    MassageDecode = []
    if datetime.today().weekday() == 5 or datetime.today().weekday() == 6:
        for i in MatsunagaToUnivBuses_WE:
            if CurrentTimeEncode <= i:
                if i % 60 == 0:
                    MinuteDecode = '00'
                else:
                    MinuteDecode = str(i % 60)
                MassageDecode.append(str(int(i / 60)) + ':' + MinuteDecode)
                break
            elif i == MatsunagaToUnivBuses_WE[len(MatsunagaToUnivBuses_WE) - 1]:
                MassageDecode.append('NONE')
        for i in UnivToMatsunagaBuses_WE:
            if CurrentTimeEncode <= i:
                if i % 60 == 0:
                    MinuteDecode = '00'
                else:
                    MinuteDecode = str(i % 60)
                MassageDecode.append(str(int(i / 60)) + ':' + MinuteDecode)
                break
            elif i == UnivToMatsunagaBuses_WE[len(UnivToMatsunagaBuses_WE) - 1]:
                MassageDecode.append('NONE')
    else:
        for i in MatsunagaToUnivBuses:
            if CurrentTimeEncode <= i:
                if i % 60 == 0:
                    MinuteDecode = '00'
                else:
                    MinuteDecode = str(i % 60)
                MassageDecode.append(str(int(i / 60)) + ':' + MinuteDecode)
                break
            elif i == MatsunagaToUnivBuses[len(MatsunagaToUnivBuses) - 1]:
                MassageDecode.append('NONE')
        for i in UnivToMatsunagaBuses:
            if CurrentTimeEncode <= i:
                if i % 60 == 0:
                    MinuteDecode = '00'
                else:
                    MinuteDecode = str(i % 60)
                MassageDecode.append(str(int(i / 60)) + ':' + MinuteDecode)
                break
            elif i == UnivToMatsunagaBuses[len(UnivToMatsunagaBuses) - 1]:
                MassageDecode.append('NONE')
    return MassageDecode


def load_billboard():
    billboard_list = []
    with open('billboard.txt', 'r', encoding='utf-8') as f:
        for i in f:
            billboard_list.append(str(i.replace('\n', '')))
    return billboard_list[random.randint(0, len(billboard_list) - 1)]


def save_traffic_data(traffic_data: int):
    with open('traffic.txt', 'a', encoding='utf-8') as f:
        f.write("{str1}\nToday's traffic : {str2}\n".format(
            str1=datetime.today().strftime('%Y-%m-%d'), str2=str(traffic_data)))
        f.close()
