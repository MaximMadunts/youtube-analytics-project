import json
import os

from googleapiclient.discovery import build


# os.environ["API_KEY"] = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"


class Channel:
    api_key = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"

    def __init__(self, channel_id, api_key=None):
        self.view_count = None
        self.video_count = None
        self.subscribers_count = None
        self.link = None
        self.description = None
        self.title = None
        self.name = None
        self.url = None
        self.api_key = api_key or os.environ.get("API_KEY")
        self.channel_id = channel_id
        self.youtube = build("youtube", "v3", developerKey=self.api_key)
        self.channel_data()
        self.title = None

    def channel_data(self):
        response = self.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        ).execute()

        channel_data = response["items"][0]
        snippet = channel_data["snippet"]
        statistics = channel_data["statistics"]

        # self.title = channel_data["title"]
        self.name = snippet["title"]
        self.description = snippet["description"]
        self.link = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribers_count = int(statistics.get("subscriberCount", 0))
        self.video_count = int(statistics.get("videoCount", 0))
        self.view_count = int(statistics.get("viewCount", 0))

    @classmethod
    def get_service(cls):
        api_service_name = "youtube"
        api_version = "v3"
        return build(api_service_name, api_version, developerKey=cls.api_key)

    def to_json(self, filename):
        data = {
            "id": self.channel_id,
            "name": self.name,
            "description": self.description,
            "link": self.link,
            "subscribers_count": self.subscribers_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def print_info(self):
        print(f"ID канала: {self.channel_id}")
        print(f"Название канала: {self.name}")
        print(f"Описание канала: {self.description}")
        print(f"Ссылка на канал: {self.link}")
        print(f"Количество подписчиков: {self.subscribers_count}")
        print(f"Количество видео: {self.video_count}")
        print(f"Общее количество просмотров: {self.view_count}")

# if __name__ == "__main__":
#     api_key = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"
#     channel = Channel(channel_id)
#     channel.print_info()
