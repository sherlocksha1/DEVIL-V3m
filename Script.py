class script(object):
    START_TXT = """đ·đŽđ»đŸ đ€{},
đŒđą đđđđ , <a href='https://t.me/Ramananshav3_bot'>đđšđĄđ§ đđźđ«đđąđ«đđŁ</a>, đžđ'đ đđđđą đđđđą đđđđ đđđ đđ đđ đąđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đž'đđ đđđđđđđ đđđđđđ đđđđđ đż
"""
    HELP_TXT = """đ·đŽđ {}
đđŠđłđŠ đđŽ đđ©đŠ đđŠđ­đ± đđ°đł đđș đđ°đźđźđąđŻđ„đŽ."""
    ABOUT_TXT = """
   đđđąđšđ§ đ đŠđ
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ° đđšđĄđ§ đđźđ«đđąđ«đđŁ â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đŒđ đœđ°đŒđŽ - <a href="https://t.me/Ramananshav3_bot"> RAMANAN </a>
ââŁâȘŒ đČđđŽđ°đđŸđ- <a href="https://t.me/peter_parker_10"> đčđ đ€đ€ </a>
ââŁâȘŒ đ»đžđ±đđ°đđ - đżđđđŸđ¶đđ°đŒ
ââŁâȘŒ đ»đ°đœđ¶đđ°đ¶đŽ - đżđđđ·đŸđœ đč
ââŁâȘŒ đłđ°đđ°đ±đ°đđŽ - đŒđŸđœđ¶đŸ đłđ±
ââŁâȘŒ đđŽđđđŽđ -  đ·đŽđđŸđșđ
ââŁâȘŒ đ±đđžđ»đ đđđ°đđ - v1.0.2 [ đ±đŽđđ° ]
ââ°ââââââââââââââââŁ âââââââââââââââââââââ±âÛȘÛȘ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ŐOááááŽ áOáȘáŽ - <a href="https://t.me/albintko"> đđđđđ đđđ„đ </a>

đČđđŽđ°đđŸđ:
<a href="https://t.me/albintko"> đ°đ»đ±đžđœ  </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

âą/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
âą /alive - check me alive or deadđ€§
Just for a rasamđ"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
âĄïž /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

âĄïž <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>COMMAND /stickerid\nđšđż đžđđ đ­đŸđŸđœ đłđŸđđŸđđđșđ đČđđđŒđđŸđ đšđœ đąđđđŒđ /stickerid đłđ đŠđŸđ đČđđđŒđđŸđ đšđœ (đ±đŸđđđ đ¶đđđ đČđđđŒđđŸđ)</b>"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

đïž Command

âą /song or /mp3 (songname) - download song from yt servers.
âą /video or /mp4 (songname) - download video from yt servers

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

â /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>đČ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đźđđ: 
đŁ. /dice - Roll The Dice 
đ€. /Throw đđ /Dart - đłđ đŹđșđđŸ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âą /filter - add a filter in chat.
âą /filters - list all the filters of a chat.
âą /del - delete a specific filter in chat.
âą /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âą /connect  - connect a particular chat to your PM.
âą /disconnect  - disconnect from a chat.
âą /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
âą /paste [text] - paste the given text on Pasty
âą /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
âą /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
âą /id - get id of a specifed user.
âą /info  - get information about a user.
âą /json - get the json details of a message.

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
âą /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on both pm and group.
âą IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
âą /imdb  - get the film information from IMDb source.
âą /search  - get the film information from various sources.

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą More search tools can be found on inline.
âą Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
âą /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on group.
âą These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
âą /ban - ban a user.
âą /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âą /mute - mute a user.
âą /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âą /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
âą IMDb should have admin privillage.
âą These commands works on group.
âą These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âą /logs - to get the rescent errors.
âą /stats - to get status of files in db.
âą /delete - to delete a specific file from db.
âą /users - to get list of my users and ids.
âą /chats - to get list of the my chats and ids.
âą /leave - to leave from a chat.
âą /disable - do disable a chat.
âą /ban_users - to ban a user.
âą /unban_users - to unban a user.
âą /channel - to get list of total connected channels.
âą /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**âŠïž READ THIS INSTRUCTION âŠïž**

__đŁ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately đ__

**đ JOIN THIS CHANNEL & TRY AGAIN đ**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
âą /inkick - command with required arguments and i will kick members from group.
âą /instatus - to check current status of chat member from group.
âą /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âą /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âą /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """âYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âïž Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """đź Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """âI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """âïž Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
