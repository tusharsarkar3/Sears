from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu(update,context):
    query = update.callback_query
    context.bot.edit_message_text( chat_id=query.message.chat_id,message_id=query.message.message_id,text="Select the type of news or type the keyword :", reply_markup=main_menu_opt())

def category(update,context):
    query = update.callback_query
    context.bot.edit_message_text( chat_id=query.message.chat_id,message_id=query.message.message_id,text="Select the catergory : ", reply_markup=category_menu())
    

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def main_menu_opt():
    button_list = [
    InlineKeyboardButton("General", callback_data="general"),
    InlineKeyboardButton("Category", callback_data="category"),
    # InlineKeyboardButton("Keyword based news", callback_data="keyword")
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

def category_menu():
    button_list = [
    InlineKeyboardButton("Technology", callback_data="tech"),
    InlineKeyboardButton("Business", callback_data="business"),
    InlineKeyboardButton("Entertainment", callback_data="entertainment"),
    InlineKeyboardButton("Sports", callback_data="sports"),
    InlineKeyboardButton("Back to main menu", callback_data="main_menu")
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
def keyword_menu():
    button_list = [
    InlineKeyboardButton("Back to main menu", callback_data="main_menu")
    ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

def restore_menu(update,context):
    update.callback_query.message.reply_text("Select the type of news or type the keyword :",
                            reply_markup=main_menu_opt())

