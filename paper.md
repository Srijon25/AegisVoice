title: "AegisVoice: Open Software for Cancel Phrase Verification and Threat Response" authors:

name: Srijon Kumar Shill affiliation: 1 affiliations: name: Independent Researcher index: 1 date: 2025-06-08 bibliography: paper.bib Summary 

AegisVoice is an open-source software platform designed for detecting spoken cancel phrases and simulating threat response behavior in real-time voice interfaces. With increasing adoption of voice-activated systems in critical domains such as home automation, healthcare, and industrial safety, AegisVoice provides a needed framework for testing the effectiveness of voice-based override systems under uncertain conditions. The software offers both a GUI for non-technical users and a programmable API for researchers.

AegisVoice allows users to define and manage profiles containing cancel phrases (e.g., "abort operation", "stop now", "shutdown"). It uses robust speech recognition (via SpeechRecognition and PyAudio) combined with semantic similarity scoring (via RapidFuzz) to evaluate how closely a spoken input matches an authorized cancel phrase. When a match with sufficient confidence is detected, the system can simulate threat responses or log override events for audit and analysis.

The project supports customizable thresholds, undo timers, phrase feedback, and confidence scoring visualization. It is especially suited for HCI research, usability testing, and resilience studies in high-stakes environments.

Statement of Need 

Voice interfaces are increasingly employed in settings where safety, reliability, and rapid overrides are critical. However, there is a lack of open tools for evaluating how effectively such systems respond to cancel phrases in dynamic and noisy environments. AegisVoice fills this gap by providing:

An extensible platform to benchmark override behavior Tools for real-time speech evaluation and logging A GUI and test suite for reproducibility and usability testing Modular design for integration into broader research pipelines Functionality 

The core features of AegisVoice include:

Speech Recognition: Real-time speech-to-text via microphone input Phrase Detection: Approximate matching against a customizable cancel phrase set Confidence Evaluation: Semantic similarity scoring with tunable thresholds Simulation Mode: Trigger events to simulate a real-time system response Undo and Logging: Audit trails, profile backups, and undo capabilities GUI Interface: Interactive web app using Streamlit Testing and Reproducibility: Automated tests for components Installation and Usage pip install -r requirements.txt streamlit run aegisvoice/ui/dashboard.py 

Users can define profiles, test phrases, and run simulations directly through the dashboard. The system can also be used headlessly via the Python API.

Comparison to Other Tools 

While commercial voice assistants offer override capabilities, they are typically closed systems without tunable or testable phrase management. AegisVoice is distinct in its transparency, modularity, and focus on research-grade evaluation of cancel phrase reliability.

Development and Contributions 

The project is actively maintained on GitHub and welcomes contributions via pull requests or issues. Contributions to features, documentation, and language support are especially encouraged.

Acknowledgements 

This work was developed independently by the author. It builds on the excellent libraries: speechrecognition, pyaudio, rapidfuzz, scikit-learn, and streamlit.

References Warden, P. (2018). Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition. arXiv preprint arXiv:1804.03209. Cox, S. J., et al. (2008). Challenges and opportunities in human-machine interaction. IEEE Transactions on Systems, Man, and Cybernetics. RapidFuzz: Fuzzy String Matching in Python. https://github.com/maxbachmann/RapidFuzz Streamlit Documentation. https://docs.streamlit.io 
