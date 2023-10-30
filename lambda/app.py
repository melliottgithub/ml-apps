# import json
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# nltk.download('stopwords')
# ps = PorterStemmer()

# def parse(ps, params):
#     text = params['text']
#     text = text.lower()
#     text = re.sub(r'[^a-zA-Z]', ' ', text)
#     text = text.split() ## add tokenizer from nltk library
#     stop_words = set(stopwords.words('english'))
#     tokens = [ps.stem(word) for word in text if word not in stop_words]
#     return ' '.join(tokens)

# def lambda_handler(event, context):    
#     params = event.get('body')

#     try:
#         if type(params) == str:
#             params = json.loads(event.get('body'))

#         parsed_text = parse(ps, params)
#         response = {'parsed_text': parsed_text}
#         return {
#             'headers': {
#                 'Access-Control-Allow-Origin': '*'
#                 },
#             'statusCode': 200,
#             'body': json.dumps(response)
#         }
#     except Exception as ex:
#         return {
#             'headers': {
#                 'Access-Control-Allow-Origin': '*'
#                 },
#             'statusCode': 500,
#             'body': f'Internal error: {str(ex)}'
#         }

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

def text_parse_nltk(text, lemmatize=False, keep_numbers=False):
    text = re.sub(r'[^a-zA-Z\s]' if not keep_numbers else r'[^a-zA-Z0-9\s]', '', text.lower())
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    processor = WordNetLemmatizer() if lemmatize else PorterStemmer()

    result_tokens = [processor.lemmatize(word) if lemmatize else processor.stem(word) for word in words if word not in stop_words]
    
    return ' '.join(result_tokens)

def lambda_handler(event, context):
    try:
        input_text = event.get('text')
        processed_text = text_parse_nltk(input_text, lemmatize=True, keep_numbers=False)
        response = {'parsed_text': processed_text}
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': f'Internal error: {str(ex)}'
        }
