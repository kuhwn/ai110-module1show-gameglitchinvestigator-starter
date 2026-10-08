# 💭 Reflection: Game Glitch Investigator

> Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

> What did the game look like the first time you ran it?
>
> List at least two concrete bugs you noticed at the start  
>  (for example: "the hints were backwards").


- When I first ran the game, the only bug I found was just that the hints are reversed, and are incorrect.

---

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input       | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
| ----------- | ----------------- | --------------- | ---------------------- | ----------------------- |
| guess of 4  | Go higher hint    | 📉 Go LOWER!    | none                   | `app.py`, `check_guess` |
| guess of 50 | Go lower hint     | 📈 Go HIGHER!   | none                   | `app.py`, `check_guess` |

---

## 2. How did you use AI as a teammate?

> Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
>
> Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
>
> Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

- I used Claude Code for this project, and it pointed out that the bugs existed in `app.py`. The AI suggested swapping the hints because they were reversed. 

- I knew the reversed hints was true because I tried out the program on Streamlit, and it was working like it should have. It made a quick fix.

---

## 3. Debugging and testing your fixes

> How did you decide whether a bug was really fixed?
> Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
> Did AI help you design or understand any tests? How?

- I asked AI to help me break down concepts I didn't understand, and I used `pytest` to run the tests it gave me. I decided the bug was finished when it worked, but I should probably run some more tests next time.

---

## 4. What did you learn about Streamlit and state?

> How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- **Reruns** are when Streamlit runs the entire `app.py` file again, and produces a fresh run to your page, instead of updating on the spot.

- **Session states**, like `st.session_state` is like a portion that isn't affected by the reruns.

---

## 5. Looking ahead: your developer habits

> What is one habit or strategy from this project that you want to reuse in future labs or projects?
>  - This could be a testing habit, a prompting strategy, or a way you used Git.
> 
> What is one thing you would do differently next time you work with AI on a coding task?
> In one or two sentences, describe how this project changed the way you think about AI generated code.

I think it was very helpful to use Claude Code to help write a README. It would be useful in the future to give a few ideas on how to document changes to code.

I think the next time I worked with AI on a coding task, I would slow down more and try to understand what's happening under the hood. Fundamentals are still very important to know, so that arbitrary code does not get committed and pushed.