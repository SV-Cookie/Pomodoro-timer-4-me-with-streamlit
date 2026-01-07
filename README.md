# 🍅 Pomodoro Timer (Streamlit)

A simple Pomodoro-style timer built with Python using the Streamlit library to turn code into a usable webpage learn how to build and run a small interactable webpage locally

A first project that I can use to learn basic streamlit syntax and logic (e.g. st.placeholder(), time.sleep()) so that I can play around with it and build something better and more robust in the future

What does it do?
- Choose Work time (minutes) with a slider
- Choose Break time (minutes) with a slider
- Click Start
- The app counts down the work session, then counts down the break session

Lessons Learnt:
- How Streamlit runs a script top-to-bottom and updates UI from widgets (e.g., sliders and buttons)
- How to use st.empty() as a placeholder to update text dynamically in one area
- Basic countdown logic using Python and time.sleep()

--> This is a first-iteration prototype. While the couting-down, the app may not be interacted with because the countdown uses `time.sleep()` to pause the program execution.

If you want to use it...

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install streamlit

streamlit run timer_app.py

Folder
├─ timer_app.py
└─ .gitignore

### 1) Clone the repo
```bash
git clone https://github.com/<ySV-Cookie>/<yPomodoro-timer-4-me-with-streamlit>.git
cd  Pomodoro-timer-4-me-with-streamlit
