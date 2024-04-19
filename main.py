from flask import Flask
from MatchBus import match_buses, load_billboard, save_traffic_data
from waitress import serve
import schedule
import threading
import time

app = Flask(__name__)

traffic = 0


def clear_traffic_data():
    global traffic
    traffic = 0


schedule.every().day.at('23:59:00').do(save_traffic_data, traffic_data=traffic)
schedule.every().day.at('23:59:59').do(clear_traffic_data)


@app.route('/')
def GetData():
    global traffic
    traffic += 1
    return ('松永->福山大: {str1}  福山大->松永: {str2}<br>{str3}'.format(
        str1=match_buses()[0], str2=match_buses()[1], str3=load_billboard()))


def schedule_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=schedule_tasks)
    t1.start()
    # ------------------------- #
    # Only for debugging
    # app.run(debug=True)
    # ------------------------- #
    # Only for deploying
    serve(app, host='0.0.0.0', port=11224)
    # ------------------------- #
