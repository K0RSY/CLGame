import CLGame

screen = CLGame.Screen(100, 20, title="[ Test ]")
clock = CLGame.Clock(30)
speaker = CLGame.Speaker()
reader = CLGame.Reader()

sprite = ""
sprite += "---------\n"
sprite += "|   т   |\n"
sprite += "|   е   |\n"
sprite += "|   с   |\n"
sprite += "|   т   |\n"
sprite += "---------\n"

screen.draw_file(45, 10, "./sources/image.txt")

speaker.play("./sources/p.mp3")

def sigma():
    print("Test")

reader.bind("t", sigma)

for i in range(0, 20):
    screen.draw_sprite(i*4, i*i//5, sprite)
    screen.print()
    
    clock.tick()
