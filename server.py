"""
Flask server for Emotion Detection Application

This server provides a web API for emotion detection using the EmotionDetection package.
The server runs on localhost:5000 and provides an endpoint at /emotionDetector.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
import json

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page of the application.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Emotion Detection API endpoint.
    
    This endpoint accepts a 'textToAnalyze' parameter via GET request,
    processes it using the emotion_detector function, and returns a 
    formatted response.
    
    Returns:
        str: Formatted response showing emotion scores and dominant emotion,
             or error message if invalid input is provided.
    """
    # Get the text to analyze from the request parameters
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    
    # Check if text is provided
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the result is valid (not None values)
    if result is None or result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    
    # Extract emotion scores and dominant emotion
    anger_score = result['anger']
    disgust_score = result['disgust']
    fear_score = result['fear']
    joy_score = result['joy']
    sadness_score = result['sadness']
    dominant_emotion = result['dominant_emotion']
    
    # Format the response as specified
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is **{dominant_emotion}**."
    )
    
    return response

@app.route('/emotionDetector/json')
def emotion_detector_json():
    """
    Emotion Detection API endpoint that returns JSON response.
    
    This is an additional endpoint for testing purposes that returns
    the raw JSON response from the emotion_detector function.
    
    Returns:
        str: JSON string of the emotion detection results
    """
    # Get the text to analyze from the request parameters
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    
    # Check if text is provided
    if not text_to_analyze:
        return json.dumps({"error": "Invalid text! Please try again!"})
    
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Return the JSON response
    return json.dumps(result, indent=2)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return "Page not found! Please check the URL.", 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return "Internal server error! Please try again later.", 500

if __name__ == '__main__':
    # Run the Flask application
    print("Starting Emotion Detection Server...")
    print("Server will be available at: http://localhost:5000")
    print("API endpoint: http://localhost:5000/emotionDetector?textToAnalyze=<your_text>")
    print("Press Ctrl+C to stop the server")
    
    app.run(host='localhost', port=5000, debug=True)