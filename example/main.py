import CLIGame

screen = CLIGame.Screen(100, 20, title="[ Penis ]")
clock = CLIGame.Clock(30)
speaker = CLIGame.Speaker()
reader = CLIGame.Reader()

sprite = ""
sprite += "---------\n"
sprite += "|   п   |\n"
sprite += "|   е   |\n"
sprite += "|   н   |\n"
sprite += "|   и   |\n"
sprite += "|   с   |\n"
sprite += "---------\n"

screen.draw_sprite(0, 0, sprite)
screen.draw_sprite(92, 5, sprite)
screen.draw_file(7, 3, "./sources/image.txt")

speaker.play("./sources/p.mp3")

def sigma():
    print("Penis")

reader.bind("s", sigma)

for i in range(0, 20):
    screen.draw_sprite(i, i, sprite)
    screen.print()
    
    clock.tick()
