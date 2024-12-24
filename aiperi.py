import telebot
import random

bot = telebot.TeleBot("7039401090:AAGvZBNBENCkqRMVY6etUgvxcQJx1GMc47c")

@bot.message_handler(commands=['start'])
def start(message):
    mess = f"HI, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == "salam":
        bot.send_message(message.chat.id, "Sagada salam")
    elif message.text.lower() == "foto":
        photo_paths = [
            "media/foto/foto+logo.jpg",
            "media/foto/алма.jpeg",
            "media/foto/термос.jpeg",
            "media/foto/ананас.jpeg",
            "media/foto/алмурут.jpeg"
        ]
        photo_path = random.choice(photo_paths)
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == "video":
        video_paths = [
            "norodnuq/video/video1/mp4"
        ]
        video_path = random.choice(video_paths)
        try:
            with open(video_path, 'rb') as video:
                bot.send_video(message.chat.id, video)
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при отправке видео: {e}")
    elif message.text.lower() == "music":
        audio_paths = []
        audio_path = random.choice(audio_paths)
        try:
            with open(audio_path, 'rb') as audio:
                bot.send_audio(message.chat.id, audio)
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при отправке музыки: {e}")
    else:
        bot.send_message(message.chat.id, "jakshna jaz")

bot.polling(none_stop=True)
