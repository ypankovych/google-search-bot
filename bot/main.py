import os
import telebot

link = 'https://google.gik-team.com/?q={}'
bot = telebot.TeleBot(os.environ.get('token'))


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def handle(query):
    response = telebot.types.InlineQueryResultArticle(
        id='1', title='Давай я поищу за тебя в Google',
        description=link.format(query.query),
        input_message_content=telebot.types.InputTextMessageContent(
            message_text=link.format(query.query.replace(' ', '+')))
    )
    bot.answer_inline_query(query.id, [response])


if __name__ == '__main__':
    bot.polling()
