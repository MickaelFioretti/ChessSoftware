# --- import ---
import os


# --- function ---
def clear_shell():
    """Clear the shell"""
    os.system("cls" if os.name == "nt" else "clear")
