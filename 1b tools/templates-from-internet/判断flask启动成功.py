import webbrowser
from application import app
import threading
import time
from urllib import request

INDEX_URL = "http://127.0.0.1:5000"


def open_browser():
    print('server starting...')
    while True:
        try:
            request.urlopen(url=INDEX_URL)
            break
        except Exception as e:
            print(e)
            time.sleep(0.5)
    print('server started !')
    # server started callback
    webbrowser.open(INDEX_URL)


threading.Thread(target=open_browser).start()
# start server
app.run(host="0.0.0.0", port=5000)