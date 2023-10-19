import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
ps = PorterStemmer()

def lambda_handler(event, context):
    try:
        text = event['text']
        text = text.lower()
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        text = text.split()
        stop_words = set(stopwords.words('english'))
        tokens = [ps.stem(word) for word in text if word not in stop_words]
        parsed_text = ' '.join(tokens)
        
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
