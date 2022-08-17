# (c) @PredatorHackerzZ
# I just made this for searching a channel message from inline.
# Maybe you can use this for something else.
# I first made this for @TGBotListBot ...
# Edit according to your use.
import asyncio
from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from TeamTeleRoid.forcesub import ForceSub

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@Bot.on_message(filters.private & filters.command("start"))

async def start_handler(_, event: Message):

    await event.reply_photo(

        photo="https://te.legra.ph/file/965fdc73a8bee02b968a3.jpg",

        caption=Config.START_MSG.format(event.from_user.mention),

        reply_markup=InlineKeyboardMarkup([

	    [InlineKeyboardButton("➕ Add Me In Your Groups ➕", url="http://t.me/DTG_SIMPLE_BOT?startgroup=true")],            [InlineKeyboardButton("Our Channel", url="https://t.me/DTG_TV"),

             InlineKeyboardButton("Our Movie Group", url="https://t.me/Movie_Search_bot_hindi")],

	    [InlineKeyboardButton("Support Group", url="https://t.me/DTG_SUPPORT")],

            [InlineKeyboardButton("Help", callback_data="Help_msg"),

             InlineKeyboardButton("About", callback_data="About_msg")]

            ])

    )

@Bot.on_message(filters.private & filters.command("help"))

async def help_handler(_, event: Message):

    await event.reply_photo(

        photo="https://te.legra.ph/file/965fdc73a8bee02b968a3.jpg",

        caption=Config.ABOUT_HELP_TEXT.format(event.from_user.mention),

        reply_markup=InlineKeyboardMarkup([

	    [InlineKeyboardButton("➕ Add Me In Your Groups ➕", url="http://t.me/DTG_SIMPLE_BOT?startgroup=true")],

            [InlineKeyboardButton("Our Channel", url="https://t.me/DTG_TV"),

             InlineKeyboardButton("Our Movie Group", url="https://t.me/Movie_Search_bot_hindi")],

	    [InlineKeyboardButton("Support Group", url="https://t.me/DTG_SUPPORT")],	

            [InlineKeyboardButton("About", callback_data="About_msg")]

            ])

    )

@Bot.on_message(filters.incoming)

async def inline_handlers(_, event: Message):

    if event.text == '/start':

        return

    answers = f'**     🗃️ 𝐑𝐞𝐬𝐮𝐥𝐭𝐬 𝐅𝐨𝐫\n      ┬┴┬┴┤ {event.text} ├┬┴┬┴ \n\n───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n───█▒▒░░░░░░░░░▒▒█───\n────█░░█░░░░░█░░█────\n─▄▄──█░░░▀█▀░░░█──▄▄─\n█░░█─▀▄░░░░░░░▄▀─█░░█\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n     🄲🄷🄴🄲🄺 🅂🄿🄴🄻🄻🄸🄽🄶\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰\n\n**'

    async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):

        if message.text:

            thumb = None

            f_text = message.text

            msg_text = message.text.html

            if "|||" in message.text:

                f_text = message.text.split("|||", 1)[0]

                msg_text = message.text.html.split("|||", 1)[0]

            answers += f'**🎬 Title ➠ ' + '' + f_text.split("\n", 1)[0] + '' + '\n\n📜 About ➠ ' + '' + f_text.split("\n", 2)[-1] + ' \n\n**'

    try:

        a=await event.reply_text(answers) 
        await asyncio.sleep(10)
        await a.delete()
	
        print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
    except QueryIdInvalid:
	
	
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")
        await asyncio.sleep(10)
        await a.delete()

@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("Our Channel", url="https://t.me/DTG_TV"),
						InlineKeyboardButton("Support Group", url="https://t.me/DTG_SUPPORT")
					],
					[
						InlineKeyboardButton("Developer", url="https://t.me/DTG_"),
						InlineKeyboardButton("Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
          elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("About", callback_data="About_msg"),
						InlineKeyboardButton("Our Channel", url="https://t.me/DTG_TV")
					], 
                                        [
						InlineKeyboardButton("Owner", url="https://t.me/DTG_Admin_bot"),
						InlineKeyboardButton("Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup([
	                            [InlineKeyboardButton("➕ Add Me In Your Groups ➕", url="http://t.me/DTG_SIMPLE_BOT?startgroup=true")],
                                    [InlineKeyboardButton("Our Channel", url="https://t.me/DTG_TV"),
                                     InlineKeyboardButton("Our Movie Group", url="https://t.me/Movie_Search_bot_hindi")],
	                            [InlineKeyboardButton("Support Group", url="https://t.me/DTG_SUPPORT")],
                                    [InlineKeyboardButton("Help", callback_data="Help_msg"),
                                     InlineKeyboardButton("About", callback_data="About_msg")]
                                    ]  
		       ),
                       parse_mode="html"
		)

       
# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
