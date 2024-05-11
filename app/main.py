import tkinter as tk
import os
import sys

# Get the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project directory to the Python path
sys.path.append(os.path.join(project_dir, '..'))
from app.gui import MainWindow

def main():
    # root = tk.Tk()
    app = MainWindow(None)
    app.mainloop()

if __name__ == "__main__":
    main()