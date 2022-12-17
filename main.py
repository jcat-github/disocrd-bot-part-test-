special_dict = {["yes", "meow"]: "hi"}
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
var = input("type")
if var in special_dict:
	print("seccess")