import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Список треков в MP3
        self.playlist = [
            os.path.join(self.base_path, "music/justin_bieber_beauty_and_a_beat.mp3"),
            os.path.join(self.base_path, "music/kendrick_lamar_not_like_us.mp3"),
            os.path.join(self.base_path, "music/central_cee_sprinter.mp3"),
            os.path.join(self.base_path, "music/maroon5_payphone.mp3"),
            os.path.join(self.base_path, "music/taylor_swift_cruel_summer.mp3")
        ]
        
        self.covers = {
            0: os.path.join(self.base_path, "images/covers/justin_bieber.png"),
            1: os.path.join(self.base_path, "images/covers/kendrick_lamar.png"),
            2: os.path.join(self.base_path, "images/covers/central_cee.png"),
            3: os.path.join(self.base_path, "images/covers/maroon5.png"),
            4: os.path.join(self.base_path, "images/covers/taylor_swift.png")
        }
        self.current_index = 0

    def play(self):
        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
        except:
            print("Ошибка: Убедись, что файлы переименованы в .mp3")

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_cover(self):
        path = self.covers[self.current_index]
        return pygame.image.load(path).convert() if os.path.exists(path) else pygame.Surface((300, 300))