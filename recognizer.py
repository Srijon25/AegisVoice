# AegisVoice: recognizer.py - Core module for detecting cancel phrases

import speech_recognition as sr
from difflib import SequenceMatcher
from typing import List, Tuple

class CancelPhraseRecognizer:
    def __init__(self, cancel_phrases: List[str], confidence_threshold: float = 0.7):
        self.cancel_phrases = [phrase.lower() for phrase in cancel_phrases]
        self.confidence_threshold = confidence_threshold
        self.recognizer = sr.Recognizer()

    def listen_and_recognize(self, timeout: int = 5) -> Tuple[str, float]:
        with sr.Microphone() as source:
            print("Listening for cancel phrase...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")
                score = self.evaluate_confidence(text)
                return text, score
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return "", 0.0
            except sr.RequestError as e:
                print(f"API Error: {e}")
                return "", 0.0

    def evaluate_confidence(self, recognized_text: str) -> float:
        scores = [SequenceMatcher(None, recognized_text, phrase).ratio() for phrase in self.cancel_phrases]
        best_score = max(scores, default=0.0)
        print(f"Best match score: {best_score}")
        return best_score

    def is_cancel_triggered(self, recognized_text: str) -> bool:
        confidence = self.evaluate_confidence(recognized_text)
        return confidence >= self.confidence_threshold

    def add_phrase(self, phrase: str):
        phrase = phrase.lower()
        if phrase not in self.cancel_phrases:
            self.cancel_phrases.append(phrase)

    def remove_phrase(self, phrase: str):
        phrase = phrase.lower()
        if phrase in self.cancel_phrases:
            self.cancel_phrases.remove(phrase)
