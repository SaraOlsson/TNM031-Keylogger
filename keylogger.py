from pynput import keyboard

# not used yet
class KeyLogger:
    def __init__(self):

        self.listener = None

    def init(self):

        print("running")

        # define which functions to call on press or release
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        self.listener.start()


    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

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
