__coder__ = "mohsen-fn"
__channel__ = "t.me/freezed_cash"
__github__ = "github.com/mohsenFn"

"-------------------------- CODE STARTS HERE! --------------------------"

from telegram.ext import CommandHandler, MessageHandler, RegexHandler
from telegram.ext import Updater, Filters, run_async
from sql_manager import insert_qa, asnwer_to_q, all_q_a, delete_q
from warn_sql import insert_warn, check_warns
from config import *
from re import split

# sub variables --> should be global while using in functions
chat_id = 255877970 # admin's chat id
lock_link_var = None
lock_forward_var = None
lock_sticker_var = None
max_warn = 3

# command for giving list of admins
def admin_list(update, context):
    admin = ''
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        admin += '...'+i.user.name + '\n'
    context.bot.sendMessage(update.message.chat_id, "admins:\n{0}".format(admin))

# function for turning off an on the anti-link
def set_anti_link(update, context):
    global lock_link_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    
    if context.args[0].lower() == "on":
        if is_admin:
            lock_link_var = True
            update.message.reply_text("anti-link is on")
    else:
        if is_admin:
            lock_link_var = False
            update.message.reply_text("anti-link is off")

# function for setting lock sticker on and off
def set_anti_sticker(update, context):
    global lock_sticker_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

    if context.args[0].lower() == "on":
        if is_admin:
            lock_sticker_var = True
            update.message.reply_text("anti-sticker is on")
    else:
        if is_admin:
            lock_sticker_var = False
            update.message.reply_text("anti-sticker is off")

# function for setting lock forward on and off
def set_anti_forward(update, context):
    global lock_forward_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    
    if context.args[0].lower() == "on":
        if is_admin:
            lock_forward_var = True
            update.message.reply_text("anti-forward is on")
    else:
        if is_admin:
            lock_forward_var = False
            update.message.reply_text("anti-forward is off")

