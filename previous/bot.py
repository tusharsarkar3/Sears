# import telegram
# from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackQueryHandler,  MessageHandler, Filters, ConversationHandler
# from menu import *
# from api import *
# import os
#
#
# my_token = "1169146915:AAHrdcuC8N_M8fV2QvSfVi0tkP5cFjSqavA"
#
#
# def start(update,context):
#     update.message.reply_text("Select the type of news or type the keyword :",
#                             reply_markup=main_menu_opt())
#
# def search_keyword(update,context):
#     key =update.message.text
#     new = search(key)
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>%s News</b>📨🔵\n'%(key)
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     update.message.reply_text("Select the type of news or type the keyword :",
#                             reply_markup=main_menu_opt())
#
# def tech(update,context):
#     new = news("technology")
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>Tech News</b>📨🔵\n'
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.callback_query.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     restore_menu(update,context)
#
# def general(update,context):
#     new = news("general")
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>Latest News</b>📨🔵\n'
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.callback_query.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     restore_menu(update,context)
#
# def entertainment(update,context):
#     new = news("entertainment")
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>Entertainment News</b>📨🔵\n'
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.callback_query.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     restore_menu(update,context)
#
# def business(update,context):
#     new = news("business")
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>Business News</b>📨🔵\n'
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.callback_query.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     restore_menu(update,context)
#
# def sports(update,context):
#     new = news("sports")
#     titles =new[0]
#     urls = new[1]
#     text ='🔵<b>Sports News</b>📨🔵\n'
#     for title,url in zip(titles,urls):
#         text += "🔘%s<a href='%s'>(Read more at :-%s)</a>\n"%(title.rpartition(" - ")[0],url,title.rpartition(" - ")[-1])
#     update.callback_query.message.reply_text(text=text,parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)
#     restore_menu(update,context)
#
#
# # my_token = "1169146915:AAHrdcuC8N_M8fV2QvSfVi0tkP5cFjSqavA"
#
# PORT = int(os.environ.get('PORT', '5000'))
# bot = telegram.Bot(token = my_token)
# bot.setWebhook("https://tlnews.herokuapp.com/" + my_token)
#
#
# def main():
#     updater = Updater(my_token, use_context=True)
#     dp = updater.dispatcher
#
#     # on different commands - answer in Telegram
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CallbackQueryHandler(general,pattern='general'))
#     dp.add_handler(CallbackQueryHandler(category,pattern='category'))
#     dp.add_handler(CallbackQueryHandler(main_menu,pattern='main_menu'))
#     dp.add_handler(CallbackQueryHandler(tech,pattern='tech'))
#     dp.add_handler(CallbackQueryHandler(business,pattern='business'))
#     dp.add_handler(CallbackQueryHandler(entertainment,pattern='entertainment'))
#     dp.add_handler(CallbackQueryHandler(sports,pattern='sports'))
#     dp.add_handler(MessageHandler(Filters.text, search_keyword))
#
#
#     updater.start_webhook(listen="0.0.0.0",
#                        port=PORT,
#                        url_path="1169146915:AAHrdcuC8N_M8fV2QvSfVi0tkP5cFjSqavA")
#     updater.bot.setWebhook("https://tlnews.herokuapp.com/" + "1169146915:AAHrdcuC8N_M8fV2QvSfVi0tkP5cFjSqavA")
#
#     # updater.start_polling()
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()
