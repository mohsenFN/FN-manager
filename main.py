from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Updater, Filters
import text_config, bot_config
import re

chat_id = 255877970
# command for giving list of admins
def admin_list(update, context):
    admin = ''
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        admin += '...'+i.user.name + '\n'
    context.bot.sendMessage(update.message.chat_id, "admins:\n{0}".format(admin))

del_f = False
def deletemsg(update,context):
    import pdb; pdb.set_trace()
    if update.message.forward_from != None:
        ad = False
        for i in context.bot.getChatAdministrators(update.message.chat_id):
            if update.message.from_user.id == i.user.id:
                ad = True
            elif update.message.from_user.id == chat_id:
                ad = True
        if not ad:
            context.bot.deleteMessage(update.message.chat_id, update.message.message_id)

def mh(update, context):
    ad = False
    for i in context.bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if not ad:
        for i in re.split(" ", update.message.text):
            if i == "coder":
                update.message.reply_text("haj mohsen")

        for i in re.split(" ", update.message.text.lower()):
            if i.startswith("http"):
                context.bot.deleteMessage(update.message.chat_id, update.message.message_id)
            elif i == "linux":
                update.message.reply_text("*Gnu/Linux")

    if update.message.text.lower() == "!report":
        for i in context.bot.getChatAdministrators(update.message.chat_id):
            if not i.user.is_bot:
                context.bot.sendMessage(i.user.id, "message below reported by @{0}".format(update.message.from_user.username))
                context.bot.forwardMessage(chat_id=i.user.id, from_chat_id=update.message.chat_id,
                                   message_id=update.message.reply_to_message.message_id)
    if update.message.text == 'kick':
        if ad:
            if update.message.from_user.id != chat_id:
                context.bot.kickChatMember(update.message.chat_id, update.message.reply_to_message.from_user.id)
    if update.message.text == 'Del':
        if ad:
            context.bot.deleteMessage(update.message.chat_id, update.message.reply_to_message.message_id)
    if update.message.text.lower() == "!ask":
        update.message.reply_to_message.reply_text(text_config.ask)
    if update.message.text.lower() == "!spam":
        update.message.reply_to_message.reply_text(text_config.spam)
    if update.message.text.lower() == "!link":
        if update.message.chat_id != -1001199151186:
            update.message.reply_to_message.reply_text("Python group @PySpy\ngeneral chat group https://t.me/joinchat/NhBFEBsFP1KCMOVewTQb_Q\nJS group https://t.me/prototypees")
        else:
            update.message.reply_to_message.reply_text("Python group @PySpy\ngeneral chat group https://t.me/joinchat/NhBFEBsFP1KCMOVewTQb_Q\nJS group https://t.me/prototypees")
    if update.message.text.lower()=="!kali":
        update.message.reply_to_message.reply_text(text_config.kali_answer)

# general functions
def start_function(update, context):
    update.message.reply_text(text_config.start_text)

def help_function(update, context):
    update.message.reply_text(text_config.help_text)

def coder_function(update, context):
    update.message.reply_text(text_config.coder_text)

updater = Updater(bot_config.token, use_context=True)
# general handlers
updater.dispatcher.add_handler(CommandHandler("start", start_function))
updater.dispatcher.add_handler(CommandHandler("help", help_function))
updater.dispatcher.add_handler(CommandHandler("coder", coder_function))

# group handlers
updater.dispatcher.add_handler(CommandHandler('admin', admin_list))
updater.dispatcher.add_handler(MessageHandler(Filters.all, mh))


# strating bot
print("running ... ")
updater.start_polling()
updater.idle()