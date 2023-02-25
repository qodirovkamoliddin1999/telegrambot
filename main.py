
from telegram.ext import Updater,CommandHandler,ConversationHandler,MessageHandler,Filters,filters
from moviepy.editor import * 



def mp44():
    mp4 = r"video.mp4"
    mp3 = r"audio.mp3"
    video = VideoFileClip(mp4)
    audio = video.audio
    audio.write_audiofile(mp3)

    audio.close()
    video.close()



TOKEN = '6177053222:AAGZItEqT3gywNu9koC0YBetHIJYs7AZqs4'

def start(update, context):
    update.message.reply_text('Video yuboring')
    return 1

def convert(update,context):
    a = update.message.reply_text('Video audioga ogirilmoqda...')
    chat_id = update.message.chat_id
    video_id= update.message.video.file_id
    video = context.bot.get_file(video_id)
    video.download('video.mp4')
    mp44()
    # update.message.reply_text(video['file_path'])
    context.bot.deleteMessage(message_id=a.message_id, chat_id=update.message.chat_id)
    context.bot.send_document(chat_id, open('audio.mp3','rb'))
    return 1
    





def main():
    updater = Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            1:[
                MessageHandler(filters.Filters.video, convert)
            ]
        },
        fallbacks=[CommandHandler('start',start)]
    )
    disp.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()

main()



