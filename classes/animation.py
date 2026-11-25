import pygame
from pathlib import Path

class AnimationTrack:

    def __init__(self, file_path : str, sprite_width = None, sprite_height = None, frame_beats = 10, loop = True, reverse = False):
        self.frames = []
        self.beat_count = 0
        self.track_add = 1
        self.spritesheet = pygame.image.load(file_path)

        if not (sprite_width and sprite_height):  # se nenhum valor for informado, é assumido que os sprites são quadrados
            self.sprite_height = self.spritesheet.get_height()
            self.sprite_width = self.sprite_height
        else:
            self.sprite_height = sprite_height
            self.sprite_width = sprite_width

        self.reversed = reverse
        self.loop = loop
        self.frame_beats = frame_beats
        self.total_frames = self.spritesheet.get_width() // self.sprite_width  # o programa detecta automaticamente a quantidade de frames

        for frame in range(0, self.total_frames):
            subframe = pygame.Rect(frame * self.sprite_width, 0, self.sprite_width, self.sprite_height)
            self.frames.append(self.spritesheet.subsurface(subframe))

    def beat(self):  # atualiza o frame
        if self.reversed:
            self.track_add = -1
        else:
            self.track_add = 1

        if self.loop:  # se loop tiver ativado, a animação retorna ao inicio ou fim
            self.beat_count = (self.beat_count + self.track_add) % (self.frame_beats * self.total_frames)
        else:  # senão, a animação vai até uma das extremidades e para
            self.beat_count = max(0, min(self.beat_count + self.track_add, (self.frame_beats * self.total_frames) - 1))

    def get_frame(self):  # pega o frame atual
        return self.frames[self.beat_count//self.frame_beats]

    def beat_and_get(self):  # atualiza e retorna o frame
        frame = self.get_frame()
        self.beat()
        return frame

    def reset(self):  # retorna à uma das extremidades
        if self.reversed:
            self.beat_count = (self.frame_beats * self.total_frames) - 1
        else:
            self.beat_count = 0


class AnimationGroup:

    def __init__(self, sprite_width = None, sprite_height = None):
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.current_track = None
        self.animation_dict = {}

    def add_animation(self, file_path : str, name = "", frame_beats = 10, loop = True, reverse = False):
        new_track = AnimationTrack(file_path, self.sprite_width, self.sprite_height, frame_beats, loop, reverse)

        if not(self.sprite_width or self.sprite_height):  # pega automaticamente esse dois valores
            self.sprite_width = new_track.sprite_width
            self.sprite_height = new_track.sprite_height

        if name == "":  # se o nome não for informado, pega o nome do file_path
            self.animation_dict[Path(file_path).stem] = new_track
        else:
            self.animation_dict[name] = new_track

    def add_folder(self, folder_path : str, name_add = ""):  # adiciona uma pasta inteira de sprites
        folder = Path(folder_path)
        path_data = [[file.stem, str(file)] for file in list(folder.iterdir())]
        for name, path in path_data:  # o nome dos AnimationTracks vão ser os nomes dos arquivos de sprite
            self.add_animation(path, name + name_add)

    def reset_all(self):
        for name in self.animation_dict.keys():
            self.animation_dict[name].reset()

    def beat(self, name : str):
        return self.animation_dict[name].beat_and_get()

    def roll(self, name : str):  # pede um AnimationTrack, se não for o atual, reinicia todos e roda o requerido
        if name != self.current_track:
            self.current_track = name
            self.reset_all()
        return self.animation_dict[name].beat_and_get()