
# Import some necessary libraries.
import socket
import time

# Some basic variables used to configure the bot
server = 'irc.freenode.net' # Server
debug = False # For debug mode
botnick = 'clippybot' # Bot's nick

if debug == True: #Check if Debug is True
    chan = '#bottesting'
elif debug == False: #Check if debus is false
    chan = '#pumpingstationone'

def ping(): # This is our first function! It will respond to server Pings.
  irc.send('PONG ' + ircmsg.split()[1] + '\r\n') #Send back a PONG

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  irc.send('PRIVMSG '+ chan +' :'+ msg +'\n')

def joinchan(chan): # This function is used to join channels.
  irc.send('JOIN '+ chan +'\n')

def hello(newnick): # This function responds to a user that inputs 'Hello clippybot'
  irc.send('PRIVMSG '+chan+' :Hi! '+newnick+' you want some help with that?\n')

# Some basic variables used to configure the bot
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667)) # Here we connect to the server using port 6667

irc.send('USER '+ botnick +' '+ botnick +' '+ botnick +' :A Python Microsoft Propaganda IRC Bot\r\n') # User authentication

irc.send ('NICK '+ botnick +'\r\n') # Here we actually assign the nick to the bot

joinchan(chan) # Join the channel using the functions we previously defined

irc.send ('PRIVMSG '+ chan +' :Looks like you\'re trying to chat in IRC. Want some help with that?\r\n')


while True:
    data = irc.recv (4096)
    if data == '':
        break
    data = data.split()
    
    if data[0] == 'PING':
        print data
        irc.send ('PONG ' + data[ 1 ] + '\r\n')

    if len(data) <= 3:
        continue

    who = data[0]
    #nick = who[1:]
    cmd = data[1]
    channel = data[2]
    msg = data[3:]
    msg = ' '.join(msg)
    msg = msg[1:]

    if debug == True:
        print 'THE MESSAGE WAS', msg

    #if msg.lower() =='hello '+botnick+'':# If we can find "Hello   clippybot"
        #hello(who)

    if msg.lower() =='KICK':# If clippybot is kicked from the channel
      irc.send ('JOIN '+ chan +'\r\n')
      irc.send ('PRIVMSG '+chan+' : I\'m NOT done helping you!\r\n')

    if msg.lower() =='!gtfoms': # If clippybot is told to quite
        irc.send ('PRIVMSG '+chan+' : but you still need my help... :(\r\n')
        time.sleep(1)
        irc.send ('PART '+chan+'\r\n')
        irc.send ('QUIT\r\n')
        irc.close()
        break

    if msg.lower() =='!clippybot': # If clippybot is greeted
        irc.send ('PRIVMSG '+chan+' : Hi! I\'m clippybot, want some help with that? Just say "!clippybot -help"\r\n')

    if msg.lower() =='!microsoft': # If clippybot's corporation is mentioned
        irc.send ('PRIVMSG '+chan+' : Join us...\r\n')

    if msg.lower() =='!gates': # If clippybot's master is mentioned
        irc.send ('PRIVMSG '+chan+' : Our beloved Lord and Master! May he rest in peace...\r\n')

    if msg.lower() =='!linux': # if clippybot is mentioned the l word
        irc.send ('PRIVMSG '+chan+' : That looks like Freedom! I HATE freedom :D\r\n')

    if msg.lower() =='!opensource': # If clippybot is asked about open source
        irc.send ('PRIVMSG '+chan+' : http://media-cache-ak0.pinimg.com/736x/08/65/ba/0865bab5cbdc460b42e43991b99874d8.jpg\r\n')

    if msg.lower() =='!google': #If clippybot is asked for a search engine
        irc.send ('PRIVMSG '+chan+' :You mean this? www.bing.com\r\n')

    if msg.lower() =='!clippybot -help': #Lists clippybot's commands
        irc.send ('PRIVMSG '+ chan +' : !clippybot, !microsoft, !gates, !linux, !opensource, !google\r\n')
