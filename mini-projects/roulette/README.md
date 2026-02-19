\# 🎰 Mini Roulette – Tkinter Python Game



Mini Roulette is a simple desktop roulette game built with Python and Tkinter.  

The player starts with 100 points and can bet on Red, Black, or Green.



It’s a lightweight project perfect for beginners learning:

\- Python basics

\- GUI development with Tkinter

\- Random number generation

\- Simple game logic





\# 📸 Preview



Small desktop window with:

\- Points counter

\- Bet input field

\- Buttons for Red / Black / Green

\- Result message display





\# ⚙️ How It Works



The game simulates a roulette wheel with the following color distribution:



🔴 Red → 7 slots  

⚫ Black → 7 slots  

🟢 Green → 1 slot  



Total: 15 possible outcomes





\# 💰 Payout Rules



Red   → x2  → 7/15  

Black → x2  → 7/15  

Green → x14 → 1/15  



If you win on Red or Black, you receive 2× your bet.  

If you win on Green, you receive 14× your bet.  

If you lose, your bet is subtracted from your points.





\# 🚀 Installation \& Usage



\## Requirements



\- Python 3.x installed  

\- Tkinter (usually included with Python)  



To check Python version:

python --version





\## Running the Game



Save the file as:

mini\_roulette.py



Then run:

python mini\_roulette.py



The game window will open.





\# 🎮 How to Play



1\. Enter your bet amount in the input field.  

2\. Click one of the color buttons:

&nbsp;  - Red

&nbsp;  - Black

&nbsp;  - Green  

3\. The game will randomly choose a result.  

4\. Your points will update automatically.  

5\. Try not to go bankrupt 😉





\# 🧠 Code Overview



The project contains:



\## spin(color\_choice)



Handles:

\- Bet validation  

\- Random color selection  

\- Win/loss calculation  

\- UI updates  



\## Tkinter widgets



\- Label for displaying points and results  

\- Entry for bet input  

\- Button for color selection  



Random selection is handled by:

random.choice(colors)





\# 📌 Starting Points



Players begin with:

100 points





\# 🛠 Possible Improvements



\- Add sound effects  

\- Add animations  

\- Add reset button  

\- Add game history log  

\- Improve UI design  

\- Add balance persistence (save to file)  

\- Add real roulette wheel visualization  

\- Fix label typo: "Body" → "Points"





\# 📄 License



This project is free to use and modify for educational purposes.





\# 👨‍💻 Author



Created as a simple Python Tkinter learning project.



