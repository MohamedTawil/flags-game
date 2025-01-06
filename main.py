from tkinter import *
import pandas
import random

correct_answer = 0
answer = 0
wrong_answers = 0
country_r = 0
r_list = []


country_images = {}


def easy():
    global codes_list, copy_list, codes_data, country_images
    codes_list.clear()
    for _ in range(22):
        codes_list.append(copy_list[_])

    copy_list.clear()

    for _ in range(22):
        copy_list.append(codes_list[_])

    place_img()


def medium():
    global codes_list, copy_list, codes_data
    codes_list.clear()

    for _ in range(22, 66):
        codes_list.append(copy_list[_])

    copy_list.clear()
    for _ in range(44):
        copy_list.append(codes_list[_])

    place_img()


def hard():
    global codes_list, copy_list, codes_data
    codes_list.clear()

    for _ in range(66, 194):
        codes_list.append(copy_list[_])

    copy_list.clear()
    for _ in range(128):
        copy_list.append(codes_list[_])

    place_img()


def all_f():
    global codes_list, copy_list, codes_data

    place_img()


def modes():
    easy_b.place(x=225, y=300)
    medium_b.place(x=225, y=420)
    hard_b.place(x=225, y=540)
    all_b.place(x=225, y=660)

    easy_b.config(command=easy)
    medium_b.config(command=medium)
    hard_b.config(command=hard)
    all_b.config(command=all_f)


def reset():
    global codes_list, copy_list, codes_data
    correct_answer_l0.place_forget()
    correct_answer_l1.place_forget()
    correct_answer_l2.place_forget()
    correct_answer_l3.place_forget()
    correct_l.place_forget()
    false_l0.place_forget()
    false_l1.place_forget()
    false_l2.place_forget()
    false_l3.place_forget()
    score_l.place_forget()
    best_score_l.place_forget()
    heart_1.place_forget()
    heart_2.place_forget()
    heart_3.place_forget()
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    button4.grid_forget()
    canvas.grid_forget()
    play_again_b.place_forget()
    bg.place_forget()
    easy_b.place_forget()
    medium_b.place_forget()
    hard_b.place_forget()
    all_b.place_forget()
    start_l.place_forget()
    startb_b.place_forget()
    startb_b.place_forget()
    home_b.place_forget()
    congrats_l.place_forget()


def start():
    global codes_list, copy_list, codes_data, wrong_answers, score
    window.geometry("750x900")
    reset()
    codes_data = pandas.read_csv("country.csv")
    codes_list = codes_data["Code"].to_list()
    copy_list = codes_data["Code"].to_list()
    heart_1.config(image=heart_img)
    heart_2.config(image=heart_img)
    heart_3.config(image=heart_img)
    wrong_answers = 0
    score = 0

    start_l.place(x=100, y=-180)
    startb_b.place(x=285, y=200)
    startb_b.config(command=modes)


def win():
    correct_answer_l0.place_forget()
    correct_answer_l1.place_forget()
    correct_answer_l2.place_forget()
    correct_answer_l3.place_forget()
    correct_l.place_forget()
    false_l0.place_forget()
    false_l1.place_forget()
    false_l2.place_forget()
    false_l3.place_forget()

    score_l.place_forget()
    best_score_l.place_forget()
    heart_1.place_forget()
    heart_2.place_forget()
    heart_3.place_forget()

    canvas.itemconfig(country_name, text="congratulation\n  YOU WON!", font=("Ariel", 40, "bold"))
    canvas.place(x=80, y=-100)
    congrats_l.place(x=300, y=70)
    bg.place(x=300, y=230)
    play_again_b.place(x=380, y=220)
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    button4.grid_forget()


def quit_loop():
    window.quit()


def play_again():
    global codes_list, copy_list, score, wrong_answers
    codes_list.clear()
    if len(copy_list) == 22:
        for _ in range(22):
            codes_list.append(copy_list[_])
    elif len(copy_list) == 44:
        for _ in range(44):
            codes_list.append(copy_list[_])
    elif len(copy_list) == 128:
        for _ in range(128):
            codes_list.append(copy_list[_])
    else:
        for _ in range(194):
            codes_list.append(copy_list[_])

    wrong_answers = 0
    heart_1.config(image=heart_img)
    heart_2.config(image=heart_img)
    heart_3.config(image=heart_img)
    score = 0
    place_img()


