import os
import datetime
from googleapiclient.discovery import build

from src.video import Video


def parse_duration(duration_str: str) -> datetime.timedelta:
    time_elements = duration_str.split("T")[1].split(":")
    hours = int(time_elements[0]) if len(time_elements) > 1 else 0
    minutes = int(time_elements[-2])
    seconds = int(time_elements[-1][:-1])
    duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return duration


def get_video_duration(video: Video) -> datetime.timedelta:
    duration_str = video.video_data["items"][0]["contentDetails"]["duration"]
    duration = parse_duration(duration_str)
    return duration


class PlayList:
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.playlist_data = self.get_playlist_data()
        self.title = self.playlist_data["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        self.videos = self.get_videos()

    def get_playlist_data(self):
        api_key = os.getenv("API_KEY")
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.playlists().list(
            part="snippet",
            id=self.playlist_id
        ).execute()
        return request

    def get_videos(self):
        api_key = os.getenv("API_KEY")
        youtube = build("youtube", "v3", developerKey=api_key)
        videos_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=self.playlist_id,
            maxResults=50
        ).execute()

        video_ids = [item["contentDetails"]["videoId"] for item in videos_request["items"]]
        videos = [Video(video_id) for video_id in video_ids]

        return videos

    @property
    def total_duration(self) -> datetime.timedelta:
        total_duration = sum([get_video_duration(video) for video in self.videos], datetime.timedelta())
        return total_duration

    def show_best_video(self) -> str:
        best_video = max(self.videos, key=lambda video: video.like_count)
        return best_video.video_url
