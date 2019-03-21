#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import libraries
import telegram
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

# used for log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@run_async
def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['Hello', ''], ['COMPUETER NETWORKS', 'AUTOMATA THEORY'], ['OPERATING SYSTEMS', 'PYTHON LAB'],
                           ['COMPUTER ORGANIZATION AND ARCHITECTURE'], ['Report Bug', '']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b> Please Select Subject.</b>",parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

@run_async
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

@run_async
def text(update, context):
    if update.message.text == "START":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['Hello', ''], ['COMPUETER NETWORKS', 'AUTOMATA THEORY'],
                           ['OPERATING SYSTEMS', 'PYTHON LAB'],
                           ['COMPUTER ORGANIZATION AND ARCHITECTURE'], ['Report Bug', '']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b> Please Select Subject.</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "Hello":
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text='Hello {}'.format(update.message.from_user.first_name) + ',Welcome to the bot!')
    elif update.message.text == "COMPUETER NETWORKS" or update.message.text == "BACKCN":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['CN LABS AND ASSIGNMENT'],
                           ['CN STUDY MATERIAL'],
                           ['CN SOLUTION'],['START']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "AUTOMATA THEORY" or update.message.text == "BACKAT":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['AT TUTORIAL'],
                           ['AT STUDY MATERIAL'],
                           ['AT SOLUTION'],['START']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "OPERATING SYSTEMS" or update.message.text == "BACKOS":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['OS LAB AND ASSIGNMENT'],
                           ['OS STUDY MATERIAL'],
                           ['OS SOLUTION'], ['START']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "PYTHON LAB" or update.message.text == "BACKPY":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['PY LAB AND ASSIGNMENT'],
                           ['PY STUDY MATERIAL'],
                           ['PY SOLUTION'], ['START']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "COMPUTER ORGANIZATION AND ARCHITECTURE" or update.message.text == "BACKCOA" :
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['COA LAB AND ASSIGNMENT'],
                           ['COA SOLUTION'], ['START']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "Report Bug":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Contact:-</b> @pushpak1300",parse_mode=telegram.ParseMode.HTML)
    elif update.message.text == "CN LABS AND ASSIGNMENT":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['CN LABS 1'],
                           ['CN LABS 2'],
                           ['CN LABS 3'],
                           ['CN LABS 4'],
                           ['CN LABS 5'],
                           ['CN LABS 6'],
                           ['CN LABS 7'],
                           ['CN LABS 8'],
                           ['CN LABS 9'],
                           ['CN LABS 10'],
                           ['CN LABS 11'],
                           ['CN LABS 12'],
                           ['CN ASSIGNMENT 1'],
                           ['START', 'BACKCN']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "OS LAB AND ASSIGNMENT":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['OS LABS 1-1'],
                           ['OS LABS 1-2'],
                           ['OS LABS 1-3'],
                           ['OS LABS 2-1'],
                           ['OS LABS 2-2'],
                           ['OS LABS 2-3'],
                           ['OS LABS 3-1'],
                           ['OS LABS 3-2'],
                           ['OS LABS 4'],
                           ['OS LABS 5'],
                           ['OS LABS 6'],
                           ['OS LABS 7'],
                         ['START', 'BACKOS']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "PY LAB AND ASSIGNMENT":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['PY LABS 1'],
                           ['PY LABS 2'],
                           ['PY LABS 3'],
                           ['PY LABS 4'],
                           ['PY LABS 5'],
                           ['PY LABS 6'],
                           ['PY LABS 7'],
                           ['PY LABS 8'],
                           ['PY LABS 9'],
                           ['PY LABS 10'],
                           ['PY LABS 11'],
                           ['PY LABS 12'],
                           ['PY ASSIGNMENT 1'],
                           ['PY ASSIGNMENT 2'],
                           ['START', 'BACKPY']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "AT TUTORIAL":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['AT TUTORIAL 1'],
                           ['AT TUTORIAL 2'],
                           ['AT TUTORIAL 3'],
                           ['AT TUTORIAL 4'],
                           ['AT TUTORIAL 5'],
                           ['AT TUTORIAL 6'],
                           ['AT TUTORIAL 7'],
                           ['AT TUTORIAL 8'],
                           ['START', 'BACKAT']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "COA LAB AND ASSIGNMENT":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        custom_keyboard = [['COA LABMANUAL'],
                           ['COA ASSIGNMENT 1'],
                           ['START', 'BACKCOA']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                                 parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    elif update.message.text == "CN SOLUTION" or update.message.text == "COA SOLUTION" or update.message.text == "PY SOLUTION" or update.message.text == "AT SOLUTION" or update.message.text == "OS SOLUTION":
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>BOT IS STILL IN BETA VERSION CONTACT :- </b>@pushpak1300",
                                 parse_mode=telegram.ParseMode.HTML)
    elif update.message.text == "COA LABMANUAL":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('COA/labmanual.pdf', 'rb'))
    elif update.message.text == "COA ASSIGNMENT 1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('COA/coaassignment1.docx', 'rb'))
    elif update.message.text == "CN LABS 1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment1.pdf', 'rb'))
    elif update.message.text == "CN LABS 2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment2.pdf', 'rb'))
    elif update.message.text == "CN LABS 3":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment3.docx', 'rb'))
    elif update.message.text == "CN LABS 4":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment4.docx', 'rb'))
    elif update.message.text == "CN LABS 5":
        ccontext.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment5.docx', 'rb'))
    elif update.message.text == "CN LABS 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment6.docx', 'rb'))
    elif update.message.text == "CN LABS 7":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment7.docx', 'rb'))
    elif update.message.text == "CN LABS 8":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment8.docx', 'rb'))
    elif update.message.text == "CN LABS 9":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment9.docx', 'rb'))
    elif update.message.text == "CN LABS 10":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment10.docx', 'rb'))
    elif update.message.text == "CN LABS 11":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment11.docx', 'rb'))
    elif update.message.text == "CN LABS 12":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment12.docx', 'rb'))
    elif update.message.text == "OS LABS 1-1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-1.pdf', 'rb'))
    elif update.message.text == "OS LABS 1-2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-2.pdf', 'rb'))
    elif update.message.text == "OS LABS 1-3":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-3.pdf', 'rb'))
    elif update.message.text == "OS LABS 2-1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-1.pdf', 'rb'))
    elif update.message.text == "OS LABS 2-2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-2.pdf', 'rb'))
    elif update.message.text == "OS LABS 2-3":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-3.pdf', 'rb'))
    elif update.message.text == "OS LABS 3-1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab3-1.pdf', 'rb'))
    elif update.message.text == "OS LABS 3-2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab3-2.pdf', 'rb'))
    elif update.message.text == "OS LABS 4":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab4.pdf', 'rb'))
    elif update.message.text == "OS LABS 5":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab5.pdf', 'rb'))
    elif update.message.text == "OS LABS 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab6.pdf', 'rb'))
    elif update.message.text == "OS LABS 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab6.pdf', 'rb'))
    elif update.message.text == "PY LABS 1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment1.pdf', 'rb'))
    elif update.message.text == "PY LABS 2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment2.pdf', 'rb'))
    elif update.message.text == "PY LABS 3":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment3.pdf', 'rb'))
    elif update.message.text == "PY LABS 4":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment4.pdf', 'rb'))
    elif update.message.text == "PY LABS 5":
        ccontext.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment5.pdf', 'rb'))
    elif update.message.text == "PY LABS 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment6.pdf', 'rb'))
    elif update.message.text == "PY LABS 7":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment7.pdf', 'rb'))
    elif update.message.text == "PY LABS 8":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment8.pdf', 'rb'))
    elif update.message.text == "PY LABS 9":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment9.pdf', 'rb'))
    elif update.message.text == "PY LABS 10":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment10.pdf', 'rb'))
    elif update.message.text == "PY LABS 11":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment11.pdf', 'rb'))
    elif update.message.text == "PY LABS 12":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment12.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 1.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 2.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 3":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 3.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 4":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 4.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 5":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 5.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 6.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 7":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial no 7.pdf', 'rb'))
    elif update.message.text == "AT TUTORIAL 6":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('AT/Tutorial No 8.pdf', 'rb'))
    elif update.message.text == "PY ASSIGNMENT 1":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/assignmentno1.pdf', 'rb'))
    elif update.message.text == "PY ASSIGNMENT 2":
        context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/assignmentno2.pdf', 'rb'))
    elif update.message.text == "AT STUDY MATERIAL" or update.message.text == "COA STUDY MATERIAL" or update.message.text == "OS STUDY MATERIAL" or update.message.text == "CN STUDY MATERIAL" or update.message.text == "PY STUDY MATERIAL":
        context.bot.send_message(chat_id=update.message.chat_id,text='<b>Click :-</b><a href="https://tinyurl.com/seit-bot">Link Is Here</a>',parse_mode=telegram.ParseMode.HTML)
    else:
        Context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.message.chat_id, text="Please Send The Text Message!!")


