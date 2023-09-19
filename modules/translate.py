import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Remplacez les valeurs suivantes par vos propres informations d'identification
api_key = 'gjz2q7FH2w7h4hipScPp_Bng7R0a0DOTfexwuO83WKS_'
service_url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/39c50e76-508f-4371-b2f7-a2c49e489885'

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(service_url)

def translateText(original_text):
    translation = language_translator.translate(
        text=original_text,
        model_id='en-fr'
    ).get_result()

    return translation['translations'][0]['translation']