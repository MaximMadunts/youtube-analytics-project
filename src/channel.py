import json
import os
from googleapiclient.discovery import build


# os.environ["API_KEY"] = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"


class Channel:
    def __init__(self, channel_id):
        self.api_key = os.environ.get("API_KEY")
        self.channel_id = channel_id
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def print_info(self):
        request = self.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        ).execute()
        print(json.dumps(request, indent=2))


if __name__ == "__main__":
    channel_id = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"
    channel = Channel(channel_id)
    channel.print_info()
