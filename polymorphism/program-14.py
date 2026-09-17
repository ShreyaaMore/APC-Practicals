# 14.	Create a base class Media with a method play(). Derive Audio, Video, and Podcast. Override play() according to the media type.

class Media:
    def __init__(self, title, duration_minutes):
        self.title = title
        self.duration_minutes = duration_minutes

    def play(self):
        print(f"Playing generic media: {self.title}")


class Audio(Media):
    def __init__(self, title, duration_minutes, bitrate_kbps):
        super().__init__(title, duration_minutes)
        self.bitrate_kbps = bitrate_kbps

    def play(self):
        print(f"[AUDIO] Streaming '{self.title}' (MP3 @ {self.bitrate_kbps} kbps) | Duration: {self.duration_minutes} mins")


class Video(Media):
    def __init__(self, title, duration_minutes, resolution):
        super().__init__(title, duration_minutes)
        self.resolution = resolution

    def play(self):
        print(f"[VIDEO] Playing '{self.title}' in {self.resolution} HD video stream | Duration: {self.duration_minutes} mins")


class Podcast(Media):
    def __init__(self, title, duration_minutes, host, episode_no):
        super().__init__(title, duration_minutes)
        self.host = host
        self.episode_no = episode_no

    def play(self):
        print(f"[PODCAST] Episode #{self.episode_no}: '{self.title}' hosted by {self.host} | Duration: {self.duration_minutes} mins")


media_library = [
    Audio("Clair de Lune", 5.2, 320),
    Video("Inception (Scene 4)", 12.0, "4K UHD"),
    Podcast("AI Revolution Ep. 42", 45.0, "Lex Fridman", 42)
]

print("Media Playback (Polymorphism)")
for item in media_library:
    item.play()