def lost():
    window.geometry("730x600")
    correct_answer_l0.place_forget()
    correct_answer_l1.place_forget()
    correct_answer_l2.place_forget()
    correct_answer_l3.place_forget()
    correct_l.place_forget()
    false_l0.place_forget()
    false_l1.place_forget()
    false_l2.place_forget()
    false_l3.place_forget()
    canvas.itemconfig(country_name, text="YOU LOST")

    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    button4.grid_forget()

    score_l.place(x=300, y=-75)
    canvas.place(x=50, y=-70)
    heart_1.place(x=380, y=50)
    heart_2.place(x=330, y=50)
    heart_3.place(x=280, y=50)

    play_again_b.config(image=play_again_img)
    play_again_b.place(x=280, y=80)
    home_b.place(x=-7, y=-75)


def button_1():
    global score, answer, wrong_answers, country_r
    if len(codes_list) > 0:
        pyimg = button1.cget("image")
        number = ""
        for char in pyimg:
            if char.isdigit():
                number = number + str(char)

        number = int(number)

        answer = 1
        if answer != correct_answer:
            button1.config(command="")
            false_l0.place(x=50, y=200)
            correct_answer_l0.config(text=codes_data[codes_data.index == number - 16].Title.item())
            correct_answer_l0.place(x=90, y=200)
            wrong_answers += 1
            if wrong_answers == 1:
                heart_3.config(image=empty_heart_img)
            elif wrong_answers == 2:
                heart_2.config(image=empty_heart_img)
            else:
                heart_1.config(image=empty_heart_img)
                window.after(500, lost)
                return "lost"

        if correct_answer == 1:
            correct_l.place(x=150, y=200)
            score += 1
            button1.config(command="")
            button2.config(command="")
            button3.config(command="")
            button4.config(command="")
            window.after(500, place_img)
    else:
        win()


def button_2():
    global score, answer, wrong_answers
    if len(codes_list) > 0:
        pyimg = button2.cget("image")
        number = ""
        for char in pyimg:
            if char.isdigit():
                number = number + str(char)

        number = int(number)

        answer = 2
        if answer != correct_answer:
            button2.config(command="")
            false_l1.place(x=440, y=200)
            correct_answer_l1.config(text=codes_data[codes_data.index == number - 16].Title.item())
            correct_answer_l1.place(x=480, y=200)
            wrong_answers += 1
            if wrong_answers == 1:
                heart_3.config(image=empty_heart_img)
            elif wrong_answers == 2:
                heart_2.config(image=empty_heart_img)
            else:
                heart_1.config(image=empty_heart_img)
                window.after(500, lost)
                return "lost"

        if correct_answer == 2:
            correct_l.place(x=520, y=200)
            score += 1
            button1.config(command="")
            button2.config(command="")
            button3.config(command="")
            button4.config(command="")
            window.after(500, place_img)
    else:
        win()


def button_3():
    global score, answer, wrong_answers
    if len(codes_list) > 0:
        pyimg = button3.cget("image")
        number = ""
        for char in pyimg:
            if char.isdigit():
                number = number + str(char)

        number = int(number)

        answer = 3
        if answer != correct_answer:
            button3.config(command="")
            false_l2.place(x=50, y=470)
            correct_answer_l2.config(text=codes_data[codes_data.index == number - 16].Title.item())
            correct_answer_l2.place(x=90, y=470)
            wrong_answers += 1
            if wrong_answers == 1:
                heart_3.config(image=empty_heart_img)
            elif wrong_answers == 2:
                heart_2.config(image=empty_heart_img)
            else:
                heart_1.config(image=empty_heart_img)
                window.after(500, lost)
                return "lost"

        if correct_answer == 3:
            correct_l.place(x=150, y=470)
            score += 1
            button1.config(command="")
            button2.config(command="")
            button3.config(command="")
            button4.config(command="")
            window.after(500, place_img)
    else:
        win()


def button_4():
    global score, answer, wrong_answers
    if len(codes_list) > 0:
        pyimg = button4.cget("image")
        number = ""
        for char in pyimg:
            if char.isdigit():
                number = number + str(char)

        number = int(number)

        answer = 4
        if answer != correct_answer:
            button4.config(command="")
            false_l3.place(x=410, y=470)
            correct_answer_l3.config(text=codes_data[codes_data.index == number - 16].Title.item())
            correct_answer_l3.place(x=450, y=470)
            wrong_answers += 1
            if wrong_answers == 1:
                heart_3.config(image=empty_heart_img)
            elif wrong_answers == 2:
                heart_2.config(image=empty_heart_img)
            else:
                heart_1.config(image=empty_heart_img)
                window.after(500, lost)
                return "lost"

        if correct_answer == 4:
            correct_l.place(x=520, y=470)
            score += 1
            button1.config(command="")
            button2.config(command="")
            button3.config(command="")
            button4.config(command="")
            window.after(500, place_img)
    else:
        win()


