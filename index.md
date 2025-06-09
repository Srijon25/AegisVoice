# AegisVoice Documentation

Welcome to the **AegisVoice** documentation. AegisVoice is an open-source, speech-enabled security tool designed to detect cancel phrases and simulate response actions in threat scenarios. Built for research and reproducibility, it supports configurable profiles, threat simulations, and evaluation logging.

## Features
- 🎙 Cancel phrase detection via speech
- 🧠 Semantic similarity scoring
- 🔄 Profile and phrase management
- 🧪 Threat response simulation
- 🧾 Secure logging
- 🖥 GUI dashboard with Streamlit

## Project Structure
```
aegisvoice/
├── recognizer.py       # Speech detection core
├── evaluator.py        # Confidence scoring
├── simulator.py        # Simulated threat responses
├── profiles.py         # Cancel phrase profile manager
├── ui/dashboard.py     # Streamlit dashboard
├── logger.py           # Logging events
```

## Install
```bash
pip install -r requirements.txt
```

## Run GUI
```bash
streamlit run aegisvoice/ui/dashboard.py
```

## License
MIT License. See [LICENSE](../LICENSE).

## Citation
If using for academic purposes, cite the accompanying paper in the `paper/` directory.

---
For usage instructions, see [docs/usage.md](usage.md).
