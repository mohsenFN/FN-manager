token = "573403283:AAHWfASnPy13q_2eEfILghgDHYTRzsnYtkI"
admin = 255877970 # for sending group stats and etc.
help_text = """ \

commands for all users
-->
/help shows you instruction of bot
/coder about coder and this code
/me data about user
/admin list of admins in current group
/time command for getting time(year-Month-Day Hour:minute)
-------------------------

command only for admins
-->
configing group settings
/anti_link <on>|<off> turns anti-link off or on
/anti_sticker <on>|<off> turns anti-link off or on
/anti_forward <on>|<off> turns anti-forward off or on
/welc <on>|<off> turns welcomer option off or on

/rm <int> removoes last <int> messages (some isuess)
/settings function to get list of settings
/add <help> to learn the instructions
/warn reply this to warn users
/mute and /unmute --> clear point :)
/sleep on|off for preventing users from chatting 

"""

me_text = """
FN group manager
first name : {}
last name : {}
user name : {}
id : {}
is bot : {}
"""

setting_text = """
to be sure about settings i use True and False
->True(on)\n->False(off)\n->None(not set)\n
anti sticker : {}
anti link : {}
anti forward : {}
welcome : {}
max warn : {}
"""

insert_qa_help_text = "use /add <question|comnmand> <asnwer|respond you want to get>\n  remember `!` should be your questions first character\nto delete a command use `/add rm <command name>`\nto see your all command use `/add <all|list>`"

kali_answer = "we recommend you ubuntu.becuase it's much wiser and easier to use and also much powerfull.\nyou can install your needed tools manully."

spam = "send your message in one scale to group seems more proper."

ask = "ask your question if anybody know, will asnwer." 

links = "Python group @PySpy\ngeneral chat group https://t.me/joinchat/NhBFEBsFP1KCMOVewTQb_Q\nJS group https://t.me/prototypees"

start_text = "slm\nbe bot modiriat goroh rabid khosh umadid\ncommands\n..../help\n..../coder"

coder_text = "mohsen-fn\n. . . . channel @freezed_cash\n. . . . pv @six_6_six\n. . . . github github.com/MohsenFN\n\ncheck this bots source on my github"

user_kicked_text = "user\nname -> {}\nid ->{}\nhas been removed due warns(3)"

user_warned_text = "user\nname -> {}\nid ->{}\nhas {} warns"

welcome_text = "Heeewha\n{} just joined the group !"

welcome_text_non_uni = "Heeewha\nwe have a new member !"

sleep_mode_on_text = "Sleep mode activted\nuse /sleep off for deactivating"

sleep_mode_off_text = "Sleep mode is no longer active"

sleep_wrong_text = "invlaid arguments -- > on|off"

cant_mute_bot_text = "You cant mute me :("

muted_user_text = "#MUTED\nspecified user is muted now\nuse /unmute if you changed your mine"

unmuted_user_text = "this user is not muted already"

def check_tfn(vari):
    if vari == True:
        return "on"
    else:
        return "off"