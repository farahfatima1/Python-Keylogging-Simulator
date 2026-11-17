import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from datetime import datetime
import os

LOG_FILE = Path("logs/keystrokes.txt")
LOG_FILE.parent.mkdir(exist_ok=True)
LOG_FILE.write_text("")

BG, CARD = "#0B1220", "#111C2E"
TEXT, SECONDARY = "#F8FAFC", "#94A3B8"
ACCENT, SUCCESS, DANGER = "#00D9FF", "#22C55E", "#EF4444"


def log_key(event):
    key = event.keysym
    special = {
        "space": "[SPACE]",
        "Return": "[ENTER]",
        "BackSpace": "[BACKSPACE]",
        "Tab": "[TAB]",
        "Escape": "[ESC]"
    }
    key = special.get(key, f"[{key.upper()}]" if len(key) > 1 else key)

    with LOG_FILE.open("a") as f:
        f.write(f"{datetime.now():%H:%M:%S} - {key}\n")

    status.config(text=f"● ACTIVE | Last Key: {key}")
    total.config(text=len(LOG_FILE.read_text().splitlines()))


def clear_session():
    if messagebox.askyesno("Clear Session", "Clear current test session?"):
        LOG_FILE.write_text("")
        text.delete("1.0", tk.END)
        total.config(text="0")
        status.config(text="● READY | Session Cleared")


def open_log():
    if LOG_FILE.exists():
        os.startfile(LOG_FILE.resolve())
    else:
        messagebox.showinfo("Log File", "No log file exists yet.")


def end_session():
    messagebox.showinfo(
        "Session Complete",
        "Test session completed.\n\nSaved to logs/keystrokes.txt"
    )
    root.destroy()


root = tk.Tk()
root.title("Key Logging Simulator")
root.geometry("900x600")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root, text="KEY LOGGING SIMULATOR",
    font=("Arial", 24, "bold"), fg=TEXT, bg=BG
).pack(anchor="w", padx=30, pady=(25, 2))

tk.Label(
    root, text="Cybersecurity Laboratory • Controlled Environment",
    font=("Arial", 11), fg=SECONDARY, bg=BG
).pack(anchor="w", padx=30)

status = tk.Label(
    root, text="● READY | Waiting for test input...",
    font=("Arial", 11, "bold"), fg=SUCCESS, bg=CARD
)
status.pack(fill="x", padx=30, pady=15, ipady=10)

frame = tk.Frame(root, bg=CARD)
frame.pack(fill="x", padx=30)

tk.Label(
    frame, text="SESSION STATISTICS",
    font=("Arial", 11, "bold"), fg=SECONDARY, bg=CARD
).pack(anchor="w", padx=20, pady=(15, 0))

total = tk.Label(
    frame, text="0",
    font=("Arial", 28, "bold"), fg=ACCENT, bg=CARD
)
total.pack(anchor="w", padx=20)

tk.Label(
    frame, text="Total Keystrokes",
    font=("Arial", 10), fg=SECONDARY, bg=CARD
).pack(anchor="w", padx=20, pady=(0, 15))

tk.Label(
    root, text="CONTROLLED TEST INPUT",
    font=("Arial", 11, "bold"), fg=TEXT, bg=BG
).pack(anchor="w", padx=30, pady=(15, 5))

text = tk.Text(
    root, height=10, width=92,
    font=("Consolas", 12),
    bg="#0F172A", fg=TEXT,
    insertbackground=ACCENT,
    relief="flat", padx=15, pady=15
)
text.pack(padx=30)
text.bind("<Key>", log_key)
text.focus()

tk.Label(
    root,
    text="⚠ Authorized laboratory testing only • Do not enter real passwords",
    font=("Arial", 9), fg=SECONDARY, bg=BG
).pack(pady=10)

buttons = tk.Frame(root, bg=BG)
buttons.pack(fill="x", padx=30, pady=5)

tk.Button(
    buttons, text="CLEAR SESSION", command=clear_session,
    bg=CARD, fg=TEXT, relief="flat", padx=18, pady=8
).pack(side="left")

tk.Button(
    buttons, text="OPEN LOG", command=open_log,
    bg=CARD, fg=TEXT, relief="flat", padx=18, pady=8
).pack(side="left", padx=10)

tk.Button(
    buttons, text="END SESSION", command=end_session,
    bg=DANGER, fg=TEXT, relief="flat", padx=18, pady=8
).pack(side="right")

tk.Label(
    root, text="Key Logging Simulator v2.0 | Local Controlled Test",
    font=("Arial", 9), fg=SECONDARY, bg=BG
).pack(side="bottom", pady=10)

root.mainloop()