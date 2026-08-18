# Generated from: AI 1.ipynb
# Converted at: 2026-08-18T02:40:29.284Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

print("Hello! I am cleaner.")
print("build a cleaning robot...")
print(2 + 3, "is the answer to 2 + 3")
room = ["D", "C", "D", "D", "C"]

def show_room(room):
    picture = ""
    for spot in room:
        if spot == "D":
            picture += "💩 "
        else:
            picture += "✨ "
    print(picture)

print("Our room right now!")
show_room(room)


def clean_spot(spot):
    if spot == "D":

        return "C"
    else:
        return "C"

result = clean_spot("D")
print("The robot looked at a dirty spot and made it:", result, "(C means clean)")
print("BEFORE - the dirty room:")
show_room(room)

for i in range(len(room)):
    room[i] = clean_spot(room[i])
    print("After cleaning spot number", i + 1, ":")
    show_room(room)

print()

m1=input()
if (m1=="hello"):
  print("hello this is chatbox")
  print("what is your name?")
  m2=input()
  if (m2=="vishnu"):
    print("Hello vishnu, I hope you are doing well...")
    print("how can i help you...?")
    m3=input()
    if (m3=="python"):
      print("Python is a high-level, versatile, and beginner-friendly programming language  known for its clear, English-like syntax and widespread adoption across modern industries. ")
    m4=input()
    if (m4=="marwadi university"):
      print("Marwadi University (MU) is a prominent private university established in 2016 and located in Rajkot,Gujarat,INDIA." )
    m5=input()
    if(m5=="bye"):
      print("bye, Have a good day!...")
else:
  print("sorry ,I can't help with this")

email=input()
spamwords = ["offer","claim","prize","free","money","click"]
spam = False
for word in spamwords:
    if word in email:
        spam = True
        break
if (email!=spamwords):
 print("mail is spam")
else:
 print("mail is not spam")