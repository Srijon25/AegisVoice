# AegisVoice: logger.py - Secure logging of phrase detection and system events

import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "aegisvoice.log")

os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_event(message: str, level: str = "info"):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(message)

def log_detection(text: str, confidence: float, triggered: bool):
    status = "TRIGGERED" if triggered else "NOT TRIGGERED"
    log_event(f"Detection: '{text}' | Confidence: {confidence:.2f} | Status: {status}")

def log_simulation(threat_level: str, response_time: int):
    log_event(f"Simulated Threat: Level={threat_level}, Delay={response_time}s")

def get_log_path() -> str:
    return LOG_FILE
