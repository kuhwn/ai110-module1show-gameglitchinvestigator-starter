# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.

The purpose of the game is to guess the secret number. The game will either prompt for the guess to be **higher** or **lower**. By default, each game has three attempts, although there are difficulties you can select.

- [X] Detail which bugs you found.

There were reversed hints, so higher numbers were prompted to be lower, and vice versa.

There were also wrong hints for even attempts.

- [X] Explain what fixes you applied.

To fix it, the hints were reversed to their normal course to be correct. The secret turned to string code was removed for correctness.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 10
2. The game returns "📈 Go HIGHER!"
3. User enters a guess of 60
4. The game returns "📉 Go LOWER!"
5. Depending on the tries, the score could either go down if failed, and go up if won
6. The game ends when the user has a correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```zsh
===================================================== test session starts =====================================================
platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/kelvin/f2026/codepath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 11 items                                                                                                            

tests/test_game_logic.py ...........                                                                                    [100%]

===================================================== 11 passed in 0.01s ======================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
