import os
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import logging
import telegram
from telegram import (Poll, ParseMode, KeyboardButton, KeyboardButtonPollType,
					  ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, PollAnswerHandler, PollHandler, MessageHandler,
						  Filters, CallbackQueryHandler, ConversationHandler)
from telegram.utils.helpers import mention_html

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
	v = update.effective_user.id
	username = update.effective_user.full_name
	
	print("Hello")
	update.message.reply_text('Hello ' + str(username) + 'Please select /phone to give us your phone number and /location for location access.',parse_mode=telegram.ParseMode.HTML)
	

def phone(update, context):
    con_keyboard = KeyboardButton(text="send_contact", request_contact=True)

    custom_keyboard = [[ con_keyboard]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    update.message.reply_text("To identify yourself,pls. send phone no", reply_markup=reply_markup)
    return contact_callback

def contact_callback(update, context):
    contact = update.effective_message.contact
    phone = contact.phone_number
    print(phone)

def location(update, context):
	loc_keyboard = KeyboardButton(text="send_location", request_location=True)
	custom_keyboard = [[loc_keyboard]]
	reply_markup = ReplyKeyboardMarkup(custom_keyboard)

	update.message.reply_text("To identify yourself,pls. send location", reply_markup=reply_markup)
	return location_callback

def location_callback(update, context):
    message = None
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
    current_pos = (message.location.latitude, message.location.longitude)
    print(current_pos)

def error(update, context):
	logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
	updater = Updater("1422196143:AAHu4-nuZr3Pkv6CoNCJjpdriiCqzQbbefM", use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('phone', phone))
	dp.add_handler(CommandHandler('location', location))
	location_handler = MessageHandler(Filters.location, location_callback)
	dp.add_handler(location_handler)
	dp.add_handler(MessageHandler(Filters.contact, contact_callback))
	dp.add_error_handler(error)
	updater.start_polling()


	updater.idle()


if __name__ == '__main__':
	main()
