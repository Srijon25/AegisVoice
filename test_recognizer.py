# tests/test_recognizer.py

import unittest
from unittest.mock import patch, MagicMock
from aegisvoice.recognizer import CancelPhraseRecognizer

class TestCancelPhraseRecognizer(unittest.TestCase):
    def setUp(self):
        self.phrases = ["cancel operation", "abort mission", "stop"]
        self.recognizer = CancelPhraseRecognizer(cancel_phrases=self.phrases)

    @patch("aegisvoice.recognizer.sr.Recognizer")
    @patch("aegisvoice.recognizer.sr.Microphone")
    def test_listen_and_recognize(self, mock_microphone, mock_recognizer_class):
        mock_recognizer = MagicMock()
        mock_recognizer.recognize_google.return_value = "cancel operation"
        mock_recognizer.listen.return_value = "mock_audio"
        mock_recognizer_class.return_value = mock_recognizer

        result, score = self.recognizer.listen_and_recognize()

        self.assertEqual(result, "cancel operation")
        self.assertGreaterEqual(score, 0.75)  # Assuming similarity threshold

if __name__ == '__main__':
    unittest.main()
