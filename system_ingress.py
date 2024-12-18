import tkinter as tk
import random
import string
from typing import List, Callable
import os

# Cross-platform sound handling
try:
    # Try to import winsound for Windows
    import winsound
    def play_sound(success=True):
        frequency = 1000 if success else 500
        winsound.Beep(frequency, 100)
except ImportError:
    try:
        # Fallback to playsound for other platforms
        from playsound import playsound
        def play_sound(success=True):
            # Create sounds directory if it doesn't exist
            if not os.path.exists('sounds'):
                os.makedirs('sounds')
            
            # Create simple sound files if they don't exist
            success_sound = os.path.join('sounds', 'success.wav')
            fail_sound = os.path.join('sounds', 'fail.wav')
            
            try:
                playsound(success_sound if success else fail_sound, False)
            except:
                pass  # Silently fail if sound doesn't work
    except ImportError:
        # If no sound library is available, just pass silently
        def play_sound(success=True):
            pass

class MatrixColumn:
    def __init__(self, x: int, speed: float = 1.0, message_char: str = None):
        self.x = x
        self.y = 0
        self.speed = speed
        self.chars = []
        self.length = random.randint(5, 15)
        self.message_char = message_char
        self.message_pos = random.randint(0, self.length-1) if message_char else -1
        
    def update(self, height: int) -> bool:
        self.y += self.speed
        if len(self.chars) < self.length and random.random() < 0.3:
            if len(self.chars) == self.message_pos and self.message_char:
                self.chars.append(self.message_char)
            else:
                self.chars.append(random.choice(string.ascii_letters + string.digits))
        if self.y - len(self.chars) > height:
            return False
        return True

class SecurityLayer:
    def __init__(self, prompt: str, validator: Callable[[str], bool], hint: str = ""):
        self.prompt = prompt
        self.validator = validator
        self.hint = hint

class SystemIngressGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Ingress")
        self.root.configure(bg='black')
        
        # Set window size and center it
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Initialize game state
        self.current_layer = 0
        self.game_active = False
        self.matrix_columns = []
        self.message_timer = 0
        self.start_message = "TYPE START TO BEGIN"
        self.message_index = 0
        
        # Create security layers
        self.layers = self._create_security_layers()
        
        # Setup UI
        self._setup_ui()

    def _setup_ui(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Terminal output
        self.terminal = tk.Text(
            self.main_frame,
            bg='black',
            fg='#00FF00',
            insertbackground='#00FF00',
            font=('Courier', 12),
            wrap=tk.WORD,
            height=25
        )
        self.terminal.pack(fill=tk.BOTH, expand=True)
        self.terminal.config(state=tk.DISABLED)
        
        # Input frame
        input_frame = tk.Frame(self.main_frame, bg='black')
        input_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Command prompt label
        self.prompt_label = tk.Label(
            input_frame,
            text=">",
            bg='black',
            fg='#00FF00',
            font=('Courier', 12)
        )
        self.prompt_label.pack(side=tk.LEFT)
        
        # Input entry
        self.input_entry = tk.Entry(
            input_frame,
            bg='black',
            fg='#00FF00',
            insertbackground='#00FF00',
            font=('Courier', 12),
            bd=0,
            highlightthickness=1,
            highlightcolor='#00FF00'
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        self.input_entry.bind('<Return>', self._process_input)
        self.input_entry.focus_set()
        
        # Start the matrix effect
        self.root.after(50, self._update_matrix)

    def _create_security_layers(self) -> List[SecurityLayer]:
        return [
            SecurityLayer(
                "SECURITY LAYER 1: Pattern Recognition\n\n"
                "ACCESS CODE SEQUENCE: XYZXYZABXYZXYZ\n"
                "IDENTIFY THE REPEATING PATTERN TO PROCEED\n",
                lambda x: x.upper() == "XYZXYZ",
                "Hint: Look for the longest repeating sequence..."
            ),
            SecurityLayer(
                "SECURITY LAYER 2: Decryption Challenge\n\n"
                "ENCRYPTED CODE: SSECCA\n"
                "DECRYPT THE CODE TO PROCEED\n"
                "HINT: REVERSE ENGINEERING REQUIRED\n",
                lambda x: x.upper() == "ACCESS",
                "Hint: What you're trying to gain..."
            ),
            SecurityLayer(
                "SECURITY LAYER 3: Logic Gate\n\n"
                "IF A = 1 AND B = 2 THEN C = 3\n"
                "IF X = 3 AND Y = 1 THEN Z = ?\n"
                "SOLVE FOR Z TO PROCEED\n",
                lambda x: x == "2",
                "Hint: Follow the pattern..."
            ),
            SecurityLayer(
                "SECURITY LAYER 4: Timing Protocol\n\n"
                "SYNCHRONIZATION REQUIRED\n"
                "PRESS ENTER WHEN THE SEQUENCE '42' APPEARS\n"
                "TIMING IS CRUCIAL\n",
                lambda x: True,  # Special case handled in _process_input
                "Hint: Watch carefully..."
            )
        ]

    def _write_to_terminal(self, text: str):
        self.terminal.config(state=tk.NORMAL)
        self.terminal.insert(tk.END, text)
        self.terminal.see(tk.END)
        self.terminal.config(state=tk.DISABLED)
        self.root.update()

    def _update_matrix(self):
        if not self.game_active:
            # Add new columns randomly
            if random.random() < 0.1 and len(self.matrix_columns) < 80:
                x = random.randint(0, 79)
                speed = random.uniform(0.2, 0.5)
                
                # Occasionally add a message character
                message_char = None
                if random.random() < 0.1 and self.message_index < len(self.start_message):
                    message_char = self.start_message[self.message_index]
                    self.message_index = (self.message_index + 1) % len(self.start_message)
                
                self.matrix_columns.append(MatrixColumn(x, speed, message_char))
            
            # Update existing columns
            self.terminal.config(state=tk.NORMAL)
            self.terminal.delete('1.0', tk.END)
            
            # Create the matrix display
            display = [[' ' for _ in range(80)] for _ in range(25)]
            
            # Update columns and fill display
            active_columns = []
            for col in self.matrix_columns:
                if col.update(25):
                    for i, char in enumerate(col.chars):
                        y = int(col.y) - i
                        if 0 <= y < 25:
                            display[y][col.x] = char
                    active_columns.append(col)
            self.matrix_columns = active_columns
            
            # Convert display to text
            text = '\n'.join(''.join(row) for row in display)
            self.terminal.insert('1.0', text)
            self.terminal.config(state=tk.DISABLED)
        
        self.root.after(50, self._update_matrix)

    def _process_input(self, event=None):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        
        if not self.game_active:
            if user_input.lower() == "start":
                self.game_active = True
                self.terminal.config(state=tk.NORMAL)
                self.terminal.delete(1.0, tk.END)
                self.terminal.config(state=tk.DISABLED)
                self._start_game()
            return
            
        if self.current_layer >= len(self.layers):
            return
            
        current_challenge = self.layers[self.current_layer]
        
        if current_challenge.validator(user_input):
            play_sound(True)  # Success sound
            self._write_to_terminal(f"\nSECURITY LAYER {self.current_layer + 1} BYPASSED...\n\n")
            self.current_layer += 1
            
            if self.current_layer >= len(self.layers):
                self._victory_sequence()
            else:
                self._write_to_terminal(self.layers[self.current_layer].prompt)
        else:
            play_sound(False)  # Failure sound
            self._write_to_terminal("\nACCESS DENIED. TRY AGAIN.\n")
            if current_challenge.hint:
                self._write_to_terminal(f"\n{current_challenge.hint}\n")

    def _start_game(self):
        self._write_to_terminal(
            "INITIALIZING SYSTEM INGRESS PROTOCOL...\n\n"
            "WARNING: UNAUTHORIZED ACCESS DETECTED\n"
            "SECURITY SYSTEMS ENGAGED\n\n"
        )
        self._write_to_terminal(self.layers[0].prompt)

    def _victory_sequence(self):
        victory_text = """
ACCESS GRANTED - WELCOME TO THE MAINFRAME

█▀▄▀█ ▄▀█ █ █▄░█ █▀▀ █▀█ ▄▀█ █▀▄▀█ █▀▀
█░▀░█ █▀█ █ █░▀█ █▀░ █▀▄ █▀█ █░▀░█ ██▄

SYSTEM STATUS: COMPROMISED
ROOT ACCESS: ENABLED
SECURITY: DISABLED

CONGRATULATIONS, YOU'VE SUCCESSFULLY INFILTRATED THE SYSTEM.
        """
        self._write_to_terminal(victory_text)
        self.input_entry.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = SystemIngressGame()
    game.run()
