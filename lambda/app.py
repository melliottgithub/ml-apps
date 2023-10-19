import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
ps = PorterStemmer()

def parse(ps, params):
    text = params['text']
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.split() ## add tokenizer from nltk library
    stop_words = set(stopwords.words('english'))
    tokens = [ps.stem(word) for word in text if word not in stop_words]
    return ' '.join(tokens)

def lambda_handler(event, context):    
    params = event.get('body')

    try:
        if type(params) == str:
            params = json.loads(event.get('body'))

        parsed_text = parse(ps, params)
        response = {'parsed_text': parsed_text}
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': f'Internal error: {str(ex)}'
        }
