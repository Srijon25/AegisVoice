# AegisVoice: simulator.py - Simulates threat scenarios and responses

import time
import random

class ThreatSimulator:
    def __init__(self):
        self.threat_levels = ['Low', 'Moderate', 'High', 'Critical']
        self.active = False

    def simulate_threat_event(self) -> dict:
        self.active = True
        level = random.choices(
            self.threat_levels,
            weights=[0.5, 0.3, 0.15, 0.05],
            k=1
        )[0]
        delay = random.randint(2, 5)
        time.sleep(delay)
        self.active = False
        return {
            "level": level,
            "response_time": delay,
            "message": f"Simulated {level} threat after {delay}s delay."
        }

    def respond_to_cancel(self, trigger_detected: bool) -> str:
        if trigger_detected:
            return "🛑 Cancel phrase detected. All threat actions terminated."
        else:
            return "⚠️ No cancel phrase detected. Continuing threat simulation."

    def get_status(self) -> str:
        return "Active" if self.active else "Idle"
