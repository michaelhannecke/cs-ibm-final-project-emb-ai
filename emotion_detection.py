import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=input_data, headers=headers)
    
    # Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Create result dictionary with emotion scores
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Find the dominant emotion (emotion with highest score)
    dominant_emotion = max(result, key=result.get)
    
    # Add dominant emotion to the result dictionary
    result['dominant_emotion'] = dominant_emotion
    
    return result