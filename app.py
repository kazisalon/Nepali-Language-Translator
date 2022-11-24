import streamlit as st
import numpy as np
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator


# setting up the api key configuration

api_key = 'GUBGMHVpwcTsPFvNNVdG5DKtpv6UwksAfzw5aULcGzgG'
url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/209d939b-59cb-4001-a707-013244cee735'

authenticator = IAMAuthenticator(apikey=api_key)

langtranslator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)

langtranslator.set_service_url(url)

st.title("Nepali Language Translator")

# setting up the dropdown list of the languages

option = st.selectbox(
    'Which language would you choose to type', 
    ('English', 'Nepali'))

option1 = st.selectbox('Which language would you like to translate to',
                       ('English', 'Nepali'))


sent = "Enter the text in "+option+" language in the text-area provided below"

# setting up the dictionary of languages to their keywords

language = {"hello":" hi"}

language_lib = {'English': 'en', 'Nepali' : 'ne'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select  Language for Translation")

        else:

            translate_code = language_lib[option]+'-'+language_lib[option1]

            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write("Please do cross check if text-area is filled with sentences or not")
