# Usage Guide for AegisVoice

This guide walks you through using AegisVoice for cancel phrase recognition and threat response simulation.

---

## 1. Launch the Dashboard
```bash
streamlit run aegisvoice/ui/dashboard.py
```
You’ll see a web-based interface to interact with the app.

---

## 2. Select or Create a Profile
Use the dropdown to select an existing profile. To add a new one:
- Open `profiles.json` manually, or
- Use the `profiles.py` module:

```python
from aegisvoice.profiles import ProfileManager
pm = ProfileManager()
pm.create_profile("researcher1")
```

---

## 3. Add or Remove Phrases
In the UI, under “⚙️ Edit Profile”, enter your cancel phrase and click "➕ Add Phrase".

To remove:
- Select from the dropdown and click "❌ Remove Phrase"

---

## 4. Simulate Threat Event
Click "🚨 Simulate Threat Event" to test a fake threat situation and view the mock system response.

---

## 5. Live Listening and Detection
Click "🎙️ Listen for Cancel Phrase" to:
- Activate your mic
- Recognize spoken phrases
- See confidence score and response

---

## 6. Logs
Check all logged detections and simulations in `logs/aegisvoice.log`.

---

## Tips
- Use unique, unambiguous cancel phrases.
- Adjust thresholds in `evaluator.py` if needed.
- Log file grows — consider rotating or archiving periodically.

For technical details, see [index.md](index.md).
