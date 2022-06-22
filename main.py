import random
import telebot
import jokepuller

TOKEN = '5472600721:AAFkP9FdpKA-oIDKYYWgC2IvnldNQ6PE4Cs'
HELP_MESSAGE='Hi! I am TeleChuck_bot.\n' \
			 'You can interact with me using the following commands: \n\n' \
			 'gimme <id> - I will reply you back with a Chuck Norris joke with the specidied id - <id> must fulfill 1<=id<=101 as there is only limited amount of Chuck Norris jokes (unfortunately).\n\n' \
			 'gimme - I will reply you back with one of my random Chuck Norris jokes.\n\n' \
			 '/help - provide information about my capabilities and commands.\n\n' \
			 '/start - provide information about my capabilities and commands.\n' \


bot = telebot.TeleBot(TOKEN)
jp=jokepuller.JokePuller()

def reply(message,answer):
	bot.reply_to(message,answer)


@bot.message_handler(commands=['help','start'])
def send_help(message):
	reply(message,HELP_MESSAGE)

"""
Checks if some command is gimme valid.
Looks for a pattern of "gimme <x>" where 1<=x<=101
Returns a tuple that contains two parts:
	First part - a code that describes whether the command is legal:
		the code will be 0 - if the command is legal
		the code will be 1 - if "gimme" was detected provided id is not in the range
		the code will be 2 - if "gimme" was not detected

	Second part - the provided id (or -1 if an id was not provided).
"""
def is_gimme_x_valid(command):

	# removing redundant spaces
	parts=command.split(' ')
	parts=list(filter(lambda x:x!='',parts))

	for i in range(len(parts)) :
		try:
			parts[i]=parts[i].lower()
		except:
			do_nothing=0

	if (not 'gimme' in parts):
		return (2,-1)

	if(len(parts)==1):# just gimme
		return (0,-1)

	if(len(parts)==2):
		try:
			id=int(parts[1])
			if(1<=id and id<=101):
				return (0,id)
			else:
				return (0,1e9)
		except:
			return (1,-1)
	return (1,-1)

"""
Answers the gimme command:
	does nothing if 'gimme' was not detected
	if only gimme provided - answers with a random joke
	if gimme <id> provided - answers with joke #<id> or says that <id> is not supported
	otherwise, sends an error message.
"""
@bot.message_handler(func=lambda message: is_gimme_x_valid(message.text)[0]!=2)
def send_answer(message):

	(code,id)=is_gimme_x_valid(message.text)
	if(code==0):
		if(id==-1):#No id specified - a random joke
			id=random.randint(1,101)

		if(1<=id and id<=101):
			reply(message,jp.gimme(id))

		else:
			reply(message,"! I can only tell jokes in the range [1,101]")

	elif(code==1):
		reply(message,"! I have detected an incorrect use of the gimme command.\nYou may use the /help command to receive help.")



def main():
	bot.infinity_polling()

if(__name__=="__main__"):
	main()
