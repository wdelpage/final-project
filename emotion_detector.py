import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the given text using Watson NLP Emotion Detection service.
    
    Args:
        text_to_analyze (str): The text to be analyzed for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and the dominant emotion in the format:
              {
                  'anger': anger_score,
                  'disgust': disgust_score, 
                  'fear': fear_score,
                  'joy': joy_score,
                  'sadness': sadness_score,
                  'dominant_emotion': '<name of the dominant emotion>'
              }
              Returns None values for all keys if an error occurs.
    """
    # URL for the Watson NLP Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API call
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Make the POST request to the Watson NLP service
        response = requests.post(url, headers=headers, json=input_json)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response using json library functions
            response_data = response.json()
            
            # Extract emotion predictions from the response
            # The structure is typically: emotionPredictions[0].emotion
            emotions_data = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
            
            # Extract the required emotions with their scores
            anger_score = emotions_data.get('anger', 0)
            disgust_score = emotions_data.get('disgust', 0)  
            fear_score = emotions_data.get('fear', 0)
            joy_score = emotions_data.get('joy', 0)
            sadness_score = emotions_data.get('sadness', 0)
            
            # Create a dictionary of emotions and their scores for finding dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # Find the dominant emotion (emotion with highest score)
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Return the formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # Handle error cases - return None values for all emotions
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    except requests.exceptions.RequestException as e:
        # Handle network/connection errors - return None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        # Handle JSON parsing or key access errors - return None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }