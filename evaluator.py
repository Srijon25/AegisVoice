# AegisVoice: evaluator.py - Advanced scoring and semantic confidence

from difflib import SequenceMatcher
from typing import List
from transformers import pipeline

class PhraseEvaluator:
    def __init__(self, cancel_phrases: List[str], use_semantics: bool = True):
        self.cancel_phrases = [p.lower() for p in cancel_phrases]
        self.use_semantics = use_semantics
        self.similarity_threshold = 0.75
        if use_semantics:
            self.similarity_model = pipeline("feature-extraction", model="distilbert-base-uncased")

    def basic_similarity(self, text1: str, text2: str) -> float:
        return SequenceMatcher(None, text1, text2).ratio()

    def semantic_similarity(self, text1: str, text2: str) -> float:
        import numpy as np
        vec1 = self.similarity_model(text1)[0][0]
        vec2 = self.similarity_model(text2)[0][0]
        sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        return float(sim)

    def evaluate(self, input_text: str) -> float:
        input_text = input_text.lower()
        scores = []
        for phrase in self.cancel_phrases:
            base_score = self.basic_similarity(input_text, phrase)
            if self.use_semantics:
                sem_score = self.semantic_similarity(input_text, phrase)
                final_score = (base_score + sem_score) / 2
            else:
                final_score = base_score
            scores.append(final_score)
        return max(scores, default=0.0)

    def is_triggered(self, input_text: str) -> bool:
        score = self.evaluate(input_text)
        return score >= self.similarity_threshold
