from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    tomato.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, highlightthickness=0, fg=GREEN)
    check_label.config(text='')
    start_button['state'] = 'active'
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_seconds)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    start_button['state'] = 'disabled'
    count_min = count // 60
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    tomato.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(reps//2):
            marks += '✔'
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, highlightthickness=0, fg=GREEN)
timer_label.grid(column=1, row=0)

tomato = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
tomato.create_image(100, 112, image=tomato_img)
timer_text = tomato.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
tomato.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
