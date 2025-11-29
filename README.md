#  DreamSim: Just Imagine to create Game !!


[![Powered by Gemini Pro](https://img.shields.io/badge/AI-Gemini--Pro--Latest-blue)](https://deepmind.google/technologies/gemini/)
[![Built With Pygame](https://img.shields.io/badge/Engine-Pygame-yellow)](https://www.pygame.org/)

**DreamSim** is an autonomous multi-agent system that creates playable mini-games from a your imagination. It designs the rules, generates procedural art, writes the Python code, and debugs itself.



## 🧠 How It Works
DreamSim uses a **4-Agent Pipeline** to simulate a game studio:

1. **User Input:** "A ninja jumping over lava."
2. **Vision Agent:** Writes the Game Design Document (JSON).
3. **Artist Agent:** Codes procedural assets (draws shapes/sprites via code).
4. ** Engineer Agent:** Writes the full `game.py` using Pygame logic.
5. ** QA Agent:** Scans for bugs and fixes syntax errors.
6. **Output:** A fully playable game window opens.

---

##  Quick Start (Run Locally)

### 1. Installation
git clone https://github.com/Aryan-0708/DreamSim_Capstone_Project.git
cd DreamSim_Capstone_Project
pip install -r requirements.txt

2. Security Setup

Create a file named .env in the root folder and add your Google API Key:
GOOGLE_API_KEY=YOUT_API_KEY

3. Run

python main.py
Enter a prompt like:

A space shooter where a triangle ship shoots green asteroids.

 Tech Stack
AI Model: Google Gemini  (via google-generativeai)

Game Engine: Pygame

Logic: Python 3 + Multi-Agent Orchestration

 Project Structure
bash
Copy code
main.py          # The entry point that runs the pipeline
agents.py        # Contains the 4 AI agent definitions
prompts.py       # System instructions for the LLM
requirements.txt # Dependencies

 Future Upgrades (Planned)
Web-based game rendering

Persistent asset storage

Fine-tuned agent personalities

Multiplayer support

 Contribution
Feel free to open issues or submit PRs. Ideas and improvements are welcome!

 Inspiration
DreamSim was built to explore whether a single sentence can become a fully playable game—turns out, it
