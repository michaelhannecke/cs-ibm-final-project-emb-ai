from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    print(response)
    
    # Check if dominant_emotion is None (indicating an error or blank entry)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Extract the emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Format the response as requested
    result = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is **{dominant_emotion}**."
    
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)