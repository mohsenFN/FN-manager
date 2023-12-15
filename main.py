"-------------------------- 11111111111111111 --------------------------"

"------------------------ Number One Is Awake !--------------------------"

"-------------------------- 11111111111111111 --------------------------"


__coder__ = "mohsen-fn" 
__github__ = "github.com/mohsenFn"



from telegram.ext import CommandHandler, MessageHandler, RegexHandler, CallbackQueryHandler
from telegram.ext import Updater, Filters, run_async
from telegram import ChatPermissions, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from warnsDB import insert_warn, check_warns, remove_warns_by_id
from qaDB import insert_qa, asnwer_to_q, all_q_a, delete_q
from handy_modules import check_tfn, query_tfn
from config import *
from re import split
import jdatetime
from emoji import emojize


# sub variables --> should be global while using in functions
chat_id = admin # admin's chat id
lock_link_var = None
lock_forward_var = None
lock_sticker_var = None
lock_gifs_var = None
should_welcome = None
sleep_status = None
max_warn = 3

# keyboard for admin pannel
keyboard = [
                [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
            ]


# command for giving list of admins
@run_async
def admin_list(update, context):
    admin = ''
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        admin += '...'+i.user.name + '\n'
    context.bot.sendMessage(update.message.chat_id, "admins:\n{0}".format(admin))

# function for setting anti link on & off
@run_async
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

# function for setting anti sticker on & off
@run_async
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

# function for setting anti gif on & off
@run_async
def set_anti_gifs(update, context):
    global lock_gifs_var
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
            lock_gifs_var = True
            update.message.reply_text("anti-sticker is on")
    else:
        if is_admin:
            lock_gifs_var = False
            update.message.reply_text("anti-sticker is off")

# function for setting anti forward on & off
@run_async
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
@run_async
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

# function for setting welcome message off & one
@run_async
def set_should_welcome(update, context):
    global should_welcome
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
            should_welcome = True
            update.message.reply_text("welcome option is on")
    else:
        if is_admin:
            should_welcome = False
            update.message.reply_text("welcome option is off")

# function to mute users
@run_async
def mute_user_function(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    
    if is_admin:
        user_for_mute = update.message.reply_to_message.from_user.id
        try:
            if user_for_mute == context.bot.id:
                update.message.reply_text(cant_mute_bot_text)
            else:
                context.bot.restrictChatMember(update.message.chat_id , user_for_mute ,ChatPermissions(can_send_messages=False))
                update.message.reply_to_message.reply_text(muted_user_text)
        except Exception as error:
            print(error)

# function to unmute user(only muted ones)        
@run_async
def unmute_user_function(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    if is_admin:
        try:
            user_for_unmute = update.message.reply_to_message.from_user.id
            if user_for_unmute == context.bot.id:
                update.message.reply_text(":|")

            else:
                context.bot.restrictChatMember(update.message.chat_id, int(user_for_unmute),
                ChatPermissions(
                                         can_post_messages=True,
                                         can_send_media_messages=True,
                                         can_send_other_messages=True,
                                         can_add_web_page_previews=True) # specifing permisions
                                        )

                update.message.reply_text("Unmuted!")
        except Exception as error:
            print(error)

# function for warning users
@run_async
def warn_function(update, context):
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
            count_warns = check_warns(user_for_warn)
            # removes user if her/his warn_count is over 2 and if not : it will add warn to user
            if len(count_warns) >=2 :
                context.bot.kickChatMember(update.message.chat_id, user_for_warn)
                # removes all other warns after getting removed
                remove_warns_by_id(user_for_warn)
                try:
                    update.message.reply_text(user_kicked_text.format(update.message.reply_to_message.from_user.first_name,
                                                                    update.message.reply_to_message.from_user.id))
                except:
                    update.message.reply_text("user kicked")
          
            else:
                insert_warn(user_for_warn, 1)
                try:
                    update.message.reply_text(user_warned_text.format(update.message.reply_to_message.from_user.first_name,
                                                                    update.message.reply_to_message.from_user.id,
                                                                    len(check_warns(user_for_warn))))
                except:
                    update.message.reply_text("Warned !\nHas {} warns".format(len(check_warns(user_for_warn))))
        except Exception as error:
            print(error)

# function to remove users warning(s)
@run_async
def forgive_function(update, context):
    s_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    
    if is_admin:
        user_to_forgive = update.message.reply_to_message.from_user.id # type --> integer

        try:
            remove_warns_by_id(user_to_forgive)
            update.message.reply_text("User forgived !")
        except Exception as error:
            print(error)

@run_async
def sleep_function(update, context):
    global sleep_status
    # in this mode only non-admin users are going to be prevented from sending messages
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    try:
        if context.args[0].lower() == "on":
            if is_admin:
                context.bot.set_chat_permissions(update.message.chat_id, ChatPermissions(can_send_messages=False))
                update.message.reply_text(sleep_mode_on_text)
                sleep_status = True
                
        elif context.args[0].lower() == "off":
            if is_admin:
                context.bot.set_chat_permissions(update.message.chat_id, ChatPermissions(
                                         can_post_messages=True,
                                         can_send_media_messages=True,
                                         can_send_other_messages=True,
                                         can_add_web_page_previews=True) # specifing permisions
                                        )
                update.message.reply_text(sleep_mode_off_text)
                sleep_status == False
        elif context.args[0].lower() != "off" and context.args[0].lower() != "on":
            if is_admin:
                update.message.reply_text(sleep_wrong_text)
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
                if i.startswith("http:") or  i.startswith("https:") and not is_admin:
                    context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
            for i in split("\n", update.message.text.lower()):
                if i.startswith("http:") or  i.startswith("https:") and not is_admin:
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
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

    if lock_sticker_var and not is_admin:
        try:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        except:
            pass

# manager for custom Q&A s
@run_async
def qa_manager(update, context):
    user_q = update.message.text.lower()
    try:
         update.message.reply_to_message.reply_text(
            ' '.join(eval((asnwer_to_q(user_q)[0][0])))
        )
    except Exception as error:
        print(error)

# forwarded message handler for deleting it
@run_async
def forward_manager(update, context):
    #global varibale for removing forwardeds based on varible from another function
    global lock_forward_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

    if lock_forward_var and not is_admin:
        try:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        except:
            pass

# gits handler for deleting them
@run_async
def gifs_manager(update, context):
    global lock_gifs_var
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True

    if lock_gifs_var and not is_admin:
        try:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
        except:
            pass

# function for sending info about user
@run_async
def me_function(update, context):
    # FU means from user XD
    fu = update.message.from_user
    update.message.reply_text(me_text.format(fu.first_name, fu.last_name,
                                                         fu.username ,fu.id, fu.is_bot))

# admins pannel (Inline keyboard)
@run_async
def pannel_function(update, context):
    is_admin = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        # checks if the sender of message is admin of group or no
        if update.message.from_user.id == i.user.id:
            is_admin = True
            # checks sender of message is the main admin or no
        elif update.message.from_user.id == chat_id:
            is_admin = True
    if is_admin:
        try:
            keyboard = [
                [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Pannel : ', reply_markup=reply_markup)
        except Exception as error:
            print(error)

@run_async
def pannel_query_function(update, context):
    query = update.callback_query
    data = query.data
    message_id = query.message.message_id
    
    try:
        global lock_link_var
        global lock_forward_var
        global lock_sticker_var
        global lock_gifs_var
        global should_welcome
        global sleep_status

        if data == '1':
            if lock_link_var == True:
                lock_link_var = False
            else:
                lock_link_var = True
            keyboard = [
                [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
            ]
            query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))
        
        if data == '2':
            if lock_forward_var == True:
                lock_forward_var = False
            else:
                lock_forward_var = True
                keyboard = [
                    [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                    [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                    [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                    [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                    [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                    [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                    [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
                ]
                query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))

        if data == '3':
            if lock_sticker_var == True:
                lock_sticker_var = False
            else:
                lock_sticker_var = True
                keyboard = [
                    [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                    [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                    [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                    [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                    [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                    [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                    [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
                ]
                query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))
            

        if data == '4':
            if lock_gifs_var == True:
                lock_gifs_var = False
            else:
                lock_gifs_var = True
                keyboard = [
                    [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                    [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                    [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                    [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                    [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                    [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                    [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
                ]
                query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))

        if data == '5':
            if should_welcome == True:
                should_welcome = False
            else:
                should_welcome = True
                keyboard = [
                    [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                    [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                    [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                    [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                    [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                    [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                    [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
                ]
                query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))

        if data == '6':
            if sleep_status == True:
                sleep_status = False
            else:
                sleep_status = True
                keyboard = [
                    [InlineKeyboardButton(emojize(":umbrella: Anti-link"), callback_data='8'),InlineKeyboardButton(check_tfn(lock_link_var), callback_data='1')],
                    [InlineKeyboardButton(emojize(":speech_balloon: Anti-forward"), callback_data='9'),InlineKeyboardButton(check_tfn(lock_forward_var), callback_data='2')],
                    [InlineKeyboardButton(emojize(":alarm_clock: Anti-sticker"), callback_data='10'),InlineKeyboardButton(check_tfn(lock_sticker_var), callback_data='3')],
                    [InlineKeyboardButton(emojize(":cloud: Anti-gif"), callback_data='11'),InlineKeyboardButton(check_tfn(lock_gifs_var), callback_data='4')],
                    [InlineKeyboardButton(emojize(":cat: Welcomer"), callback_data='12'),InlineKeyboardButton(check_tfn(should_welcome), callback_data='5')],
                    [InlineKeyboardButton(emojize(":snake: Sleep"), callback_data='13'),InlineKeyboardButton(check_tfn(sleep_status), callback_data='6')],
                    [InlineKeyboardButton(emojize(":name_badge: max warn"), callback_data='14'),InlineKeyboardButton(max_warn, callback_data='7')],
                ]
                query.edit_message_text('Done !\nPannel : ', reply_markup=InlineKeyboardMarkup(keyboard))

    except Exception as error:
        print(error)
    
    # last data is about max warn number so we do nothing

# function for getting time in Jalali implementation
@run_async
def time_function(update, context):
    # time_ts --> time to send
    time_ts = jdatetime.datetime.now().strftime("%Y-%B-%d %H:%M")
    update.message.reply_text(time_ts)

@run_async
def welcome_function(update, context):
    global should_welcome
    if should_welcome:
        new_members = update.message.new_chat_members
        for new_member in new_members:
            try:
                update.message.reply_text(welcome_text.format(new_member.first_name))
            except:
                try:
                    update.message.reply_text(welcome_text_non_uni)
                except Exception as error:
                    print(error)

# function to get list of settings
@run_async
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
        update.message.reply_text(setting_text.format(lock_sticker_var, lock_link_var,
                                                      lock_forward_var, should_welcome,
                                                      max_warn))

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
@run_async
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
@run_async
def coder_function(update, context):
    update.message.reply_text(coder_text)

# distinguishing update and bot(token)
updater = Updater(token, use_context=True)

"-------------------------- HANDLERS DOWN HERE! --------------------------"
updater.dispatcher.add_handler(CommandHandler("start", start_function))
updater.dispatcher.add_handler(CommandHandler("help", help_function))
updater.dispatcher.add_handler(CommandHandler("coder", coder_function))

"------------------------ GROUP SETTING HANDLERS! ------------------------"
updater.dispatcher.add_handler(CommandHandler('anti_link', set_anti_link)) # /anti_link on|off for anti link option
updater.dispatcher.add_handler(CommandHandler('anti_sticker', set_anti_sticker)) # /anti_sticker on|off for anti sticker option
updater.dispatcher.add_handler(CommandHandler('anti_forward', set_anti_forward)) # /anti_forward on|off for anti forward option
updater.dispatcher.add_handler(CommandHandler('anti_gif', set_anti_gifs)) # /anti_gif on|off for anti forward option
updater.dispatcher.add_handler(CommandHandler('welc', set_should_welcome)) # /welc on|off for replying welcome to new members
updater.dispatcher.add_handler(CommandHandler('settings', settings_function)) # function to get list of settings
updater.dispatcher.add_handler(CommandHandler('pannel', pannel_function))
updater.dispatcher.add_handler(CallbackQueryHandler(pannel_query_function))

"---------------------- CHATTING SETTINGS HANDLERS! ----------------------"
updater.dispatcher.add_handler(CommandHandler('sleep', sleep_function))
updater.dispatcher.add_handler(CommandHandler('rm', purge)) # /rm 10 > removes last 10 messages
updater.dispatcher.add_handler(CommandHandler("add", set_qa_function)) # multi process command for adding|removing|checking smart questions

"----------------------- USERS SETTINGS HANDLERS! ------------------------"
updater.dispatcher.add_handler(CommandHandler('admin', admin_list)) # gives list of admins
updater.dispatcher.add_handler(CommandHandler('warn', warn_function)) # functionto warn non-admin members
updater.dispatcher.add_handler(CommandHandler('forgive', forgive_function))
updater.dispatcher.add_handler(CommandHandler('mute', mute_user_function)) # /mute to mute user
updater.dispatcher.add_handler(CommandHandler('unmute', unmute_user_function)) # /unmute to unmute user


"--------------------------- GLOABL HANDLERS! ----------------------------"
updater.dispatcher.add_handler(CommandHandler('me', me_function)) # /me gives info about you
updater.dispatcher.add_handler(CommandHandler('time', time_function)) # /time for getting time

"--------------------------- MESSAGE HANDLERS! ---------------------------"
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_function)) # handling new users event
updater.dispatcher.add_handler(MessageHandler(Filters.regex(('!\w+')), qa_manager)) # regex handler for smart questions and answers
updater.dispatcher.add_handler(MessageHandler(Filters.forwarded, forward_manager)) # forwarded masages handler 
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, sticker_manager)) # deletes sticker if its on
updater.dispatcher.add_handler(MessageHandler(Filters.text, general_manager)) # general message handler
updater.dispatcher.add_handler(MessageHandler(Filters.animation, gifs_manager))

# strating bot
print("running ... ")
updater.start_polling()
updater.idle()