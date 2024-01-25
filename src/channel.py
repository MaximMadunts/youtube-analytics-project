import os
from googleapiclient.discovery import build

os.environ["API_KEY"] = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"
class Channel:
    def __init__(self, channel_id):
        self.api_key = os.environ.get("YOUTUBE_API_KEY")
        self.channel_id = channel_id
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def print_info(self):
        request = self.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        )
        response = request.execute()
        channel_info = response["items"][0]

        title = channel_info["snippet"]["title"]
        subscribers = channel_info["statistics"]["subscriberCount"]
        videos = channel_info["statistics"]["videoCount"]

        print(f"Channel: {title}")
        print(f"Subscribers: {subscribers}")
        print(f"Videos: {videos}")

if __name__ == "__main__":
    channel_id = "здесь_ваш_ID_канала"
    channel = Channel(channel_id)
    channel.print_info()