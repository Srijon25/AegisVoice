AegisVoice 

AegisVoice is an open-source software framework for real-time cancel phrase detection and threat response simulation. Built for researchers, developers, and security-focused human-computer interaction studies, AegisVoice offers voice-based override validation, configurable phrase profiles, semantic scoring, and a Streamlit-based GUI.

🔍 Key Features 🎙 Cancel Phrase Detection — Real-time voice input processing using speech_recognition 🧠 Semantic Scoring — Detect phrase intent with rapidfuzz-based similarity evaluation 📁 Profile Management — Add/remove user-defined cancel phrases easily 🚨 Threat Response Simulator — Mock emergency scenarios for research & testing 🖥 Streamlit Dashboard — User-friendly web UI to manage interactions 🧾 Secure Logging — Timestamped logs of phrase matches and simulations 📂 Project Structure aegisvoice/ ├── recognizer.py # Core speech recognition and phrase matching ├── evaluator.py # Scoring and confidence logic ├── simulator.py # Simulated threat response engine ├── profiles.py # Cancel phrase and profile management ├── logger.py # Logging utility ├── ui/ │ └── dashboard.py # Streamlit-based user interface tests/ ├── test_recognizer.py # Unit tests for recognizer module ├── test_evaluator.py # Unit tests for evaluator module docs/ ├── index.md # Project overview and install instructions ├── usage.md # Step-by-step user guide paper/ └── paper.md # JOSS-compatible research paper 🛠 Installation Requirements Python 3.9+ pip Microphone access Install with pip pip install -r requirements.txt 🚀 Running the App 

Start the web dashboard:

streamlit run aegisvoice/ui/dashboard.py 

Use the interface to select profiles, add phrases, simulate events, and run live speech checks.

🧪 Testing 

To run tests:

pytest tests/ 🧠 Use Cases Academic studies on human override systems Evaluation of spoken fail-safes Simulation training for safety-critical applications UX testing of speech-based commands in emergencies 📜 License 

This project is licensed under the MIT License. See the LICENSE file for details.

📣 Citation 

If you use AegisVoice for your research, please cite the paper included in paper/paper.md.

@software{shill2025aegisvoice, author = {Srijon Kumar Shill}, title = {AegisVoice: Open Software for Cancel Phrase Verification and Threat Response}, year = {2025}, publisher = {GitHub},url = {https://github.com/Srijon25/AegisVoice} } 👤 Author Name: Srijon Kumar Shill Affiliation: Independent Researcher Email: theunpredictable157@gmail.com GitHub: Srijon25 🤝 Contributions 

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit pull requests.


