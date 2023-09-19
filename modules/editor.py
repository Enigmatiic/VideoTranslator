import sys

import moviepy.editor
from moviepy.editor import *


def split_video(video_file):
    with VideoFileClip(video_file) as video:
        audio = video.audio
        video_without_audio = video.without_audio()
        # audio.write_audiofile('output/audio_of_video.mp3') pour extraire l'audio
        video.write_videofile(filename='output/video_without_audio.mp4', audio=False)

        return 'output/video_without_audio.mp4'


def merge_audio_and_video(video_without_audio, new_audio):
    with VideoFileClip(video_without_audio) as video:
        with AudioFileClip(new_audio) as audio:
            video = video.set_audio(audio)
            video.write_videofile('output/video_with_new_audio.mp4')
