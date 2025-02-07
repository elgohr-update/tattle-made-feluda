from .installer import install_packages
import os

"""
This operator uses google cloud API to extract text from an image.
the credentials to use the cloud vision API should be present in a file titled credentials.json
in the root folder. if it isn't present, it can be optionally fetched from an aws s3 bucket.
The AWS credentials to do this need to be set in the environment variables : AWS_ACCESS_KEY_ID, 
AWS_SECRET_ACCESS_KEY_ID, AWS_BUCKET, S3_CREDENTIALS_PATH

pip install :
google-cloud==0.34.0
google-cloud-vision==0.34.0
boto3
"""
# requirement_list = ["translate==3.6.1", "spacy==3.2.1"]
requirement_list = ["googletrans==4.0.0rc1", "spacy==3.2.1"]


def initialize(param):
    install_packages(requirement_list)
    os.system(
        "pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.2.0/en_core_web_md-3.2.0.tar.gz"
    )

    global translator, spacy, NER

    from googletrans import Translator

    translator = Translator()
    import spacy

    NER = spacy.load("en_core_web_md")


def run(text):
    translated = translator.translate(text)
    print("---->", translated.text)
    entity_tuple = NER(translated.text)
    entities = []
    for word in entity_tuple.ents:
        entities.append(word.text)

    return entities


def cleanup(param):
    pass


def state():
    return {
        "label": "Named Entity Extraction from Text in non english language",
    }
