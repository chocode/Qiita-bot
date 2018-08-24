from slackbot.bot import respond_to
from slackbot.bot import default_reply
import random

@respond_to("おみくじ")
def kuji(message):
	# おみくじの中身と、生起確率
	fortune = ["大吉", "中吉", "吉", "凶", "大凶"]
	kakuritu = [10, 25, 30, 25, 10]

	rnd = random.randint(1, sum(kakuritu))
	val = 0
	hit = 0

	for i in range(0, len(fortune)-1):
		val += kakuritu[i-1]
		if rnd <= val and hit == 0:
			hit = i

	message.reply("今日の運勢は 【" + fortune[hit] + "】 です。")

@default_reply()
def error_func(message):
	message.reply("コマンドを間違えてませんか？？")
