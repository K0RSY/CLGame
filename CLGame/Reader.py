from pynput import keyboard

class Reader():
    def __init__(self):
        self.binds = {}
        self.listener = keyboard.Listener(on_press=self.key_press, on_release=lambda x: 0)
        self.listener.start()

    def key_press(self, key):
        try:
            if key.char in self.binds:
                self.binds[key.char]()
        except AttributeError:
            pass

    def bind(self, key: str, func):
        self.binds[key] = func

    def unbind(self, key: str):
        del self.binds[key]
