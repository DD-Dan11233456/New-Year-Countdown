import tkinter as tk
from datetime import datetime, timedelta

def get_next_new_year():
    now = datetime.now()
    next_year = now.year + 1
    return datetime(next_year, 1, 1)

def update_countdown():
    now = datetime.now()
    remaining = target - now

    total_seconds = int(remaining.total_seconds())
    total_minutes = total_seconds // 60
    total_hours = total_minutes // 60
    total_days = remaining.days

    if mode.get() == "seconds":
        display = f"{total_seconds:,} seconds"
    elif mode.get() == "minutes":
        display = f"{total_minutes:,} minutes"
    elif mode.get() == "hours":
        display = f"{total_hours:,} hours"
    elif mode.get() == "days":
        display = f"{total_days:,} days"

    label.config(text=display)
    root.after(500, update_countdown)

def set_mode(new_mode):
    mode.set(new_mode)

root = tk.Tk()
root.title("New Year Countdown")

target = get_next_new_year()
mode = tk.StringVar(value="seconds")

label = tk.Label(root, text="", font=("Arial", 32))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Seconds", width=10, command=lambda: set_mode("seconds")).grid(row=0, column=0)
tk.Button(button_frame, text="Minutes", width=10, command=lambda: set_mode("minutes")).grid(row=0, column=1)
tk.Button(button_frame, text="Hours", width=10, command=lambda: set_mode("hours")).grid(row=0, column=2)
tk.Button(button_frame, text="Days", width=10, command=lambda: set_mode("days")).grid(row=0, column=3)

update_countdown()
root.mainloop()
