#!/usr/bin/env python3
"""
Emotion Detection Web Server
This module provides a Flask-based web server that offers emotion detection
capabilities through a REST API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: A configured Flask application instance.
    """
    app = Flask("Emotion Detector")
    @app.route("/")
    def render_index():
        """Render the main index page."""
        return render_template("index.html")
    @app.route("/emotionDetector")
    def detect_emotion():
        """
        Analyze the emotion in provided text.
        
        Returns:
            str: A formatted string with emotion analysis results or an error message.
        """
        # Retrieve the text to analyze from the request arguments
        text_to_analyze = request.args.get('textToAnalyze')
        # Pass the text to the emotion_detector function and store the response
        response = emotion_detector(text_to_analyze)
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
        result = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is **{dominant_emotion}**."
        )
        return result
    return app


if __name__ == "__main__":
    APP = create_app()
    APP.run(host="0.0.0.0", port=5000)
