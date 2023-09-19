import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

ibm_apikey = 'dws3Ebwn7TPeMCicQb9q80PAHa0tOHFrIbi1MF4KfT4-'
ibm_speech_to_text_url = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/a27d7642-a11c-4a6d-8c6a-e76d0228127e'
authentificator = IAMAuthenticator(f'{ibm_apikey}')
speech_to_text = SpeechToTextV1(authenticator=authentificator)

speech_to_text.set_service_url(f'{ibm_speech_to_text_url}')
#speech_to_text.set_disable_ssl_verification(True)


speech_model = speech_to_text.get_model('en-US_BroadbandModel')

with open(join(dirname(__file__), '../output/', 'audio_of_video.mp3'), 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        word_alternatives_threshold=0.9
    ).get_result()

    print(json.dumps(speech_recognition_results, indent=4))