# function for smart questions
def set_qa_function(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
        
    # help for /add command --> how to : /command help
    if context.args[0] == "help":
        if is_admin:
            update.message.reply_text(insert_qa_help_text)
        
    # shows list of all Iquestions and asnwers
    elif context.args[0] == "all" or context.args[0] == "list":
        if is_admin:
            # text to send user
            text_ts = ''
            for row in all_q_a():
                text_ts = text_ts+'\n'+row[0]+' --> '+' '.join(eval(row[1]))
            update.message.reply_text(text_ts)

    
    elif context.args[0] == "rm":
        if is_admin:
            try:
                delete_q(context.args[1])
                update.message.reply_text("specified command deleted")
            except Exception as error:
                print(error)
    # inserting admins Iquestions and asnwers to database
    else:
        if is_admin and str(context.args[0]).startswith('!'):
            try:
                insert_qa(str(context.args[0]), str(context.args[1:]))
                update.message.reply_text("added !")
            
            except:
                update.message.reply_text("you have the same smart-question")

# function for warning users
def warn_function(update, context):
    global lock_forward_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    if is_admin:
        user_for_warn = update.message.reply_to_message.from_user.id

        try:
            insert_warn(user_for_warn, 1)
            count_warns = check_warns(user_for_warn)
            # removes user if her/his warn_count is over 2 and if not : it will add warn to user
            if len(count_warns) >= 3 :
                context.bot.kickChatMember(update.message.chat_id, user_for_warn)
                update.message.reply_text(user_kicked_text.format(update.message.reply_to_message.from_user.first_name,update.message.reply_to_message.from_user.id))
                
            else:
                update.message.reply_text(user_warned_text.format(update.message.reply_to_message.from_user.first_name,
                                                                  update.message.reply_to_message.from_user.id,
                                                                  len(check_warns(user_for_warn))))
                # TODO: add count of warns user have DONE
                # TODO: remove user if warns counts is 3 (or more (in case for bugs)) DONE
        except Exception as error:
            print(error)


# general group manager
@run_async
def general_manager(update, context):
    #global varibale for removing links based on varible from another function
    global lock_link_var
    # variable for checkign the user is admin or no
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

        if lock_link_var == True:
            for i in split(" ", update.message.text.lower()):
                if i.startswith("http:") or  i.startswith("https:"):
                    context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
            for i in split("\n", update.message.text.lower()):
                if i.startswith("http:") or  i.startswith("https:"):
                    context.bot.deleteMessage(update.message.chat_id, update.message.message_id)

    
        for i in split(" ", update.message.text.lower()):
            if i == "linux":
                update.message.reply_text("*Gnu/Linux")

    # reported message will be forwarded to admin
    if update.message.text.lower() == "@admin":
        for i in context.bot.getChatAdministrators(update.message.chat_id):
            if not i.user.is_bot:
                context.bot.sendMessage(i.user.id, "message below reported by @{0}".format(update.message.from_user.username))
                context.bot.forwardMessage(chat_id=i.user.id, from_chat_id=update.message.chat_id,
                                   message_id=update.message.reply_to_message.message_id)

    if update.message.text == '!kick':
        if is_admin:
            if update.message.from_user.id != chat_id:
                context.bot.kickChatMember(update.message.chat_id, update.message.reply_to_message.from_user.id)
    if update.message.text == '!del':
        if is_admin:
            context.bot.deleteMessage(update.message.chat_id, update.message.reply_to_message.message_id)
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
    if update.message.text.lower() == "!ask":
        update.message.reply_to_message.reply_text(ask)

    if update.message.text.lower() == "!spam":
        update.message.reply_to_message.reply_text(spam)

    if update.message.text.lower() == "!link":
        update.message.reply_to_message.reply_text(links)

    if update.message.text.lower()=="!kali":
        update.message.reply_to_message.reply_text(kali_answer)

# sticker handler for deleting it
def sticker_manager(update, context):
    #global varibale for removing links based on varible from another function
    global lock_sticker_var
    if lock_sticker_var:
        try:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        except:
            pass

# manager for custom Q-A s
def qa_manager(update, context):
    user_q = update.message.text.lower()
    try:
         update.message.reply_to_message.reply_text(
            ' '.join(eval((asnwer_to_q(user_q)[0][0])))
        )
    except Exception as error:
        print(error)

# forwarded message handler for deleting it
def forward_manager(update, context):
    #global varibale for removing links based on varible from another function
    global lock_forward_var
    if lock_forward_var:
        try:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        except:
            pass

# function for sending info about user
def me_function(update, context):
    # FU means from user XD
    fu = update.message.from_user
    update.message.reply_text(me_text.format(fu.first_name, fu.last_name,
                                                         fu.username ,fu.id, fu.is_bot))

# function to get list of settings
def settings_function(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    if is_admin:
        update.message.reply_text(setting_text.format(lock_sticker_var, lock_link_var, lock_forward_var, max_warn))
# purge function for deleting
@run_async
def purge(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

    count = int(context.args[0])
    if is_admin:
        for i in range(count):
            try:
                context.bot.deleteMessage(update.message.chat_id, update.message.message_id-i)
            except:
                pass

# start funvtion
@run_async
def start_function(update, context):
    update.message.reply_text(start_text)

# help function
def help_function(update, context):
    global lock_forward_var
    global lock_link_var
    global lock_sticker_var
    global max_warn
    update.message.reply_text(help_text.format(
        lock_sticker_var, lock_link_var,
        lock_forward_var, max_warn
    ))

# code functon
def coder_function(update, context):
    update.message.reply_text(coder_text)



"-------------------------- HANDLERS DOWN HERE! --------------------------"
updater = Updater(token, use_context=True)
# general handlers
updater.dispatcher.add_handler(CommandHandler("start", start_function))
updater.dispatcher.add_handler(CommandHandler("help", help_function))
updater.dispatcher.add_handler(CommandHandler("coder", coder_function))

# group handlers
updater.dispatcher.add_handler(CommandHandler('anti_link', set_anti_link)) # /anti_link on|off for anti link option
updater.dispatcher.add_handler(CommandHandler('anti_sticker', set_anti_sticker)) # /anti_sticker on|off for anti sticker option
updater.dispatcher.add_handler(CommandHandler('anti_forward', set_anti_forward)) # /anti_forward on|off for anti forward option
updater.dispatcher.add_handler(CommandHandler('admin', admin_list)) # gives list of admins
updater.dispatcher.add_handler(CommandHandler('rm', purge)) # /rm 10 > removes last 10 messages
updater.dispatcher.add_handler(CommandHandler('warn', warn_function)) # functionto warn non-admin members
updater.dispatcher.add_handler(CommandHandler('me', me_function)) # /me gives info about you
updater.dispatcher.add_handler(CommandHandler('settings', settings_function)) # function to get list of settings
updater.dispatcher.add_handler(CommandHandler("add", set_qa_function)) # multi process command for adding|removing|checking smart questions
updater.dispatcher.add_handler(MessageHandler(Filters.regex(('!\w+')), qa_manager)) # regex handler for smart questions and answers
updater.dispatcher.add_handler(MessageHandler(Filters.forwarded, forward_manager)) # forwarded masages handler 
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, sticker_manager)) # deletes sticker if its on
updater.dispatcher.add_handler(MessageHandler(Filters.text, general_manager)) # general message handler

# strating bot
print("running ... ")
updater.start_polling()
updater.idle()