def place_img():
    global correct_answer, high_score, country_r, r_list, codes_data, codes_list, copy_list
    reset()
    congrats_l.place_forget()
    canvas.itemconfig(country_name, font=("Ariel", 25, "bold"))
    button1.config(command=button_1)
    button2.config(command=button_2)
    button3.config(command=button_3)
    button4.config(command=button_4)
    window.geometry("750x850")
    correct_answer_l0.place_forget()
    correct_answer_l1.place_forget()
    correct_answer_l2.place_forget()
    correct_answer_l3.place_forget()
    correct_l.place_forget()
    false_l0.place_forget()
    false_l1.place_forget()
    false_l2.place_forget()
    false_l3.place_forget()
    bg.place_forget()
    play_again_b.place_forget()
    score_l.place(x=300, y=-75)
    best_score_l.place(x=500, y=-75)
    heart_1.place(x=0, y=-75)
    heart_2.place(x=30, y=-80)
    heart_3.place(x=60, y=-75)

    play_again_b.config(image=splay_again_img, command=play_again)
    play_again_b.place(x=50, y=-45)
    bg.config(height=45, width=45)
    bg.place(x=650, y=-75)
    home_b.place(x=-15, y=-45)

    canvas.grid(column=0, row=0, columnspan=3)
    canvas2.grid(column=0, row=2, columnspan=3)
    canvas3.grid(column=1, row=1, rowspan=2)

    button1.grid(column=0, row=1)
    button2.grid(column=2, row=1)
    button3.grid(column=0, row=3)
    button4.grid(column=2, row=3)

    if score > int(high_score):
        high_score = score
        with open("high_score.txt", "w") as file1:
            file1.write(str(high_score))

    country_r = random.choice(codes_list)
    codes_list.remove(country_r)
    score_l.config(text=f"score\n{score}/{len(copy_list)}")
    best_score_l.config(text=f"best score\n{high_score}")

    r_list = [country_r]

    canvas.itemconfig(country_name, text=codes_data[codes_data.Code == country_r].Title.item())

    correct_answer = random.randint(1, 4)

    if correct_answer == 1:
        button1.config(image=country_images[country_r])

        keep = True

        count = 0
        while keep:
            r = random.choice(copy_list)

            if r not in r_list:
                r_list.append(r)
                count += 1
            if count == 3:
                keep = False

        button2.config(image=country_images[r_list[1]])
        button3.config(image=country_images[r_list[2]])
        button4.config(image=country_images[r_list[3]])

    elif correct_answer == 2:
        button2.config(image=country_images[country_r])

        keep = True

        count = 0
        while keep:
            r = random.choice(copy_list)

            if r not in r_list:
                r_list.append(r)
                count += 1
            if count == 3:
                keep = False

        button1.config(image=country_images[r_list[1]])
        button3.config(image=country_images[r_list[2]])
        button4.config(image=country_images[r_list[3]])

    elif correct_answer == 3:
        button3.config(image=country_images[country_r])

        keep = True

        count = 0
        while keep:
            r = random.choice(copy_list)

            if r not in r_list:
                r_list.append(r)
                count += 1
            if count == 3:
                keep = False

        button1.config(image=country_images[r_list[1]])
        button2.config(image=country_images[r_list[2]])
        button4.config(image=country_images[r_list[3]])

    else:
        button4.config(image=country_images[country_r])

        keep = True

        count = 0
        while keep:
            r = random.choice(copy_list)

            if r not in r_list:
                r_list.append(r)
                count += 1
            if count == 3:
                keep = False

        button1.config(image=country_images[r_list[1]])
        button2.config(image=country_images[r_list[2]])
        button3.config(image=country_images[r_list[3]])


window = Tk()
window.geometry("730x850")
window.title("guess the flags")
window.config(bg="#dbeff0", pady=90, padx=20)
canvas = Canvas(width=600, height=250, bg="#dbeff0", highlightthickness=0)
canvas2 = Canvas(width=50, height=50, bg="#dbeff0", highlightthickness=0)
canvas3 = Canvas(width=50, height=50, bg="#dbeff0", highlightthickness=0)

