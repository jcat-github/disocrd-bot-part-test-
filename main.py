
user_message = [
	["print", "python"],
	["print", "JavaScript"],
	["input", "python"],
]
bot_reply = [
	"print(\"print\")",
	"console.log(\"print\")",
	"input(\"input\")",
]
var = input("search: ").lower()
idx = 0
for i in user_message:
	contains = 0
	for x in i:
		if x in var:
			contains += 1
	if contains == len(i):
		print(bot_reply[idx])
		break
	idx += 1

if idx == len(bot_reply): print("nothing was matching.")
import main