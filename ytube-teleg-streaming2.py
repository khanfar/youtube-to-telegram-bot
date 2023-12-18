import requests
from telegram import Bot, ParseMode

def get_live_video_id(channel_id, api_key):
    url = f'https://www.googleapis.com/youtube/v3/search?part=id&channelId={channel_id}&type=video&eventType=live&key={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data and data['items']:
        live_video_id = data['items'][0]['id']['videoId']
        return live_video_id
    
    return None

def send_to_telegram(token, chat_id, message):
    bot = Bot(token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)

def main():
    channel_id = 'UCfiwzLy-8yKzIbsmZTzxDgw'
    youtube_api_key = 'AIxxSyxxx9hXWSnxxxSdz-UsI2xxxxVU'  # Replace with your actual YouTube Data API key
    telegram_bot_token = '65337xx42:AAF75xxPI-nETIGoEzxxxe9Pr0M'
    telegram_channel_username = '@mxxktxst'

    print('Checking for live stream...')
    live_video_id = get_live_video_id(channel_id, youtube_api_key)

    if live_video_id:
        live_stream_url = f'https://www.youtube.com/watch?v={live_video_id}'
        message = f'Live Stream URL: [Watch Now]({live_stream_url})'
        print(message)
        send_to_telegram(telegram_bot_token, telegram_channel_username, message)
    else:
        print('No live stream currently.')
        send_to_telegram(telegram_bot_token, telegram_channel_username, 'No live stream currently.')

if __name__ == '__main__':
    main()
