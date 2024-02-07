import json
import os

from googleapiclient.discovery import build


# os.environ["API_KEY"] = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"


class Channel:
    api_key = str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """
        Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return build('youtube', 'v3', developerKey=Channel.api_key)

    def to_json(self, file_name):
        """
        Сохраняет в Json файл значения атрибутов экземпляра - информацию о канале
        """
        data = {'channel_id': self.channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber_count': self.subscriber_count,
                'video_count': self.video_count,
                'view_count': self.view_count
                }
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

    @property
    def channel_id(self):
        return self.__channel_id

    def __str__(self):
        """
        __str__
        """
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        +
        """
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """
        -
        """
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """
        >
        """
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """
        >=
        """
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        """
        <
        """
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """
        <=
        """
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале.
        """
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value

# if __name__ == "__main__":
#     api_key = "AIzaSyBwgpmMH0dA4JQSAvcf0Li8pxKvlM4oA5g"
#     channel = Channel(channel_id)
#     channel.print_info()
