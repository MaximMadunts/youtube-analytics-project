from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_data = self.get_video_data()

        self.title = self.video_data["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.view_count = int(self.video_data["items"][0]["statistics"]["viewCount"])
        self.like_count = int(self.video_data["items"][0]["statistics"]["likeCount"])

    def get_video_data(self):
        youtube = build('youtube', 'v3')
        request = youtube.videos().list(
            part="snippet,statistics",
            id=self.video_id
        )
        return request.execute()

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{super().__str__()} - Playlist: {self.playlist_id}"
