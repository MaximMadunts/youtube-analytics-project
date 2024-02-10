import os
from dotenv import load_dotenv
from src.channel import Channel
import googleapiclient.discovery


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.video_data = self.get_video_data()
        self.video_title = self.video_data["items"][0]["snippet"]["title"]
        self.video_description = self.video_data["items"][0]["snippet"]["description"]
        self.video_url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count = self.video_data["items"][0]["statistics"]["viewCount"]
        self.like_count = self.video_data["items"][0]["statistics"]["likeCount"]

    def get_video_data(self):
        api_key = os.getenv("API_KEY")
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
        request = youtube.videos().list(
            part="snippet,statistics",
            id=self.video_id
        ).execute()
        return request

    def __str__(self) -> str:
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