#
# codes_list = codes_data["Code"].to_list()
# copy_list = codes_data["Code"].to_list()

# print(country_images)

country_name = canvas.create_text(300, 90, text="", font=("Ariel", 25, "bold"), fill="#2596be")
score = 0

with open("high_score.txt", "r") as file:
    high_score = file.read()

score_l = Label(bg="#dbeff0", font=("Ariel", 20, "bold"), fg="#2596be")

best_score_l = Label(text=f"best score\n{high_score}", bg="#dbeff0", font=("Ariel", 14, "bold"), fg="#2596be")

heart_img = PhotoImage(file="start_imgs/heart(1).png")
empty_heart_img = PhotoImage(file="start_imgs/heart.png")
play_again_img = PhotoImage(file="start_imgs/refresh.png")
splay_again_img = PhotoImage(file="start_imgs/refresh_5174927.png")
correct_img = PhotoImage(file="start_imgs/check.png")
false_img = PhotoImage(file="start_imgs/cross.png")
background = PhotoImage(file="start_imgs/plus.png")
congrats = PhotoImage(file="start_imgs/congrats.png")
start_img = PhotoImage(file="start_imgs/kawaii.png")
startb_img = PhotoImage(file="start_imgs/start-button.png")
easy_img = PhotoImage(file="start_imgs/easy.png")
medium_img = PhotoImage(file="start_imgs/medium.png")
hard_img = PhotoImage(file="start_imgs/haed.png")
all_img = PhotoImage(file="start_imgs/all.png")
home_img = PhotoImage(file="start_imgs/home-button.png")


play_again_b = Button(image=play_again_img, highlightthickness=0, bg="#dbeff0", borderwidth=0, command=play_again)
home_b = Button(image=home_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, command=start)
start_l = Label(image=start_img, bg="#dbeff0", highlightthickness=0)
startb_b = Button(image=startb_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, height=60)
easy_b = Button(image=easy_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, height=100)
medium_b = Button(image=medium_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, height=100)
hard_b = Button(image=hard_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, height=100)
all_b = Button(image=all_img, bg="#dbeff0", highlightthickness=0, borderwidth=0, height=100)
congrats_l = Label(image=congrats, bg="#dbeff0", highlightthickness=0)
correct_l = Label(image=correct_img, bg="#dbeff0", highlightthickness=0)
false_l0 = Label(image=false_img, bg="#dbeff0", highlightthickness=0)
false_l1 = Label(image=false_img, bg="#dbeff0", highlightthickness=0)
false_l2 = Label(image=false_img, bg="#dbeff0", highlightthickness=0)
false_l3 = Label(image=false_img, bg="#dbeff0", highlightthickness=0)
bg = Button(image=background, highlightthickness=0, bg="#dbeff0", borderwidth=0, command=quit_loop)


correct_answer_l0 = Label(text="", bg="#dbeff0", font=("Ariel", 16, "bold"), fg="#2596be")
correct_answer_l1 = Label(text="", bg="#dbeff0", font=("Ariel", 16, "bold"), fg="#2596be")
correct_answer_l2 = Label(text="", bg="#dbeff0", font=("Ariel", 16, "bold"), fg="#2596be")
correct_answer_l3 = Label(text="", bg="#dbeff0", font=("Ariel", 16, "bold"), fg="#2596be")


heart_1 = Label(image=heart_img, bg="#dbeff0")
heart_2 = Label(image=heart_img, bg="#dbeff0")
heart_3 = Label(image=heart_img, bg="#dbeff0")

button1 = Button(bg="#dbeff0", width=320, height=213, highlightthickness=0, borderwidth=0, command=button_1)
button2 = Button(bg="#dbeff0", width=320, height=213, highlightthickness=0, borderwidth=0, command=button_2)
button3 = Button(bg="#dbeff0", width=320, height=213, highlightthickness=0, borderwidth=0, command=button_3)
button4 = Button(bg="#dbeff0", width=320, height=213, highlightthickness=0, borderwidth=0, command=button_4)

codes_data = pandas.read_csv("country.csv")
codes_list = codes_data["Code"].to_list()
copy_list = codes_data["Code"].to_list()
for i in codes_list:
    img_file = f"flags-imgs/{i.lower()}.png"
    country_images[i] = PhotoImage(file=img_file)
start()

window.mainloop()
