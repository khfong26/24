# 24 Game 🃏

**Play it live:** [Insert your Render Link Here]

A sleek, interactive web application of the classic math puzzle game "24". The app generates four random playing cards and challenges the user to use basic arithmetic (addition, subtraction, multiplication, division) to manipulate the values so they equal exactly 24.

## Features
* **Algorithmic Validation:** Features a custom backend recursive solver. Before any hand is served to the frontend, the Python backend builds a mathematical decision tree to verify that a valid integer-based solution exists, ensuring the user is never given an impossible puzzle.
* **Modern UI/UX:** Clean, responsive interface built with Vanilla JavaScript and CSS, featuring smooth hover animations and dynamic DOM updates.
* **Clipboard Sharing:** Includes a quick-share feature that copies the current hand to the user's clipboard for easy sharing.

## Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Deployment:** Gunicorn, Render

