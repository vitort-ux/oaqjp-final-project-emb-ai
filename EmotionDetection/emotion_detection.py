import requests
import json

def emotion_detector(text_to_analyse): 
    # URL of the sentiment analysis service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format 
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API 
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    if response.status_code == 400: 
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        max_emotion = None
    else:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions, key=emotions.get)
        max_value = emotions[max_emotion]

    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': max_emotion
            }


if __name__ == '__main__':
    resposta = emotion_detector("I love this new technology.")
    print(resposta)