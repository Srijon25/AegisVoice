# AegisVoice: profiles.py - Manage cancel phrase profiles and settings

import json
import os
from typing import Dict, List

PROFILE_STORAGE = "profiles.json"

class ProfileManager:
    def __init__(self, storage_path: str = PROFILE_STORAGE):
        self.storage_path = storage_path
        self.profiles: Dict[str, List[str]] = {}
        self.load_profiles()

    def load_profiles(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                self.profiles = json.load(file)
        else:
            self.profiles = {}

    def save_profiles(self):
        with open(self.storage_path, 'w') as file:
            json.dump(self.profiles, file, indent=4)

    def get_profiles(self) -> List[str]:
        return list(self.profiles.keys())

    def get_phrases(self, profile_name: str) -> List[str]:
        return self.profiles.get(profile_name, [])

    def add_profile(self, profile_name: str, phrases: List[str] = []):
        if profile_name not in self.profiles:
            self.profiles[profile_name] = phrases
            self.save_profiles()

    def delete_profile(self, profile_name: str):
        if profile_name in self.profiles:
            del self.profiles[profile_name]
            self.save_profiles()

    def update_phrases(self, profile_name: str, phrases: List[str]):
        if profile_name in self.profiles:
            self.profiles[profile_name] = phrases
            self.save_profiles()

    def add_phrase_to_profile(self, profile_name: str, phrase: str):
        if profile_name in self.profiles and phrase not in self.profiles[profile_name]:
            self.profiles[profile_name].append(phrase)
            self.save_profiles()

    def remove_phrase_from_profile(self, profile_name: str, phrase: str):
        if profile_name in self.profiles and phrase in self.profiles[profile_name]:
            self.profiles[profile_name].remove(phrase)
            self.save_profiles()
