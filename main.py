import os
import modules.editor as utils
import modules.textToSpeech as ts
from pydub import AudioSegment


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    video_filename = 'data/af9d43e6-55fa-4a30-992a-509d155e6866-mp4_720p.mp4'
    video_without_audio = utils.split_video(video_filename)

    fichier_srt = "data/200390-en.srt"
    fichier_audio = "output/new_audio.mp3"

    lines = ts.lire_fichier_srt(fichier_srt)
    segments = ts.extraire_segments_sous_titres(lines)

    audio_final = AudioSegment.silent(duration=0)  # Crée un audio vide au début

    for segment in segments:
        segment_audio = ts.convertir_segment_en_audio(segment)
        audio_final += segment_audio

    audio_final.export(fichier_audio, format="mp3")

    print(f"Conversion terminée. Le fichier audio a été enregistré sous '{fichier_audio}'")

    utils.merge_audio_and_video(video_without_audio, fichier_audio)