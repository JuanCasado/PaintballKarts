from threading import Thread
import subprocess


class ComC (Thread):
    def __init__(self):
        Thread.__init__()
        self.proc = subprocess.Popen("./cpp_code", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        state = "run"
        while state == "run":
            inp = raw_input("Message to CPP>> ")
            if inp == "quit":
                state = "terminate"
            self.proc.stdin.write(inp + "\n")
            print(self.proc.stdout.readline().rstrip("\n"))


class ComP (Thread):
    def __init__(self):
        Thread.__init__()
