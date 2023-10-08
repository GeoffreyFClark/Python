import socket, string, time, thread
SERVER = “ ”
PORT = ####
NICKNAME = “ “
CHANNEL = “ “

def main():
    global IRC
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IRC.connect((SERVER, PORT))
thread.start_new_thread(Listener(),("Thread No:1",2))

def send_data(command):
    IRC.send(command + coordinatedatavariable)

def Listener():
    send_data('USER ___')
    send_data('NICK ___')
    while (1):
        buffer = IRC.recv(1024)
        msg = string.split(buffer)
        if msg[0] == "PING":
            print 'Pinged!'
        IRC.send("PONG %s" % msg[1] + '\n')

#The following code is in mIRC Scripting Language, for future reference:
on *:start: .temporarytextfile 60 0 temporarytextfile

alias temporarytextfile {
    set -l %filepath temporarytextfile.txt
if ($file(%filepath).mtime != %temporarytextfile) {
    set %temporarytextfile $file(%filepath).mtime
msg #channelname ($read(%filepath)
}
}
