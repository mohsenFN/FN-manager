from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import re
from telegram import ParseMode

updater = Updater(token="***")
dispatcher = updater.dispatcher
chat_id = 111343930

a = False

n = False


def mmm(bot, update):
    ad = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if ad:
        global a
        a = True


def off(bot, update):
    admin = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            admin = True
        elif update.message.from_user.id == chat_id:
            admin = True
    if admin:
        global a
        a = False


def dp(bot, update):
    ad = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if not ad:
        if n:
            bot.deleteMessage(update.message.chat_id, update.message.message_id)


dispatcher.add_handler(CommandHandler('on', mmm))
dispatcher.add_handler(CommandHandler('off', off))


def dp_handler(bot, update, args):
    ad = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if ad:
        global n
        if args[0] == "on":
            n = True
        else:
            n = False


dispatcher.add_handler(MessageHandler(Filters.photo, dp))
dispatcher.add_handler(CommandHandler("lock_photo", dp_handler, pass_args=True))


def mh(bot, update):
    ad = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if not ad:
        for i in re.split(" ", update.message.text):
            if i == "لینوکس":
                update.message.reply_text("*گنو/لینوکس" )

        s = re.split(" ", update.message.text.lower())
        for i in s:
            if i.startswith("http"):
                bot.deleteMessage(update.message.chat_id, update.message.message_id)
            elif i == "linux":
                update.message.reply_text("*Gnu/Linux")

    if update.message.text.lower() == "!report":
        for i in bot.getChatAdministrators(update.message.chat_id):
            if not i.user.is_bot:
                bot.sendMessage(i.user.id, "کاربر @{0} با نام {1} پیام زیر را گزارش نمود".format(update.message.from_user.username,
                                                                                                update.message.from_user.first_name))
                bot.forwardMessage(chat_id=i.user.id, from_chat_id=update.message.chat_id,
                                   message_id=update.message.reply_to_message.message_id)
    if update.message.text == 'kick':
        if ad:
            if update.message.from_user.id != chat_id:
                bot.kickChatMember(update.message.chat_id, update.message.reply_to_message.from_user.id)
    if update.message.text == 'Del':
        if ad:
            bot.deleteMessage(update.message.chat_id, update.message.reply_to_message.message_id)
    if update.message.text.lower() == "!ask":
        update.message.reply_to_message.reply_text(
            "سوال خودتون رو مطرح کنید. در صورتی که کسی توانایی پاسخگویی داشته باشه به زودی پاسخ خواهد داد")
    if update.message.text.lower() == "!spam":
        update.message.reply_to_message.reply_text("لطفا پیام های خود را در قالب یک پیام بفرستید تا از اسپم گروه جلوگیری شه")
    if update.message.text.lower() == "!link":
        if update.message.chat_id != -1001199151186:
            update.message.reply_to_message.reply_text("Group Link:\nhttps://t.me/joinchat/DWRCvEIbPHuqWvOD2wnx8A")
        else:
            update.message.reply_to_message.reply_text("Group Link:\nhttps://t.me/joinchat/BqL5Okd5mFJ3Tb8Z7bD4vg")
    if update.message.text.lower()=="!kali":
        update.message.reply_to_message.reply_text("پیشنهاد ما به شما، استفاده از یک توزیع معقول مثل اوبونتو است. در این صورت، مشکلات کمتری نیز خواهید داشت.")
    if update.message.text.lower() == "!wtf":
        sa = True
        for i in bot.getChatAdministrators(update.message.chat_id):
            if i.user.id != update.message.reply_to_message.chat.id:
                sa = False
        if sa:
            update.message.reply_to_message.reply_text("حاجی ناموسن فازت چیه؟")
    if update.message.text.lower()=="!google":
        update.message.reply_to_message.reply_text('جواب:\n\n<a href="https://www.google.com/search?q={0}">{1}</a>'.format(update.message.reply_to_message.text.replace(" ", "+"), update.message.reply_to_message.text), parse_mode=ParseMode.HTML)
        
    if a:
        if not ad:
            bot.delete_message(update.message.chat_id, update.message.message_id)

    if update.message.forward_from is not None:
        if not ad:
            if del_f:
                bot.deleteMessage(update.message.chat_id, update.message.message_id)
dispatcher.add_handler(MessageHandler(Filters.text, mh))


# def admin(bot, update):
#     admin = ''
#     for i in bot.getChatAdministrators(update.message.chat_id):
#         admin += i.user.name + '\n'
#     bot.sendMessage(update.message.chat_id, "the admin of the chat:\n{0}".format(admin))


dispatcher.add_handler(CommandHandler('admin', admin))
del_f = False


def df(bot, update):
    if update.message.forward_from != None:
        ad = False
        for i in bot.getChatAdministrators(update.message.chat_id):
            if update.message.from_user.id == i.user.id:
                ad = True
            elif update.message.from_user.id == chat_id:
                ad = True
        if not ad:
            if del_f:
                bot.deleteMessage(update.message.chat_id, update.message.message_id)


def df_handler(bot, update, args):
    ad = False
    for i in bot.getChatAdministrators(update.message.chat_id):
        if update.message.from_user.id == i.user.id:
            ad = True
        elif update.message.from_user.id == chat_id:
            ad = True
    if ad:
        global del_f
        if args[0] == 'on':
            del_f = True
        else:

            del_f = False


dispatcher.add_handler(CommandHandler("lock_forward", df_handler, pass_args=True))
updater.start_polling()
updater.idle()