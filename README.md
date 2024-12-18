# System Ingress Matrix

A Matrix-style hacking simulation game where you attempt to infiltrate a secured mainframe through multiple security layers. Test your pattern recognition, decryption, logic, and timing skills as you dive deeper into the system.

## Prerequisites

- Python 3.x installed on your system
- Tkinter (usually comes with Python installation)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/AgileTechSolutions/system-ingress.git
cd system-ingress
```

2. Install required dependencies:
```bash
# For Linux/macOS users:
pip3 install playsound

# For Windows users:
# No additional dependencies needed as winsound is part of Python standard library
```

## Running the Game

1. Open a terminal/command prompt
2. Navigate to the game directory
3. Run the game using Python:
```bash
# For Linux/macOS:
python3 system_ingress.py

# For Windows:
python system_ingress.py
```

## How to Play

### Getting Started
When you launch the game, you'll see a Matrix-style rain of characters. Hidden within this rain is a message telling you how to begin. Pay attention to the falling characters to spot it.

### Game Structure
The game consists of 4 security layers, each with a unique challenge:

#### Layer 1: Pattern Recognition
- You'll be presented with a sequence of characters
- Your task is to identify the repeating pattern within the sequence
- Look carefully at the string and find the longest repeating substring

#### Layer 2: Decryption Challenge
- You'll receive a scrambled code
- Rearrange the letters to form a meaningful word
- The hint provides context about what you're trying to achieve

#### Layer 3: Logic Gate
- A series of logical statements will be presented
- Use deductive reasoning to determine the correct value
- Pay attention to the relationships between variables

#### Layer 4: Timing Protocol
- This layer tests your reflexes and timing
- Watch for a specific sequence to appear
- Press Enter at the precise moment to succeed

### Controls
- Type your answers in the input field at the bottom of the screen
- Press Enter to submit your answer
- Watch for feedback after each attempt
- Use hints if you get stuck

### Tips
- Pay attention to the hints provided for each layer
- If you fail, the system will let you try again
- Look for patterns and relationships in the challenges
- Some challenges may require quick reactions
- Read all instructions carefully before attempting a solution

### Victory
Once you successfully bypass all security layers, you'll gain access to the mainframe and be presented with a victory screen.

## Features

- Matrix-style interface with falling green characters
- Four unique security challenges
- Cross-platform sound effects for feedback
- Progressive difficulty
- Hint system
- Real-time visual feedback
- Victory sequence with ASCII art

## Technical Details

The game is built using:
- Python 3.x
- Tkinter for GUI
- Cross-platform sound support (winsound on Windows, playsound on Linux/macOS)
- Object-oriented design principles

## Platform-Specific Notes

### Windows
- Uses built-in winsound module for sound effects
- No additional sound dependencies required

### Linux/macOS
- Uses playsound library for sound effects
- Requires installation of playsound package (`pip3 install playsound`)
- Sound effects are optional and the game will run without them if playsound is not installed

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
