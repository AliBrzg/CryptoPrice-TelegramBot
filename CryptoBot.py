import telebot
import requests

# Set Bot Token
myBotToken = 'YOUR_API_KEY'
bot = telebot.TeleBot(myBotToken)

# Set Text Masseage Reply
@bot.message_handler(func = lambda message : True if (message.text == '/start') else False)
def echo_all(message):
	bot.send_message(message.chat.id, "Hi @" + message.chat.username
	+ "\nSend me your Symbol name")

@bot.message_handler(func = lambda message : True if (message.text == 'Hello') else False)
def echo_all(message):
	bot.send_message(message.chat.id, "Hi " + message.chat.username)

@bot.message_handler(content_types=['text'])
def echo_all(message):
	# Send Request & Parse Price Data
	myCryptoName = message.text.upper()
	myApi = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms='+ myCryptoName +'&tsyms=USD,EUR'
	price = requests.get(myApi)
	price = price.json()
		# Checking The Correctness Of The Data
	if "Response" in price:
		bot.reply_to(message, "Symbol Not Found ... \nTry Again")
	else:
		priceUsd = price[myCryptoName]['USD']
		priceUsd = str(priceUsd) + '$'
		if "EUR" in price[myCryptoName]:
			priceEur = price[myCryptoName]['EUR']
			priceEur = str(priceEur) + '€'
		
		# Send Price
		bot.reply_to(message,priceUsd)

# Run Bot
print ("\n"+" >>> The Bot Is Running ..."+"\n")
bot.infinity_polling()
