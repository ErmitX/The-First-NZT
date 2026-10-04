import time

def pause():
    input("\nPress ENTER to continue...")

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)
    print()

def choice():
    while True:
        answer = input("\n> ").strip()
        if answer in ["1", "2", "3"]:
            return answer
        print("Please choose 1, 2, or 3.")

clear = "\033[H\033[J"

print(clear)
print("=" * 60)
print("                         THE FIRST NZT")
print("=" * 60)
print()

type_text("Eddie Morra sits alone in his apartment.")
type_text("His novel is unfinished.")
type_text("His relationship is falling apart.")
type_text("His bank account is almost empty.")
print()

type_text("Then someone knocks on the door.")
pause()

print(clear)
type_text("Eddie opens the door.")
type_text("A familiar face is standing outside.")
type_text("Vernon Gant.")
print()

type_text('"You look terrible, Eddie."')
type_text('"Thanks."')
type_text('"I have something that might change that."')
print()

type_text("Vern reaches into his pocket.")
type_text("He takes out a small transparent bag.")
print()
type_text("Inside is a single pill.")
print()
type_text("NZT-48")
print()

print("1. Ask Vernon what it is")
print("2. Take the pill immediately")
print("3. Refuse it")

answer = choice()

if answer == "1":
    print()
    type_text('"What exactly does this do?"')
    type_text('"It lets you access your entire brain."')
    type_text("\"That doesn't sound possible.\"")
    type_text('"Neither does a lot of things until you see them happen."')
    pause()

elif answer == "2":
    print()
    type_text("Eddie takes the pill.")
    type_text("He doesn't even know what he's expecting.")
    pause()

else:
    print()
    type_text("Eddie shakes his head.")
    type_text("\"No. I don't need another problem.\"")
    type_text("Vern leaves.")
    print()
    type_text("Eddie closes the door.")
    type_text("For the next few hours, everything feels normal.")
    print()
    print("ENDING: THE ORDINARY LIFE")
    raise SystemExit

print(clear)
type_text("Twenty minutes pass.")
type_text("Nothing.")
print()

type_text("Then everything changes.")

time.sleep(1)

type_text("The room becomes sharper.")
type_text("Every sound is separated.")
type_text("Every thought connects to another.")
type_text("Memories you haven't thought about in years return.")
type_text("You remember every word you've ever read.")
print()

type_text("Eddie looks at the unfinished manuscript on his desk.")
type_text("He suddenly knows exactly what to write.")
print()

type_text("He starts typing.")

words = 0

for i in range(10):
    words += 500
    print("Writing...", words, "words")
    time.sleep(0.2)

print()
type_text("Hours later, the manuscript is finished.")
type_text("Eddie looks at the screen.")
print()
print("Pages written:", words // 10)
print("Focus: 100")
print("Memory: 100")
print("Confidence: 95")
print()

type_text("For the first time in his life...")
type_text("Eddie doesn't feel average.")

print()
print("ENDING: THE BEGINNING")