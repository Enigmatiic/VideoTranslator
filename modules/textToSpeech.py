from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import tempfile
from pydub import AudioSegment
import modules.translate as trans
import re
from os.path import dirname, join
from os import makedirs, remove

# Remplacez les valeurs suivantes par vos propres informations d'identification
api_key = 'morGpG-e7k2l-3myMuZ71uasUoVeaSFAIa1ks5B6Cjeq'
service_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/e813c912-577c-4036-9f65-b3f2a65725aa'

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(service_url)


# Lire le fichier SRT
def lire_fichier_srt(fichier_srt):
    with open(fichier_srt, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


# Extraire les segments de texte et leurs timecodes d'un fichier SRT
def extraire_segments_sous_titres(lines):
    segments = []
    segment = {"timecode": None, "text": []}
    for line in lines:
        line = line.strip()
        if re.match(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+', line):
            if segment["timecode"] is not None:
                segments.append(segment)
            segment = {"timecode": line, "text": []}
        elif line != '' and not line.isnumeric() and re.match(r'.*', line):
            translate_text = trans.translateText(line)
            segment["text"].append(translate_text)
    if segment["timecode"] is not None:
        segments.append(segment)
    return segments


# Convertir un segment de texte en audio avec Watson TTS
# Convertir un segment de texte en audio avec Watson TTS
def convertir_segment_en_audio(segment):
    texte = ' '.join(segment["text"])
    response = text_to_speech.synthesize(
        texte,
        accept='audio/mp3',
        voice='fr-FR_ReneeV3Voice'
    ).get_result()

    # Créez un dossier temporaire si nécessaire
    dossier_temporaire = 'C:/Users/tondo/PycharmProjects/VideoTranslator/modules/tmp'
    makedirs(dossier_temporaire, exist_ok=True)

    # Générez un nom de fichier temporaire unique
    nom_fichier_temporaire = join(dossier_temporaire, next(tempfile._get_candidate_names()) + ".mp3").replace('\\', '/')

    # Enregistrez la réponse dans le fichier audio temporaire
    with open(nom_fichier_temporaire, 'wb') as temp_audio_file:
        temp_audio_file.write(response.content)

    with open(nom_fichier_temporaire, 'rb') as audio_file:
        # Chargez le fichier audio temporaire avec pydub
        audio = AudioSegment.from_file(audio_file, format='mp3')

        # Supprimez le fichier audio temporaire
        remove(nom_fichier_temporaire)

        return audio
