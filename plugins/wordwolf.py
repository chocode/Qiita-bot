from slackbot.bot import respond_to
from slackbot.bot import default_reply

@default_reply()
def error_func(message):
	message.reply("コマンドを間違えてませんか？？")