@run_async
def unknown(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        v=2
        # remove update.message.chat_id from conversation list
    except BadRequest:
        context.bot.send_message(chat_id=update.message.chat_id, text="BAD REQUEST ERROR")
        # handle malformed requests - read more below!
    except TimedOut:
        context.bot.send_message(chat_id=update.message.chat_id, text="TIMED OUT ERROR")
        # handle slow connection problems
    except NetworkError:
        context.bot.send_message(chat_id=update.message.chat_id, text="NETWORK ERROR")
        # handle other connection problems
    except ChatMigrated as e:
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        context.bot.send_message(chat_id=update.message.chat_id, text="DONT TAKE TENSION WE WILL HANDLE IT")
        # handle all other telegram related errors

def main():
    # it is use to crete updater object
    updater = Updater(token='Token', use_context=True)

    # defining job queue
    j = updater.job_queue
    # it is use to create dispatcher
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    #text handler
    text_handler = MessageHandler(Filters.text,text)
    dispatcher.add_handler(text_handler)





    # Message is either video, photo, or document (generic file)
    pls_handler = MessageHandler(Filters.video | Filters.photo | Filters.document, start)
    dispatcher.add_handler(pls_handler)



    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

    #jobqueuer stop
    j.stop()

if __name__ == '__main__':
    main()






