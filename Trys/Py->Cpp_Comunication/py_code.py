import subprocess

proc = subprocess.Popen("./cpp_code", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
state = "run"

while state == "run":
	input = raw_input("Message to CPP>> ")

	if input == "quit":
		state = "terminate" # any string other than "run" will do

	proc.stdin.write(input + "\n")
	print (proc.stdout.readline().rstrip("\n"))
