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


# defination of function for our bot
@run_async
def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['/hello (say Hello!)',''],['/cn (COMPUETER NETWORKS)', '/at (AUTOMATA THEORY)'],['/os (OPERATING SYSTEMS)', '/py (PYTHON LAB)'], ['/coa (COMPUTER ORGANIZATION AND ARCHITECTURE)'],['Report Bug:- @pushpak1300','']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b> Please Select Subject.</b>",parse_mode = telegram.ParseMode.HTML, reply_markup=reply_markup)


@run_async
def unknown(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


@run_async
def pls(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(chat_id=update.message.chat_id, text="Please Send The Text Message!!")


'''def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)'''


def cn(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: CN LABS :-', '/cnassignment'],
                       ['2: CN STUDY MATERIAL :-', '/cnstudymaterial'],
                       ['3: CN SLUTION:-', '/cnsolution'], ['/start (HOME)', '']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",parse_mode = telegram.ParseMode.HTML, reply_markup=reply_markup)

def at(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="You Choose Automata-Theory Subject!")


def os(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: OS LABS :-', '/oslab'],
                       ['2: OS STUDY MATERIAL :-', '/osstudymaterial'],
                       ['3: OS SLUTION:-', '/ossolution'], ['/start (HOME)', '']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",
                             parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def py(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: PYTHON LABS :-', '/pyassignment'],
                       ['2: PYTHON STUDY MATERIAL :-', '/pystudymaterial'],
                       ['3: PYTHON SOLUTION:-', '/pysolution'], ['/start (HOME)', '']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the Option!</b>",parse_mode = telegram.ParseMode.HTML, reply_markup=reply_markup)


def coa(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You Choose Computer-Organization-Architeture Subject!")


def hello(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Hello {}'.format(update.message.from_user.first_name)+'Welcome to the bot!')


def cnassignment(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: CN LABS 1 :-', '/cnassignment1'],
                       ['2: CN LABS 2 :-', '/cnassignment2'],
                       ['3: CN LABS 3 :-', '/cnassignment3'],
                       ['4: CN LABS 4 :-', '/cnassignment4'],
                       ['5: CN LABS 5 :-', '/cnassignment5'],
                       ['6: CN LABS 6 :-', '/cnassignment6'],
                       ['7: CN LABS 7 :-', '/cnassignment7'],
                       ['8: CN LABS 8 :-', '/cnassignment8'],
                       ['9: CN LABS 9 :-', '/cnassignment9'],
                       ['10: CN LABS 10 :-', '/cnassignment10'],
                       ['11: CN LABS 11 :-', '/cnassignment11'],
                       ['12: CN LABS 12 :-', '/cnassignment12'],
                       ['/start (HOME)', '/back (back)']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                             parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

def oslab(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: OS LABS 1-1 :-', '/oslab11'],
                       ['2: OS LABS 1-2 :-', '/oslab12'],
                       ['3: OS LABS 1-3 :-', '/oslab13'],
                       ['4: OS LABS 2-1 :-', '/oslab21'],
                       ['5: OS LABS 2-2 :-', '/oslab22'],
                       ['6: OS LABS 2-3 :-', '/oslab23'],
                       ['7: OS LABS 3-1 :-', '/oslab31'],
                       ['8: OS LABS 3-2 :-', '/oslab32'],
                       ['9: OS LABS 4 :-', '/oslab4'],
                       ['10: OS LABS 5 :-', '/oslab5'],
                       ['11: OS LABS 6 :-', '/oslab6'],
                       ['12: OS LABS 7 :-', '/oslab7'],
                       ['/start (HOME)', '/back (back)']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                             parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)


def pyassignment(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    custom_keyboard = [['1: PY LABS 1 :-', '/PYassignment1'],
                       ['2: PY LABS 2 :-', '/PYassignment2'],
                       ['3: PY LABS 3 :-', '/PYassignment3'],
                       ['4: PY LABS 4 :-', '/PYassignment4'],
                       ['5: PY LABS 5 :-', '/PYassignment5'],
                       ['6: PY LABS 6 :-', '/PYassignment6'],
                       ['7: PY LABS 7 :-', '/PYassignment7'],
                       ['8: PY LABS 8 :-', '/PYassignment8'],
                       ['9: PY LABS 9 :-', '/PYassignment9'],
                       ['10: PY LABS 10 :-', '/PYassignment10'],
                       ['11: PY LABS 11 :-', '/PYassignment11'],
                       ['12: PY LABS 12 :-', '/PYassignment12'],
                       ['/start (HOME)', '/backpy (back)']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text="<b>Please Select the labs!</b>",
                             parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    
def cnassignment1(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment1.pdf', 'rb'))


def cnassignment2(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment2.pdf', 'rb'))


def cnassignment3(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment3.docx', 'rb'))


def cnassignment4(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment4.docx', 'rb'))


def cnassignment5(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment5.docx', 'rb'))


def cnassignment6(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment6.docx', 'rb'))


def cnassignment7(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment7.docx', 'rb'))


def cnassignment8(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment8.docx', 'rb'))


def cnassignment9(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment9.docx', 'rb'))


def cnassignment10(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment10.docx', 'rb'))


def cnassignment11(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('CN/cnassignment11.docx', 'rb'))

def cnassignment12(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document="http://www.africau.edu/images/default/sample.pdf")


def pyassignment1(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment1.pdf', 'rb'))


def pyassignment2(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment2.pdf', 'rb'))


def pyassignment3(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment3.pdf', 'rb'))


def pyassignment4(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment4.pdf', 'rb'))


def pyassignment5(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment5.pdf', 'rb'))


def pyassignment6(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment6.pdf', 'rb'))


def pyassignment7(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment7.pdf', 'rb'))


def pyassignment8(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment8.pdf', 'rb'))


def pyassignment9(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment9.pdf', 'rb'))


def pyassignment10(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment10.pdf', 'rb'))


def pyassignment11(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment11.pdf', 'rb'))

def pyassignment12(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('PY/PYassignment12.pdf', 'rb'))

def oslab11(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-1.pdf', 'rb'))

def oslab12(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-2.pdf', 'rb'))

def oslab13(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab1-3.pdf', 'rb'))

def oslab21(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-1.pdf', 'rb'))

def oslab22(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-2.pdf', 'rb'))

def oslab23(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab2-3.pdf', 'rb'))

def oslab31(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab3-1.pdf', 'rb'))

def oslab32(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab3-2.pdf', 'rb'))

def oslab4(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab4.pdf', 'rb'))

def oslab5(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab5.pdf', 'rb'))

def oslab6(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab6.pdf', 'rb'))

def oslab7(update, context):
    context.bot.send_document(chat_id=update.message.chat_id, document=open('OS/oslab7.pdf', 'rb'))

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I did not understand text!,try Command.")


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='C',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        v=2
        # remove update.message.chat_id from conversation list
    except BadRequest:
        v=2
        # handle malformed requests - read more below!
    except TimedOut:
        v=2
        # handle slow connection problems
    except NetworkError:
        v=2
        # handle other connection problems
    except ChatMigrated as e:
        v=2
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        v=2
        # handle all other telegram related errors


def callback_goodmorning(context):
    context.bot.send_message(chat_id='897193693',text='Good Morning!')





def main():
    # it is use to crete updater object
    updater = Updater(token='629846052:AAEc3aarafrhMxcrICA_kOLS2LsSv4fjmUg', use_context=True)



    #defining job queue
    j = updater.job_queue
    # it is use to create dispatcher
    dispatcher = updater.dispatcher

    # command adder and it's dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    #CN
    cn_handler = CommandHandler('cn', cn)
    dispatcher.add_handler(cn_handler)

    cnassignment_handler = CommandHandler('cnassignment', cnassignment)
    dispatcher.add_handler(cnassignment_handler)

    cnassignment1_handler = CommandHandler('cnassignment1', cnassignment1)
    dispatcher.add_handler(cnassignment1_handler)

    cnassignment2_handler = CommandHandler('cnassignment2', cnassignment2)
    dispatcher.add_handler(cnassignment2_handler)

    cnassignment3_handler = CommandHandler('cnassignment3', cnassignment3)
    dispatcher.add_handler(cnassignment3_handler)

    cnassignment4_handler = CommandHandler('cnassignment4', cnassignment4)
    dispatcher.add_handler(cnassignment4_handler)

    cnassignment5_handler = CommandHandler('cnassignment5', cnassignment5)
    dispatcher.add_handler(cnassignment5_handler)

    cnassignment6_handler = CommandHandler('cnassignment6', cnassignment6)
    dispatcher.add_handler(cnassignment6_handler)

    cnassignment7_handler = CommandHandler('cnassignment7', cnassignment7)
    dispatcher.add_handler(cnassignment7_handler)

    cnassignment8_handler = CommandHandler('cnassignment8', cnassignment8)
    dispatcher.add_handler(cnassignment8_handler)

    cnassignment9_handler = CommandHandler('cnassignment9', cnassignment9)
    dispatcher.add_handler(cnassignment9_handler)

    cnassignment10_handler = CommandHandler('cnassignment10', cnassignment10)
    dispatcher.add_handler(cnassignment10_handler)

    cnassignment11_handler = CommandHandler('cnassignment11', cnassignment11)
    dispatcher.add_handler(cnassignment11_handler)

    cnassignment12_handler = CommandHandler('cnassignment12', cnassignment12)
    dispatcher.add_handler(cnassignment12_handler)
    
    #PY
    
    PY_handler = CommandHandler('py', py)
    dispatcher.add_handler(PY_handler)

    PYassignment_handler = CommandHandler('pyassignment', pyassignment)
    dispatcher.add_handler(PYassignment_handler)

    PYassignment1_handler = CommandHandler('pyassignment1', pyassignment1)
    dispatcher.add_handler(PYassignment1_handler)

    PYassignment2_handler = CommandHandler('pyassignment2', pyassignment2)
    dispatcher.add_handler(PYassignment2_handler)

    PYassignment3_handler = CommandHandler('pyassignment3', pyassignment3)
    dispatcher.add_handler(PYassignment3_handler)

    PYassignment4_handler = CommandHandler('pyassignment4', pyassignment4)
    dispatcher.add_handler(PYassignment4_handler)

    PYassignment5_handler = CommandHandler('pyassignment5', pyassignment5)
    dispatcher.add_handler(PYassignment5_handler)

    PYassignment6_handler = CommandHandler('pyassignment6', pyassignment6)
    dispatcher.add_handler(PYassignment6_handler)

    PYassignment7_handler = CommandHandler('pyassignment7', pyassignment7)
    dispatcher.add_handler(PYassignment7_handler)

    PYassignment8_handler = CommandHandler('pyassignment8', pyassignment8)
    dispatcher.add_handler(PYassignment8_handler)

    PYassignment9_handler = CommandHandler('pyassignment9', pyassignment9)
    dispatcher.add_handler(PYassignment9_handler)

    PYassignment10_handler = CommandHandler('pyassignment10',pyassignment10)
    dispatcher.add_handler(PYassignment10_handler)

    PYassignment11_handler = CommandHandler('pyassignment11', pyassignment11)
    dispatcher.add_handler(PYassignment11_handler)

    PYassignment12_handler = CommandHandler('pyassignment12', pyassignment12)
    dispatcher.add_handler(PYassignment12_handler)
    

    back_handler = CommandHandler('backcn', cn)
    dispatcher.add_handler(back_handler)

    back_handler1 = CommandHandler('backpy', py)
    dispatcher.add_handler(back_handler1)

    back_handler2 = CommandHandler('backos', os)
    dispatcher.add_handler(back_handler2)

    at_handler = CommandHandler('at', at)
    dispatcher.add_handler(at_handler)

    os_handler = CommandHandler('os', os)
    dispatcher.add_handler(os_handler)

    oslab_handler = CommandHandler('oslab', oslab)
    dispatcher.add_handler(oslab_handler)

    oslab11_handler = CommandHandler('oslab11', oslab11)
    dispatcher.add_handler(oslab11_handler)

    oslab12_handler = CommandHandler('oslab12', oslab12)
    dispatcher.add_handler(oslab12_handler)

    oslab13_handler = CommandHandler('oslab13', oslab13)
    dispatcher.add_handler(oslab13_handler)

    oslab21_handler = CommandHandler('oslab21', oslab21)
    dispatcher.add_handler(oslab21_handler)

    oslab22_handler = CommandHandler('oslab22', oslab22)
    dispatcher.add_handler(oslab22_handler)

    oslab23_handler = CommandHandler('oslab23', oslab23)
    dispatcher.add_handler(oslab23_handler)

    oslab31_handler = CommandHandler('oslab31', oslab31)
    dispatcher.add_handler(oslab31_handler)

    oslab32_handler = CommandHandler('oslab32', oslab32)
    dispatcher.add_handler(oslab32_handler)

    oslab4_handler = CommandHandler('oslab4', oslab4)
    dispatcher.add_handler(oslab4_handler)

    oslab5_handler = CommandHandler('oslab5', oslab5)
    dispatcher.add_handler(oslab5_handler)

    oslab6_handler = CommandHandler('oslab6', oslab6)
    dispatcher.add_handler(oslab6_handler)

    oslab7_handler = CommandHandler('oslab7', oslab7)
    dispatcher.add_handler(oslab7_handler)

    coa_handler = CommandHandler('coa', coa)
    dispatcher.add_handler(coa_handler)

    py_handler = CommandHandler('py', py)
    dispatcher.add_handler(py_handler)

    hello_handler = CommandHandler('hello', hello)
    dispatcher.add_handler(hello_handler)

    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)

    # inline query handler
    inline_caps_handler = InlineQueryHandler(inline_caps)
    dispatcher.add_handler(inline_caps_handler)
    '''
     #job queue
    job_minute = j.run_repeating(callback_goodmorning, interval=90, first=0)
    '''
    # error handle
    dispatcher.add_error_handler(error_callback)   
    # unknown command message handling
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Message is either video, photo, or document (generic file)
    pls_handler = MessageHandler(Filters.video | Filters.photo | Filters.document, pls)
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
