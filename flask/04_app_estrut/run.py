# exemplo
from app import app
import signal, sys

def handler(signal, frame):
    print('Tchaul!')
    sys.exit(0)
signal.signal(signal.SIGINT, handler)



if __name__ == "__main__":
    app.debug = True
    try:
        app.run()
    except KeyboardInterrupt:
        print('print this')
    finally:
        print('finally')