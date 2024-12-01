from playsound import playsound

class Speaker():
    def play(self, path: str):
        playsound(path, False)