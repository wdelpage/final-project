"""
EmotionDetection Package

A Python package for detecting emotions in text using Watson NLP services.
"""

from .emotion_detection import emotion_detector

__version__ = "1.0.0"
__author__ = "Wasana Delpage"
__email__ = "delpagel@gmail.com"

# Make the emotion_detector function available at package level
__all__ = ["emotion_detector"]