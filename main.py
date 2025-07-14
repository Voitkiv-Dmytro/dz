"""from calculations import add,minus,multiply,div,power
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = None
while choice != 0:
    choice = int(input("Enter your choice \n (0-stop program, 1-add numbers,2-minus, 3-div numbers, 4-multiply,5-power): "))
    if choice == 1:
        c = add(a,b)
        print(c)
        continue
    elif choice == 2:
        c = minus(a,b)
        print(c)
        continue
    elif choice == 3:
        c = div(a,b)
        print(c)
        continue
    elif choice == 4:
        c = multiply(a,b)
        print(c)
        continue
    elif choice ==5:
        c = power(a)
        print(c)
        continue
    else:
        print("Incorrect choice")"""

"""import os
#os.mkdir("Створена папка")
#os.rename("Створена папка", "Folder")"""
   
"""with open("file.txt", "r") as file:
    text = file.read()
    print(text)"""

"""with open("file.txt", "a+") as my_file:
    my_file.write(" This is our first text")"""

"""name = input("Введіть своє ім'я: ")
hobby = input("Введіть своє хобі: ")
dish = input("Введіть свою улюблену їжу: ")
with open("file.txt", "w") as file:
    file.write(name)
    file.write(hobby)
    file.write(dish)

with open("file.txt", "r") as file:
    text = file.read()
    print(text)
with open("file.txt", "r") as file:
    text = file.readline()
    print(text)
with open("file.txt", "r") as file:
    text = file.readlines()
    print(text)"""

"""a = int(input("Enter your choice(1-показати всі справи, 2- додати нову справу, 3-очистити справи, 4 - вийти): "))
if a == 1:
    with open("file.txt", "r") as file:
        text = file.read()
        print(text)
elif a == 2:
    b = input("Напиши справу: ")
    with open("file.txt", "a+") as file:
        file.write(b)
elif a == 3:
    with open("file.txt", "w") as file:
        file.close()
        os.remove("file.txt")
elif a == 4:
    print("Ви вийшли з програми.")"""


"""print("Вас вітає телефонна книга")
phone_book = {}
while True:
    print("1-додати новий контакт,\n2- пошук контакту,\n3-видалення контакту,\n4-вивести всі контакти")
    choice = int(input("Зробіть свій вибір: "))
    if choice == 1:
        a = input("Введіть ім'я контакту, який хочете створити: ")
        b = input("Введіть номер його телефону: ")
        phone_book[a]=b
        print("Контакт успішно створено")
        
    elif choice == 2:
        a = input("Введіть контакт який хочете знайти: ")
        if a in phone_book.keys():
            print("Контакт успішно знайдено: ")
            print(phone_book[a])
        else:
            print("На жаль, такого контакту не існує")
        
    elif choice == 3:
        a = input("Введіть контакт який хочете видалити: ")
        if a in phone_book.keys():
            del phone_book[a]
            print("Контакт успішно видалено")
        else:
            print("Невірно вказаний контакт")
        
    elif choice == 4:
        print("Список усіх контактів\n", phone_book)
        
    else:
        print("Неправильно зроблений вибір")"""


"""print("Hello world")
print(10/1)
print(5+5*2)

try:
    num = int(input("Enter number: "))
    print(f"Ти ввів {num}")
except ValueError:
    print("Ви ввели не число, а щось інше.")"""

"""try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
except ValueError:
    print("Ви ввели не число, а щось інше.")
else:
    print(a+b)
finally:
    print("Цей код виконався незалежно від помилки.")"""

"""import tkinter as tk

def my_func():
    button.config(text="Ви натиснули на мене")

def func2():
    label.config(font=("Calibri",25), fg="red")

def func3():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()


root = tk.Tk()
root.title("Наша перша програма")
root.geometry("600x600")
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
label = tk.Label(frame1, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
button = tk.Button(root, text="Click me!", command=my_func)
button.pack()
button2 = tk.Button(root,text="Змінити колір напису", command=func2)
button2.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func3)
button3.pack()


root.mainloop()"""

"""import tkinter as tk
import random

def on_click(event):
    label.config(text= "Мене натиснуто!")

def change_backgroung_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    root.config(bg=random.choice(colors))

root = tk.Tk()
label = tk.Label(root, text="Натисни на мене", bg="lightblue")
label.pack(padx=20, pady=20)
label1 = tk.Label(root, text="Натисни на Enter, щоб знімити колір фону", bg="lightblue")
label1.pack(padx=20, pady=40)
root.bind("<Return>", change_backgroung_color)

label.bind("<Button-3>", on_click)
root.mainloop()"""


#Autoclicker
"""import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import mouse


def start_clicker():
# тут буде запуск клікера
    global running, delay
    clicks_per_second = int(entry.get())
    delay = 1/clicks_per_second
    messagebox.showinfo("Auto Clicker", "Auto Clicker started. Click 'ESC' to stop.")
    running = True
    schedule_click()

def schedule_click():
    if running:
        mouse.click()
        time.sleep(delay)
        schedule_click()

def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker","Auto Cliker stopped.")
    root.destroy()

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.configure(bg="#e0f7fa")
root.bind('i', show_info)
running = False
delay = 0
# Label: назва
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Add some padding

# Label: кліки на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#e0f7fa", fg="#00796b")
label.pack(pady=5)

# Entry для кількості кліків
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30))

# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10)

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey("esc", exit_app)

root.mainloop()"""

"""import customtkinter as ctk

def button_pressed():
    print("Кнопка натиснута")

app = ctk.CTk()
app.title("First custom app")
button = ctk.CTkButton(app, text="Click me", command=button_pressed)
button.pack(pady=20)

app.mainloop()"""

#Converter

"""import customtkinter as ctk

BTC_TO_UAH = 4119907.27
ETH_TO_UAH = 151023.61
USDT_TO_UAH = 42.12

def convert():
    amount = float(entry_amount.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

# Якщо конвертуємо з криптовалюти в UAH
    if from_currency == "BTC":

        amount_in_uah = amount * BTC_TO_UAH

    elif from_currency == "ETH":

        amount_in_uah = amount * ETH_TO_UAH

    elif from_currency == "USDT":

        amount_in_uah = amount * USDT_TO_UAH

    elif from_currency == "UAH": # Якщо конвертуємо з гривні

        amount_in_uah = amount

# Якщо конвертуємо з UAH у криптовалюту
    if to_currency == "BTC":

        converted_amount = amount_in_uah / BTC_TO_UAH

    elif to_currency == "ETH":

        converted_amount = amount_in_uah / ETH_TO_UAH

    elif to_currency == "USDT":

        converted_amount = amount_in_uah / USDT_TO_UAH

    elif to_currency == "UAH": # Якщо конвертуємо в гривні

        converted_amount = amount_in_uah

# Оновлюємо результат
    result_label.configure(text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}")

app = ctk.CTk()
app.title("Конвертер криптовалют")
app.geometry("400x300")
# Заголовок
title_label = ctk.CTkLabel(app, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

# Поле для вводу суми
entry_amount = ctk.CTkEntry(app, placeholder_text="Введи суму")
entry_amount.pack(pady=10)

# Вибір валюти для конвертації з
from_currency_var = ctk.StringVar(value="BTC")
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
from_currency_menu.pack(pady=5)

# Вибір валюти для конвертації в
to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu = ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
to_currency_menu.pack(pady=5)

convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

# Результат конвертації
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

# Запуск програми
app.mainloop()"""

"""try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("На жаль ти ввів не число!")
else:
    print("Ти молодець, ввів все без помилок ось результат")
    print(f"Сума чисел які ти ввів: {num1+num2}")
finally:
    print("Я виконуюсь завжди!")

#2
import math
try:
    number = int(input("Введіть додатнє число: "))
    if number < 0:
        raise ValueError("Неможливо обчислити квадратний корінь від'ємного числа")
except ValueError as e:
    print(f"Помилка: {e}")
else:
    print(f"Квадратний корінь з {number} = {math.sqrt(number)}")
finally:
    print("Дякуємо за звернення!")"""


#menu
"""import tkinter as tk
# Створюємо головне вікно
root = tk.Tk()
root.title("Miй додаток")
# Створюємо меню
menubar= tk.Menu(root)
# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Вiдкрити")
file_menu1.add_command(label="36еpeгти")
file_menu1.add_command(label="Вийти", command=root.quit)
# Додаємо другий пункт меню
file_menu2=tk.Menu (menubar, tearoff=0) 
file_menu2.add_command(label="Koпiвaти")
file_menu2.add_command(label="Вирiзати") 
file_menu2.add_command(label="Вставити")
# Додаємо два підменю в головне меню
menubar.add_cascade(label="Фaйл", menu=file_menu1)
menubar.add_cascade(label="Pедагувати", menu=file_menu2)
# Додаємо головне меню у вікно
root.config(menu=menubar)
root.mainloop()"""

#color menu

"""import tkinter as tk

# Функції для зміни кольору фону
def change_to_red():
    root.config(bg="red")
def change_to_blue():
    root.config(bg="blue")
def change_to_green():
    root.config(bg="green")
def change_to_yellow():
    root.config(bg="yellow")
def change_to_purple():
    root.config(bg="purple")
def change_to_orange():
    root.config(bg="orange")
# Головне вікно
root = tk.Tk()
root.title("Додаток художника")
root.geometry("400x400")
# Створюємо меню
menubar = tk.Menu(root)
# Створюємо підменю
color_menu = tk.Menu(menubar, tearoff=0)
color_menu.add_command(label="Червоний", command=change_to_red)
color_menu.add_command(label="Синій", command=change_to_blue)
color_menu.add_command(label="Зелений", command=change_to_green)
color_menu.add_command(label="Жовтий", command=change_to_yellow)
color_menu.add_command(label="Фіолетовий", command=change_to_purple)
color_menu.add_command(label="Помаранчевий", command=change_to_orange)
# Додаємо підменю в головне меню
menubar.add_cascade(label="Вибір кольору", menu=color_menu)
# Додаємо головне меню до вікна
root.config(menu=menubar)
root.mainloop()"""


"""import tkinter as tk
# Головне вікно
# Функції для кнопок 
def new_file():
    print("Створено новий файл!")
def save_file():
    print("36epeжено!")
def open_file():
    print("Відкрито!")
def cut_text():
    print("Вирізано текст!")
def copy_text():
    print("Скопійовано текст!")
def paste_text():
    print("Вставлено текст!")
root = tk.Tk()
root.title("Простий редактор з панеллю інструментів") 
root.geometry("400x400")
# Створюємо фрейм для панелі інструментів 
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
# Кнопка "Нове"
new_button = tk.Button(toolbar, text="Hoвe", command=new_file) 
new_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Зберегти"
save_button = tk.Button(toolbar, text="36еpeгти", command=save_file) 
save_button.pack (side=tk.LEFT, padx=2, pady=2)
# Кнопка "Відкрити"
open_button = tk.Button(toolbar, text="Вiдкрити", command=open_file) 
open_button.pack(side=tk. LEFT, padx=2, pady=2)
# Кнопка "Вирізати"
cut_button= tk. Button (toolbar, text="Bиpiзати", command=cut_text) 
cut_button.pack (side=tk. LEFT, padx=2, pady=2)
# Кнопка "Копіювати"
copy_button= tk.Button(toolbar, text="Koniвати", command=copy_text) 
copy_button.pack (side=tk. LEFT, padx=2, pady=2)
# Кнопка "Вставити"
paste_button = tk.Button(toolbar, text="Вставити", command=paste_text) 
paste_button.pack (side=tk. LEFT, padx=2, pady=2)
#Відображаємо панель інструментів 
toolbar.pack(side=tk.TOP, fill=tk.X)
# Основний контент
content = tk.Text(root)
content.pack (expand=1, fill=tk.BOTH)
root.mainloop()"""


#calculator 3.6


import tkinter as tk

current_expression = ""
def on_button_click(button):
    global current_expression

    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)

    elif button == "=":
        try:
            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)

        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""
    else:
            current_expression += str(button)
            display.delete(0, tk.END)
            display.insert(0, current_expression)

def set_theme(theme):
    if theme == "light":
        root.config(bg="white")
        display.config(bg = "lightgray", fg = "black")
    elif theme =="dark":
        root.config(bg="black")
        display.config(bg = "gray", fg = "white")
    for button in buttons:
        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', 
                        fg='black' if theme != "dark" else 'white')

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")

display = tk.Entry(root, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = []
button_texts = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+','(',')'
]

row_val = 1
col_val = 0
# Створюємо кнопки:
for text in button_texts:

    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# МЕНЮ
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
menubar.add_cascade(label="Налаштування", menu=theme_menu)
root.config(menu=menubar)
root.mainloop()

#1
"""expression = input("Введи математичний вираз: ")
result = eval(expression)
print(f"Результат: {result}")"""

"""while True:
    expression = input("Введи математичний вираз (або 'вихід' для завершення): ")
    if expression.lower() == "вихід":
        break
    result = eval(expression)
    print(f"Результат: {result}")"""

"""
import tkinter as tk

def my_func():
    button.config(text="Ви натиснули на мене")

def func2():
    label.config(font=("Calibri",25), fg="red")

def func3():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()


root = tk.Tk()
root.title("Наша перша програма")
root.geometry("600x600")
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
label = tk.Label(frame1, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
button = tk.Button(root, text="Click me!", command=my_func)
button.pack()
button2 = tk.Button(root,text="Змінити колір напису", command=func2)
button2.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func3)
button3.pack()


root.mainloop()
"""

#3.1

"""import tkinter as tk

def my_func():
    label.config(fg="red")
    button.config(text="Ви натиснули на мене", fg="red")

def func2():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()

root = tk.Tk()

root.geometry("600x600")
root.title("Наша перша програма")
label = tk.Label(root, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
button = tk.Button(frame1, text="Click me!", command=my_func)
button.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func2)
button3.pack()

root.mainloop()"""

#3.2
"""from tkinter import Tk, Label
root = Tk()
my_label = Label(root, text="Hello!", font=("Arial", 16), fg = "blue", padx = 100, pady=200)
my_label.pack()
root.mainloop()"""
#pack
"""from tkinter import Tk, Label, Button

root = Tk()
root.title("GUI з Pack")

header = Label(root, text="Вітаємо у веселому GUI!", bg="lightblue", fg="white", font=("Arial", 20), padx=10, pady=10)
header.pack(side="top", fill="x")

instruction = Label(root, text="Я Верхній рядочок", bg="lime", fg="black", font=("Arial", 14), padx=20, pady=10)
instruction.pack(side="top", fill="x", padx=10, pady=10)

left_button = Button(root, text="Я Ліва кнопка", bg="orange", fg="white", font=("Arial", 12), padx=20, pady=10)
left_button.pack(side="left", fill="y", expand=True, padx=10, pady=10)

right_button = Button(root, text="Я Права кнопка", bg="purple", fg="white", font=("Arial", 12), padx=20, pady=10)
right_button.pack(side="right", fill="y", expand=True, padx=10, pady=10)

status = Label(root, text="А я Нижній рядок", bg="yellow", fg="black", font=("Arial", 12), padx=20, pady=10)
status.pack(side="bottom", fill="x")

root.mainloop()"""

"""x= 10
func1 = lambda x: x*10
print(func1(x))

#telegram

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4'
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
# Створення клавіатури
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)

# Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)


# Запуск бота
bot.polling()"""


"""import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4')
# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)

    # Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

# Обробка текстових повідомлень (реакція на кнопки)
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help")
@bot.message_handler(commands=["telljoke"])
def tell_joke(message):
    bot.reply_to(message, "ТУТ МАВ БУТИ ЖАРТ. АХАХАХАХ")
@bot.message_handler(commands=["info"])
def tell_joke(message):
    bot.reply_to(message, "Я — бот, який допомагає з програмуванням і вміє жартувати!")
@bot.message_handler(commands=["random"])
def random_message(message):
    a = random.randint(1,10)
    bot.reply_to(message, f"Random number {a}")


#from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
    elif message.text == "Почати":
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("Відкрити сайт середовища для програмування", url="https://codehs.com/")
        button2 = InlineKeyboardButton("Відкрити сайт школи", url="https://justschool.me/uk")
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, "Обери дію:", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я не знаю такої команди, спробуй натиснути на кнопку 😊")


bot.polling()"""


"""import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
# Створюємо клавіатуру з темами
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Планети", callback_data="planets")
    button2 = InlineKeyboardButton("Зорі", callback_data="stars")
    button3 = InlineKeyboardButton("Чорні діри", callback_data="black_holes")
    keyboard.add(button1, button2, button3)
# Відправляємо повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери тему, щоб дізнатися цікавий факт про космос:", reply_markup=keyboard)
# Обробляємо вибір теми
@bot.callback_query_handler(func=lambda call: True)
def handle_topic_selection(call):
    if call.data == "planets":
        bot.send_message(call.message.chat.id, "Факт: Юпітер настільки великий, що міг би вмістити понад 1300 планет Земля!")
    elif call.data == "stars":
        bot.send_message(call.message.chat.id, "Факт: Сонце – це зірка, яка вміщує 99,86% маси всієї Сонячної системи.")

    elif call.data == "black_holes":

        bot.send_message(call.message.chat.id, "Факт: Якщо б ти потрапив у чорну діру, то розтягнувся б, як спагетті.")

# Пропонуємо повернутися до вибору
    bot.send_message(call.message.chat.id,"Хочеш дізнатися ще щось? Напиши /start, щоб повернутися до меню!")

bot.polling()"""

"""import time
import schedule
def remainder():
    print("Нагадування час зробити перерву!")

schedule.every(5).seconds.do(remainder)
while True:
    schedule.run_pending()
    time.sleep(1)"""


"""import telebot
import schedule
import time

# Токен бота
TOKEN = "7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4"
bot = telebot.TeleBot(TOKEN)

# ID користувача
CHAT_ID = 8086768572 # Введи ID чату (@userinfobot)

# Налаштування розкладу
def send_reminder():
    bot.send_message(CHAT_ID, "Час зробити важливу справу!")

# Заплановані нагадування
schedule.every().day.at("09:00").do(send_reminder)
schedule.every().day.at("18:00").do(send_reminder)
schedule.every(10).seconds.do(send_reminder)

# Основний цикл
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)
"""
#method split
#1
"""text = "Hello world!"
print(text)
text = text.split(" ")
print(text)

students = "Андрій, Олена, Микола, Світлана, Юлія, Дмитро"
students_list = students.split(", ")
print(students_list)
com1 = students_list[0:3]
com2 = students_list[3:6]
print(com1)
print(com2)
#2
dates = "25.12.2021, 01.01.2020, 5.15.2023"
dates_list = dates.split(", ")
print(dates_list)
years = []
for date in dates_list:
    year = date[-4:]
    years.append(year)

print(years)
#3
url = "https://example.com?page=5&sort=asc&filter=new"
query = url.split("?")[1]
print(query)
params = query.split("&")
print(params)
for i in params:
    print(i)"""

"""import telebot
TOKEN = '7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4'
# Встав токен, який надіслав BotFather
bot = telebot.TeleBot(TOKEN)
chat_id = 8086768572 # Введи ID чату (@userinfobot)

def convert_unit(value, from_units, to_units):
    conversions ={
        "чашки": {"мілілітри":240},
        "столових_ложок": {"мілілітри": 15},
        "чайних_ложок": {"мілілітри":5},
        "склянки": {"мілілітри":250}
    }
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None 
@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Привіт! Я допоможу тобі конвертувати задану кількість чашок, ложок, склянок у мілілітри.\
        \nНапиши в такому форматі: 5 чашки в мілілітри.")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]
        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "перепрошую, спробуйте ще раз")
    except Exception as e:
        bot.send_message(message.chat.id, "Все погано у тебе помилка в коді!")
bot.polling()"""
"""
 parts = ["2 столових_ложок", "мілілітри"]
 value_and_from_unit = ["2", "столових_ложок"]
 to_unit = "мілілітри"
 value = 2.00
 from_unit = "столових_ложок"




"""


"""import telebot
import random

TOKEN = '7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4'
bot = telebot.TeleBot(TOKEN)

# Шлях до папки, де зберігаються меми
UPLOAD_FOLDER = r"C:\memes/"
#C:\memes + /

# Список, де ми зберігатимемо назви файлів з мемами
memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", 
         "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg"]

@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Вітаю тебе в мем-боті. Ось команди які доступні: /meme, /photo, /count")
@bot.message_handler(content_types=['photo'])
def receive_meme(message):
# Дістаємо інформацію про надісланий файл із мемом
    file_info = bot.get_file(message.photo[-1].file_id)
# Завантажуємо файл з мемом
    downloaded_file = bot.download_file(file_info.file_path)
# Зберігаємо мем на комп'ютері під унікальним іменем   c:memes/"21.jpg"
    file_name = str(len(memes) + 1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
# Додаємо назву мема в список memes
    memes.append(file_name)
    bot.reply_to(message, "Мем отримано і збережено!")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        
    else:
        bot.reply_to(message, "Мемів поки немає :(")

@bot.message_handler(commands=['count'])
def meme_count(message):
    if memes:
        memes_count = len(memes)
        bot.reply_to(message, f"Додано мемів: {memes_count}")
    else:
        bot.reply_to(message, "Мемів не знайдено!")

bot.polling()"""


"""import telebot
import requests
TELEGRAM_BOT_TOKEN = "7926689322:AAEfLRdA9T68pbC2LbbmhpcpDr_aTCMsxts"
COHERE_API_KEY = "tVr39gH3rv4KliCVInUmdgMC5T7C1xhV0xNZWKRl"
COHERE_API_URL = "https://api.cohere.ai/generate"
RESPONSE_MODE = "коротко"
RESPONSE_STYLE = "серйозний"
#chat_id = 8086768572

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
# Функція для генерації тексту через Cohere API
def generate_text(prompt):
    if RESPONSE_STYLE == "жартівливий":
        prompt = f"Зроби цю відповідь веселою: {prompt}"
        # Стиль "серйозний" нічого не змінює в prompt
        data = {
            "model": "command-xlarge-nightly",
            "prompt": prompt,
            "max_tokens": 150,
        }
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",
    }
    max_tokens = 50 if RESPONSE_MODE == "коротко" else 150
    data = {
    "model": "command-xlarge-nightly", # Використовується модель для генерації тексту
    "prompt": prompt,
    "max_tokens": max_tokens, # Максимальна кількість токенів
    }
    try:
        response = requests.post(COHERE_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json() 
            generation = response_data["text"]
            return generation
    except Exception as e:
        return f"Помилка: {e}"
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши мені текст, і я спробую продовжити його за допомогою Cohere API.")

@bot.message_handler(commands=["mode"])
def select_mode(message):
    bot.reply_to(message, "Обери режим відповіді: коротко або детально.")
    bot.register_next_step_handler(message, set_mode)

def set_mode(message):
    global RESPONSE_MODE
    if message.text.lower() == "коротко":
        RESPONSE_MODE = "коротко"
        bot.reply_to(message, "Режим встановлено: коротка відповідь.")
    elif message.text.lower() == "детально":
        RESPONSE_MODE = "детально"
        bot.reply_to(message, "Режим встановлено: детальна відповідь.")
    else:
        bot.reply_to(message, "Невідомий режим. Спробуйте ще раз.")

@bot.message_handler(commands=["style"])
def select_style(message):
    bot.reply_to(message, "Обери стиль відповіді: жартівливий або серйозний.")
    bot.register_next_step_handler(message, set_style)
def set_style(message):
    global RESPONSE_STYLE
    if message.text.lower() == "жартівливий":
        RESPONSE_STYLE = "жартівливий"
        bot.reply_to(message, "Стиль встановлено: жартівливий.")
    elif message.text.lower() == "серйозний":
        RESPONSE_STYLE = "серйозний"
        bot.reply_to(message, "Стиль встановлено: серйозний.")
    else:
        bot.reply_to(message, "Невідомий стиль. Спробуйте ще раз.")

# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot.reply_to(message, "Генерую відповідь, зачекайте...")
    generated_text = generate_text(user_input)
    bot.send_message(message.chat.id, generated_text)

if __name__ == "__main__":
    print("Бот запущено!")
    bot.polling()
"""

"""import pygame
import random
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((500, 400)) # Ширина 400, висота 300
pygame.display.set_caption("Мене звати Дмитро")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN: # Якщо натиснута клавіша Enter
                random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                screen.fill(random_color)
        pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()"""

"""import telebot
import random

bot = telebot.TeleBot("7990794814:AAH2MEvNZu0g-T43fdXJFwkgJTAz4wSBnsM")
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Я твій створений бот!")

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help")

@bot.message_handler(commands=["telljoke"])
def tell_joke(message):
    bot.reply_to(message, "Програміст - це людина, яка спочатку довго думає, щоб потім нічого не робити.")

@bot.message_handler(commands=["info"])
def tell_joke(message):
    bot.reply_to(message, "Я — бот, який допомагає з програмуванням і вміє жартувати!")

@bot.message_handler(commands=["random"])
def random_message(message):
    a = random.randint(1,10)
    bot.reply_to(message, f"Random number {a}")

bot.polling()
"""
#vector2
"""import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")
rect_position = pygame.math.Vector2(100,100)
object_size = 50
object_color = (255,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rect_position.x +=50
                rect_position.y +=20
    screen.fill((255,255,255))
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))
    pygame.display.flip()
pygame.quit()"""


"""import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
t = 0 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.time.get_ticks() - t > 2000:
            print("Час іде....")
            t = pygame.time.get_ticks()"""


#AIM_TRAINER
"""import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
WHITE = (255,255,255)
RED = (255,0,0)

x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30
font = pygame.font.SysFont("Arial",30)
start_time = pygame.time.get_ticks()
last_move_time = 0
MOVE_INTERVAL = 1000
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x -x)**2 + (mouse_y -y)**2)**0.5
            if distance <=  RADIUS:
                score+=1
                print("Є влучання!")
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= MOVE_INTERVAL:
        x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = current_time
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)
    score_text = font.render(f"Влучань: {score}", True, (0,0,0))
    screen.blit(score_text,(10,10)) 
    elapsed_time = (current_time - start_time)//1000
    time_text = font.render(f"Час: {elapsed_time} c", True, (0,0,0))
    screen.blit(time_text,(10,40))
    pygame.draw.rect(screen, (0,255,0), (0,0,500,500),10)
    pygame.display.flip()
pygame.quit()"""

"""import pygame

# Ініціалізація Pygame
pygame.init()
# Налаштування екрану
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Програма з текстом")
# Кольори
WHITE = (255, 255, 255)
# Шрифт
font = pygame.font.SysFont("Arial", 36)
# Текст
text = font.render("Привіт, світe!", True, (0, 0, 0))
# Основний цикл гри
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
# Очищаємо екран
    screen.fill(WHITE)
# Виводимо текст на екран
    screen.blit(text, (150, 200))
# Оновлюємо екран
    pygame.display.flip()
# Завершуємо роботу Pygame
pygame.quit()"""

#request
"""import requests

# URL для отримання випадкового питання
url = "https://opentdb.com/api.php?amount=1&type=multiple&category=9"

# Надсилаємо GET-запит до API
response = requests.get(url)
# Перевіряємо, чи запит успішний
if response.status_code == 200:
    question_data = response.json() # Отримуємо дані у форматі JSON
    question = question_data['results'][0]['question'] # Питання
    correct_answer = question_data['results'][0]['correct_answer'] # Правильна відповідь
    incorrect_answers = question_data['results'][0]['incorrect_answers'] # Неправильні відповіді
# Виводимо питання та варіанти відповідей
    print(f"Question: {question}")
    answers = incorrect_answers + [correct_answer]
# Виводимо варіанти відповідей без використання enumerate
    i = 1
    for answer in answers:
        print(f"{i}. {answer}")
        i += 1
# Виводимо правильну відповідь (для перевірки)
    print(f"Correct answer: {correct_answer}")
else:
    print("Не вдалося отримати питання. Спробуйте ще раз.")"""

#CoHere Api part 1

"""import telebot 
import requests

TELEGRAM_BOT_TOKEN = "7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4"

COHERE_API_KEY = "aQst2PUunZmgwUrawtfCPVzuawAhImOyFU0KKotM"
COHERE_API_URL = "https://api.cohere.ai/generate"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "command-xlarge-nightly", # Використовується модель для генерації тексту
        "prompt": prompt,
        "max_tokens": 100, # Максимальна кількість токенів
    }
    try:
        response = requests.post(COHERE_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            if "generations" in response_data and len(response_data["generations"]) > 0:
                generation = response_data["generations"][0]["text"]
                return generation
            else:
                return "Помилка: пустий результат від API."
        else:
            return f"Помилка: {response.status_code}"
    except Exception as e:
        return f"Помилка: {e}"
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши мені текст, і я спробую продовжити його за допомогою Cohere API.")

# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot.reply_to(message, "Генерую відповідь, зачекайте...")
    generated_text = generate_text(user_input)
    bot.send_message(message.chat.id, generated_text)
if __name__ == "__main__":
    print("Бот запущено!")
    bot.polling()"""

"""import telebot
import requests

TELEGRAM_BOT_TOKEN = "7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4"

COHERE_API_KEY = "tVr39gH3rv4KliCVInUmdgMC5T7C1xhV0xNZWKRl"
COHERE_API_URL = "https://api.cohere.ai/generate"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Функція для генерації тексту через Cohere API
def generate_text(prompt):
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",
        }
    data = {
        "model": "command-xlarge-nightly", # Використовується модель для генерації тексту
        "prompt": prompt,
        "max_tokens": 100, # Максимальна кількість токенів
        }
    try:
        response = requests.post(COHERE_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            generation = response_data["text"]
            return generation
    except Exception as e:
        return f"Помилка: {e}"

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши мені текст, і я спробую продовжити його за допомогою Cohere API.")
# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot.reply_to(message, "Генерую відповідь, зачекайте...")
    generated_text = generate_text(user_input)
    bot.send_message(message.chat.id, generated_text)

if __name__ == "__main__":
    print("Бот запущено!")
    bot.polling()"""

"""import pygame
# Ініціалізуємо Pygame
pygame.init()
# Зберігаємо у змінних розміри вікна (ширина, висота)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Зберігаємо у змінній основний колір фону (RGB)
background_color = (135, 206, 250) # Небесно-блакитний
# Створюємо вікно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Встановлюємо назву вікна
pygame.display.set_caption("Моя перша гра")
# Заповнюємо фон кольором
screen.fill(background_color)
# Оновлюємо дисплей
pygame.display.flip()
# Затримка перед виходом
pygame.time.delay(5000)"""

"""import pygame
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((400, 300)) # Ширина 400, висота 300
pygame.display.set_caption("Мій перший ігровий цикл")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN: # Якщо натиснута клавіша Enter
                running = False
# Очищуємо екран заданим кольором
    screen.fill(background_color)
# Оновлюємо екран
    pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()"""

"""import pygame
import random
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((500, 400)) # Ширина 400, висота 300
pygame.display.set_caption("Мене звати Дмитро")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN: # Якщо натиснута клавіша Enter
                random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                screen.fill(random_color)
        pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()"""

"""import telebot 
import cohere

API_KEY = "tVr39gH3rv4KliCVInUmdgMC5T7C1xhV0xNZWKRl"
co = cohere.Client(API_KEY)
bot = telebot.TeleBot("7892012324:AAER0jO7XAqDBAuVvKwjkg6q77FX2qvsRJ4")

@bot.message_handler(func = lambda message: True)
def handle_message(message):
    text = message.text
    try:
        response = co.summarize(
            text = text,
            length="auto",
            model="summarize-xlarge",
            additional_command="",
            temperature=0.3,
        )
        summary = response.summary
        bot.reply_to(message,summary)
    except Exception as e:
        print("ERROR: ", str(e))
        bot.reply_to(message,"Opps! Something went wrong.")

bot.polling()"""


#vector
#1
"""import pygame

# Створюємо об'єкт Vector2 для позиції (100, 150)
position = pygame.math.Vector2(100, 150)
# Виведемо координати позиції
print(f"X: {position.x}, Y: {position.y}")

#2
import pygame
# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
# Створення об'єкта: прямокутник
rect_position = pygame.math.Vector2(300, 100) # Початкова позиція
# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Очищуємо екран
        screen.fill((255, 255, 255))
# Малюємо прямокутник
        pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))
# Оновлення екрана
        pygame.display.flip()
pygame.quit()

#3
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")
rect_position = pygame.math.Vector2(100,100)
object_size = 100
object_color = (255,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rect_position.x +=50
                rect_position.y +=20
    screen.fill((255,255,255))
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))
    pygame.display.flip()
pygame.quit()"""


#events

"""import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Хтось натиснув стрілочку вгору!")
            elif event.key == pygame.K_DOWN:
                print("Хтось натиснув стрілочку вниз!")
            elif event.key == pygame.K_s:
                print("s")
            elif event.key == pygame.K_w:
                print("W")
            elif event.key == pygame.K_a:
                print("A")
            elif event.key == pygame.K_SPACE:
                print("Space")
            elif event.key ==pygame.K_LSHIFT:
                print("LEFT SHIFT")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Хтось відпустив стрілочку вгору!")
            
pygame.quit()

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
# Виведення інформації про натиснуту клавішу
        if keys[pygame.K_LEFT]:
            message = "Клавіша ліворуч натиснута"
            print(message)
        elif keys[pygame.K_RIGHT]:
            message = "Клавіша праворуч натиснута"
            print(message)
        elif keys[pygame.K_UP]:
            message = "Клавіша вгору натиснута"
            print(message)
        elif keys[pygame.K_DOWN]:
            message = "Клавіша вниз натиснута"
            print(message)
            
pygame.quit()

#events

import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# Кольори
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)
# Початкові координати квадратика
x, y = 300, 200
width, height = 50, 50
speed = 5 # Швидкість руху квадратика
# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Отримання стану клавіш
    keys = pygame.key.get_pressed()
# Рух квадратика
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: # Ліворуч
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # Right
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]: # UP
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: # Ліворуч
        y += speed
# Очищення екрану
    screen.fill(YELLOW)
# Малюємо квадратик
    pygame.draw.rect(screen, GREEN, (x, y, width, height))
# Оновлення екрану
    pygame.display.update()
# Кадри на секунду
    clock.tick(60)"""

"""import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)
# Завантаження зображення кота та фону
cat_img = pygame.image.load("bird.png") # Завантажуємо зображення кота
cat_img = pygame.transform.smoothscale(cat_img, (50, 50)) # Використовуємо smoothscale для кращої якості
cat = cat_img.get_rect() # Отримуємо розміри зображення кота
cat.topleft = (100, 100) # Встановлюємо початкову позицію кота
# Завантаження фону
background_img = pygame.image.load("background.png") # Завантажуємо фонове зображення
background_img = pygame.transform.scale(background_img, (800, 600)) # Масштабуємо його під розмір екрану
# Параметри швидкості, вони знадобляться пізніше
speed = 0 # Початкова вертикальна швидкість (кіт стоїть на місці)
gravity = 0.5 # Значення нашої сили тяжіння
jump_speed = -8 # Швидкість стрибка (зверни увагу, що вона від'ємна, бо напрямлена вгору)

obstacle_timer = 0
obstacles = [] #Перешкоди
obstacle_width = 50
gap_height = 150 # Збільшена відстань між верхньою та нижньою перешкодами
min_distance = 250 # Мінімальна горизонтальна відстань між перешкодами
score = 0
font = pygame.font.Font(None, 36)
# Основний цикл
while True:
    screen.blit(background_img, (0, 0)) # Малюємо фонове зображення на екрані
# Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed
    speed += gravity
    cat.y += speed
    if cat.y > 500:
        cat.y = 550
        speed = 0
        pygame.quit()
    if cat.y < -70:
        cat.y = 550
        speed = 0
        pygame.quit()
    obstacle_timer += 1
    if obstacle_timer > min_distance:
        top_obstacle_height = random.randint(100,400)
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height # Регулюємо висоту нижньої перешкоди
        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)
        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width, bottom_obstacle_height)
        obstacles.append((top_obstacle, bottom_obstacle))
        obstacle_timer = 0 # Скидаємо таймер після спавну нової перешкоди
    # Переміщаємо перешкоди та перевіряємо на зіткнення
    for top_obstacle, bottom_obstacle in obstacles:
        top_obstacle.x -= 5 # Переміщаємо перешкоду вліво
        bottom_obstacle.x -= 5 # Переміщаємо нижню перешкоду вліво
        if cat.colliderect(top_obstacle) or cat.colliderect(bottom_obstacle):
            print("Game Over!")
            print(f"Кількість очок: {score}")
            pygame.quit()
            exit()
        if top_obstacle.x < -obstacle_width: # Видаляємо перешкоду, якщо вона вийшла за межі екрану
            score += 1
            obstacles.remove((top_obstacle, bottom_obstacle))

    # Малюємо кота
    screen.blit(cat_img, cat.topleft)
    for top_obstacle, bottom_obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, top_obstacle) # Верхня перешкода
        pygame.draw.rect(screen, GREEN, bottom_obstacle) # Нижня перешкода
# Оновлюємо екран
    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
# Оновлюємо частоту кадрів
    clock.tick(60)"""

"""import os

if not os.path.exists("SecretFolder"):
    os.mkdir("SecretFolder")
with open("SecretFolder/secret.txt", "w") as file:
    file.write("Це таємний файл")
print("Таємний сховок створено")

if os.path.exists("secret.txt"):
    print(f"Файл {"secret.txt"} успішно створено в {"SecretFolder"}!")
else:
    print("Помилка: файл не створено.")


films = "фільм 1, фільм 2, фільм 3"
with open("text.txt", "w") as file:
    file.write(films)
    print("Фільми записані у файл")

with open("write.txt", "r") as file:
    text = file.readline()
    print(text)"""
    

#6.2

"""import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('my_database2.db')
# Створення курсора
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
               
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
''')

# Вставка одного запису
cursor.execute("INSERT INTO users (name, age) VALUES ('Dmytro', 50)")
# Підтвердження змін
conn.commit()

# Перевірка результату (вибірка всіх записів)
cursor.execute("SELECT * FROM users")
print(cursor.fetchall()) # Вивести всі записи з таблиці

# Закриття з'єднання
conn.close()"""


"""import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('my_database.db')
# Створення курсора
cursor = conn.cursor()
# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
''')

# Вставка одного запису
#cursor.execute("INSERT INTO users (name, age) VALUES ('Klice', 88)")
# Підтвердження змін
conn.commit()
cursor.execute("SELECT name, age FROM users WHERE age > 40")
print(cursor.fetchall())
cursor.execute("SELECT id,name, age FROM users WHERE name LIKE '__i%'")
print(cursor.fetchall()) # Вивести всі записи з таблиці
cursor.execute("SELECT id,name, age FROM users WHERE name LIKE 'K%'")
print(cursor.fetchall()) # Вивести всі записи з таблиці

# %слово, яке треба знайти%
# Закриття з'єднання
conn.close()"""


"""import sqlite3
conn = sqlite3.connect('my_database1.db')
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS library (

id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year INTEGER
)
''')

cursor.execute("INSERT INTO library (title, author, year) VALUES ('Book1', 'Author 1', 1990)")
cursor.execute("INSERT INTO library (title, author, year) VALUES ('Book2', 'Author 2', 2000)")
cursor.execute("INSERT INTO library (title, author, year) VALUES ('Book3', 'Author 3', 2010)")
conn.commit()
cursor.execute("SELECT * FROM library")
print(cursor.fetchall()) # Вивести всі записи з таблиці

# Закриття з'єднання
conn.close()"""

#6.3
"""import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('my_database.db')
# Створення курсора
cursor = conn.cursor()
# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (

id INTEGER PRIMARY KEY AUTOINCREMENT,
dish_name TEXT,
category TEXT,
price INT,
available TEXT
)
''')
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('pasta', 'main_dish', 45, 'YES')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('ice-cream', 'desert', 50, 'YES')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('pizza', 'main_dish', 150, 'NO')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('potato', 'main_dish', 5, 'YES')")
cursor.execute("INSERT INTO menu (dish_name, category, price, available) VALUES ('soup', 'soup', 60, 'NO')")

cursor.execute("SELECT dish_name, category,price,available FROM menu WHERE dish_name LIKE '%pasta%'")
print(cursor.fetchall()) # Вивести всі записи з таблиці
cursor.execute("SELECT dish_name, category,price,available FROM menu WHERE category LIKE '%main_dish%'")
print(cursor.fetchall())
cursor.execute("SELECT dish_name, category,price,available FROM menu WHERE price > 15 AND available LIKE '%YES%'")
print(cursor.fetchall())

# Закриття з'єднання
conn.close()"""

#6.4
"""import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('my_database.db')
# Створення курсора
cursor = conn.cursor()
# Створення таблиці (якщо її ще немає)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
''')

# Вставка одного запису
#cursor.execute("INSERT INTO users (name, age) VALUES ('Klice', 88)")
namep = input("Enter name:")
agep = int(input("Enter age: "))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",(namep,agep))
# Підтвердження змін
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall()) # Вивести всі записи з таблиці
cursor.execute("UPDATE users SET age  = 30 WHERE age < 30")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
cursor.execute("UPDATE users SET name = 'Ms.'|| name WHERE name LIKE 'A%'")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall()) 
cursor.execute("DELETE FROM users WHERE age >80")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall()) 
cursor.execute("DELETE FROM users WHERE name = 'Ms.Alice'")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall()) 
cursor.execute("DELETE FROM users")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
# Закриття з'єднання
conn.close()"""

#6.5
#1
"""import pandas as pd

df = pd.DataFrame({
    "Фільм": ["Інтерстеллар", "Матриця", "Дюна"],
    "Рейтинг": [8.6, 8.7, 8.0]

})
print(df)"""

#2
"""import pandas as pd

# Завантаження даних з файлу
df = pd.read_csv("movies_dataset.csv")

# Відобразимо перші 5 рядків
print(df)
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(subset=['wins', 'nominations']))"""

#6.6
"""import pandas as pd

# Завантаження даних з файлу
df = pd.read_csv("movies_dataset.csv")
print(df[df['Rating']<7][['Title','Year','Rating']])
print(df[df['grossWorldWide']>50000000])


print(df.groupby('genres')['Rating'].mean())
print(df.groupby('genres')['grossWorldWide'].mean())
print("---------------")
print(df.sort_values('Rating')[['Title', 'Rating']])
print("---------------/--*-*")
print(df.sort_values('Rating', ascending=False)[['Title', 'Rating']])
print(df.sort_values('Year').head(5)[['Title', 'Year']])
print(df[df['Year']==2003][['Title','Year','Rating']])

df2 = pd.read_csv("education.csv")
print(df2[df2['Year']==1950])
print(df2[df2['Share of population with at least some basic education']==0])
print(df2[df2['Entity']=="India"][['Year','Share of population with at least some basic education']])"""

#6.7
#1
"""import matplotlib.pyplot as plt

week_days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця', 'Субота', 'Неділя']
views = [0, 10, 42, 125, 379, 581, 1989]

plt.plot(week_days, views)  
plt.title("Приріст переглядів за тиждень")
plt.xlabel("День тижня")
plt.ylabel("Кількість переглядів")
plt.show()
#2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("education.csv")
brazil_data = df[df['Entity'] == 'Brazil']
plt.figure(figsize=(10,6))
plt.plot(brazil_data['Year'], brazil_data["Share of population with at least some basic education"], marker = 'o',color= 'b')
plt.title('Зміни частки населення з базовою освітою в Бразилії', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Частка населення з базовою освітою (%)', fontsize=12)
plt.grid(True)
plt.show()

#3
import matplotlib.pyplot as plt
# Назви категорій
categories = ['USA', 'India', 'China', 'Germany', 'UK']
# Числові значення для кожної категорії
values = [20, 15, 30, 10, 25]
# Створення графіку з різними кольорами для кожного стовпця
colors = ['red', 'blue', 'green', 'purple', 'orange']
plt.bar(categories, values, color=colors)
# Підписи до осей
plt.xlabel('Країни')
plt.ylabel('Значення')
plt.title('Порівняння кількості для різних країн')
# Показуємо графік
plt.show()

#4
import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv("billionaires.csv")
# Підрахунок кількості мільярдерів у кожній індустрії
industry_counts = df["Industry"].value_counts()
# Побудова стовпчастої діаграми
plt.figure(figsize=(12, 6))
plt.bar(industry_counts.index, industry_counts.values, color="gold")
# Оформлення графіку
plt.xlabel("Індустрія")
plt.ylabel("Кількість мільярдерів")
plt.title("Розподіл мільярдерів за індустріями")
plt.xticks(rotation=90) # Повертаємо підписи на осі X для зручності
# Показуємо графік
plt.show()

#5
import pandas as pd
import matplotlib.pyplot as plt
# Завантажуємо дані
df = pd.read_csv("billionaires.csv")
# Підраховуємо кількість мільярдерів у кожній індустрії
industry_counts = df["Industry"].value_counts()
# Беремо ТОП-5 індустрій, решту об'єднуємо в "Інші"
top_industries = industry_counts[:5]
top_industries["Інші"] = industry_counts[5:].sum()

# Будуємо кругову діаграму
plt.figure(figsize=(8, 8)) # Задаємо розмір
plt.pie(
top_industries,
labels=top_industries.index,
autopct="%1.1f%%", # Додаємо відсотки
colors=plt.cm.Paired.colors, # Встановлюємо кольори
startangle=140 # Повертаємо діаграму
)
plt.title("Розподіл мільярдерів за індустріями")
plt.show()"""


"""from lxml import etree

# Завантаження XML файлу
tree = etree.parse("lab.xml")
root = tree.getroot()

# Отримання всіх елементів <student>
students = root.xpath(".//student")

# Обробка кожного студента
for student in students:
    first_name = student.xpath("./name/first_name")[0].text
    last_name = student.xpath("./name/last_name")[0].text
    dob = student.xpath("./dob")[0].text

    print(f"Student: {first_name} {last_name}, DOB: {dob}")
    gender = input("Enter gender for this student: ")

    # Додавання нового елементу <gender>
    gender_elem = etree.Element("gender")
    gender_elem.text = gender
    student.append(gender_elem)

# Збереження зміненого XML у новий файл
tree.write("lab_5_new.xml", pretty_print=True, xml_declaration=True, encoding="UTF-8")"""


"""import kagglehub

# Download latest version
path = kagglehub.dataset_download("samithsachidanandan/1000-most-trending-youtube-videos")

print("Path to dataset files:", path)

import kagglehub

# Download latest version
path = kagglehub.dataset_download("orvile/brain-tumor-dataset")

print("Path to dataset files:", path)"""

#7.1
#1
"""def bubble_sort(arr):
    n = len(arr)# Проходимо по всіх елементах масиву
    for i in range(n):# Останні i елементів вже відсортовані
        for j in range(0, n-i-1):# Якщо поточний елемент більший за наступний, міняємо їх місцями
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Приклад використання
arr = [64, 34, 25, 12, 22, 11, 90]
print("Невідсортований список:", arr)
bubble_sort(arr)
print("Відсортований список:", arr)

#2
def insertion_sort(arr):
    # Проходимо по кожному елементу масиву, починаючи з другого
    for i in range(1, len(arr)):
        key = arr[i] # Зберігаємо поточний елемент для порівняння
        j = i - 1
# Переміщаємо елементи масиву, що більші за ключ, на одну позицію вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
# Вставляємо ключ в правильну позицію
        arr[j + 1] = key
    return arr

# Приклад використання
arr = [12, 11, 13, 5, 6]
print("До сортування:", arr)
sorted_arr = insertion_sort(arr)
print("Після сортування:", sorted_arr)"""



"""key = {
'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' ' # Пробіл залишимо без змін
}
def decrypt(encrypted_text,key):
    reverse_key = {v:k for k,v in key.items()}
    decrypted_text = ""
    for char in encrypted_text:
        if char in reverse_key:
            decrypted_text += reverse_key[char] #reverse_key["["]
        else:
            decrypted_text += char # Якщо символ не в зворотному ключі, залишаємо його незмінним
    return decrypted_text

encrypted_text = '[)@++ ! $-~=@}& <-; ]- @ [;~~&} %@<? <-; @}& ~-}& +-:&+< @`% ~-}& ]&~=&}@]&...'
decrypted = decrypt(encrypted_text, key)

print(f"Розшифрований текст: {decrypted}")"""

"""import customtkinter as ctk

# Створення словника для масонського шифру з клавіатурними символами
cipher_dict = {
'А': '@', 'Б': '#', 'В': '$', 'Г': '%', 'Ґ': '&',
'Д': '*', 'Е': '(', 'Є': ')', 'Ж': '+', 'З': '-',
'И': '=', 'І': '_', 'Ї': '{', 'Й': '}', 'К': '[',
'Л': ']', 'М': ':', 'Н': ';', 'О': "'", 'П': '"',
'Р': '|', 'С': '/', 'Т': '7', 'У': '~', 'Ф': '^',
'Х': '?', 'Ц': '!', 'Ч': '@', 'Ш': '#', 'Щ': '$',
'Ь': '%', 'Ю': '^', 'Я': '&'
}
# Функція для шифрування
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.upper() in cipher_dict:
            encrypted_text += cipher_dict[char.upper()]
        else:
            encrypted_text += char
    return encrypted_text
# Функція для розшифрування
def decrypt(text):
    decrypted_text = ""
    reverse_dict = {v: k for k, v in cipher_dict.items()}
    for char in text:
        if char in reverse_dict:
            decrypted_text += reverse_dict[char]
        else:
            decrypted_text += char
    return decrypted_text
# Функція для оновлення тексту
def update_text():
    input_text = text_input.get("1.0", "end-1c") # Отримуємо текст
    encrypted = encrypt(input_text) # Шифруємо
    text_output.delete("1.0", "end") # Очищаємо поле для виведення
    text_output.insert("1.0", encrypted) # Виводимо зашифрований текст
def decrypt_text():
    input_text = text_input.get("1.0", "end-1c") # Отримуємо текст
    decrypted = decrypt(input_text) # Розшифровуємо
    text_output.delete("1.0", "end") # Очищаємо поле для виведення
    text_output.insert("1.0", decrypted) # Виводимо розшифрований текст
# Створення вікна за допомогою customtkinter
root = ctk.CTk()
root.title("Масонський шифратор")
root.geometry("500x400")
# Текстове поле для введення
text_input = ctk.CTkTextbox(root, width=450, height=100)
text_input.pack(pady=20)
# Кнопки для шифрування та розшифрування
encrypt_button = ctk.CTkButton(root, text="Шифрувати", command=update_text)
encrypt_button.pack(pady=10)
decrypt_button = ctk.CTkButton(root, text="Розшифрувати", command=decrypt_text)
decrypt_button.pack(pady=10)
# Текстове поле для виведення результатів
text_output = ctk.CTkTextbox(root, width=450, height=100)
text_output.pack(pady=20)
# Запуск головного циклу
root.mainloop()"""

#lab 5
"""import random
from sympy import mod_inverse

# Генерація ключів
def generate_keys(p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Обчислення секретного ключа d
    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)  # Відкритий та закритий ключі

# Функція шифрування
def encrypt(message, pub_key):
    e, n = pub_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Функція дешифрування
def decrypt(encrypted_message, priv_key):
    d, n = priv_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Контрольний приклад
p = 53
q = 67
e = 1021

# Генерація ключів
pub_key, priv_key = generate_keys(p, q, e)

# Читаємо текстовий файл
file_name = "input.txt"
with open(file_name, "r", encoding="utf-8") as file:
    message = file.read()

# Шифрування
encrypted_message = encrypt(message, pub_key)

# Запис зашифрованих даних у файл
with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(' '.join(map(str, encrypted_message)))

# Дешифрування
decrypted_message = decrypt(encrypted_message, priv_key)

# Запис розшифрованих даних у файл
with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_message)

print("Шифрування та дешифрування виконано успішно!")"""

#lab6

"""import sympy

# Генерація ключів
def generate_keys(p, q):
    n = p * q
    return n, (p, q)  # Відкритий та закритий ключі

# Функція шифрування
def encrypt(message, pub_key):
    n = pub_key
    encrypted_message = [pow(ord(char), 2, n) for char in message]  # Підносимо код символу до квадрату за модулем n
    return encrypted_message

# Функція дешифрування
def decrypt(encrypted_message, priv_key):
    p, q = priv_key
    n = p * q
    decrypted_message = ''

    for c in encrypted_message:
        # Обчислення квадратних коренів за модулем p та q
        roots_p = sympy.sqrt_mod(c, p, all_roots=True)
        roots_q = sympy.sqrt_mod(c, q, all_roots=True)

        # Генерація можливих коренів
        possible_roots = []
        for r1 in roots_p:
            for r2 in roots_q:
                M1 = (r1 * q * sympy.mod_inverse(q, p) + r2 * p * sympy.mod_inverse(p, q)) % n
                M2 = n - M1  # Другий можливий корінь
                possible_roots.extend([M1, M2])

        # Вибір кореня, що відповідає осмисленому тексту
        valid_chars = [chr(root) for root in possible_roots if 32 <= root <= 126]

        if valid_chars:
            decrypted_message += valid_chars[0]  # Використовуємо перший коректний символ
        else:
            decrypted_message += '?'  # Якщо не знайдено коректного символу

    return decrypted_message

# Контрольний приклад
p = 53
q = 67
n, priv_key = generate_keys(p, q)

# Запис великого осмисленого тексту у файл
input_text = "Метод Рабіна базується на принципі складності обчислення квадратного кореня за модулем великого числа. Завдяки цьому підходу він забезпечує високий рівень захисту інформації у криптографічних системах."
with open("input.txt", "w", encoding="utf-8") as file:
    file.write(input_text)

# Читаємо текстовий файл
with open("input.txt", "r", encoding="utf-8") as file:
    message = file.read()

# Шифрування
encrypted_message = encrypt(message, n)

# Запис зашифрованих даних у файл
with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(' '.join(map(str, encrypted_message)))

# Дешифрування
decrypted_message = decrypt(encrypted_message, priv_key)

# Запис розшифрованого тексту у файл
with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_message)

print("Шифрування та дешифрування виконано успішно!")"""

"""print(ord("П"))

def caesar_cipher(text, shift):
    encrypted_text =""
    for char in text:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord('a')
            encrypted_text += chr((ord(char)- shift_base+ shift)%26+shift_base) # a - 65 - 65 + 3 %26 = 3 + 65 = 68 
        else:
            encrypted_text+=char
    return encrypted_text

# Введення тексту
text = input("Введіть текст для шифрування: ")
shift = 3 # Зміщення на 3
encrypted = caesar_cipher(text, shift)

print("Зашифрований текст:", encrypted)"""


"""import hashlib

# Вхідний текст
text = "hello"

# Створення хешу за допомогою SHA-256
hash_object = hashlib.sha256(text.encode())
hash_object1 = hashlib.sha256(text.encode())
# Виведення хешу
print("Хеш: ", hash_object.hexdigest())
print("Хеш: ", hash_object1.hexdigest())
#print(hashlib.algorithms_available)
a = input("Enter text for hashing: ")
b = "дякую"
while a!=b:
    hash_object2 = hashlib.sha256(a.encode())
    print("Хеш: ", hash_object2.hexdigest())
    a = input("Enter text for hashing: ")
print("Хешування закінчено!")

text = input("Enter text: ")
a = lambda text: hashlib.sha256(text.encode()).hexdigest()
print(a(text))

list1 = ["text1", "text2", "text3"]
list2 = []
for i in list1:
    list2.append(a(i))

print(list2)
hashlist= []
texthash1 = input("enter text 1: ")
texthash2 = input("enter text 2: ")
hashlist.append(a(texthash1))
hashlist.append(a(texthash2))
i = 0
while i < len(hashlist):
    if hashlist[i]==hashlist[i+1]:
        print("Хеші однакові")
        break
    else:
        print("Хеші різні")
        break 

import hashlib

def generate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
# Читання файлу порціями
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()


file_path = "my_file.txt"
file_hash = generate_file_hash(file_path)
print("Хеш файлу: ", file_hash)

hashlib.algorithms_available"""

"""import bcrypt

password = "mysecretpassword1"

# Генерація "солі" та хешування пароля
salt = bcrypt.gensalt()

print(salt)

hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

print(hashed_password)

entered_password = input("Enter your password: ")
i =1
while i < 3:
# Перевірка пароля
    if bcrypt.checkpw(entered_password.encode('utf-8'),hashed_password):
        print("Пароль правильний!")
        break
    else:
        print("Невірний пароль!")
    entered_password = input("Enter your password: ")
    i+=1
if i == 3:
    print("Ви ввели тричі неправильний пароль!\nВаш акаунт заблоковано!")"""

"""import bcrypt

users_db = []
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"),salt)
    users_db.append({"username":username, 'hashed_password':hashed_password})
    print(f"User {username} succesfully registred!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users_db:
        if user['username'] == username:
            if bcrypt.checkpw(password.encode('utf-8'), user['hashed_password']):
                print(f"Ласкаво просимо, {username}!\n")
                return
            else:
                print("Невірний пароль!\n")
                return
        print(f"User {username} is not found!")

def main():
    while True:
        print("1. Реєстрація")
        print("2. Авторизація")
        print("3. Вийти")
        choice = input("Виберіть опцію (1/2/3): ")
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз!\n")

# Запуск програми
if __name__ == "__main__":
    main()"""


"""import telebot

# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('8113042583:AAFSsZza2U9GXA1_baVIXjwKdq-Ib2FavDc')

# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")

# Команда /help: відправляє повідомлення з підказками
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help, /length <текст>")

# Команда /length: визначає довжину введеного тексту
@bot.message_handler(commands=['length'])
def get_length(message):
# Отримуємо текст після команди /length
    text = message.text[8:] # Вилучаємо "/length " з команди
    if not text:
        bot.reply_to(message, "Будь ласка, введи текст для визначення довжини. Наприклад: /length hello world")
        return
# Обчислюємо довжину тексту
    length = len(text)
    bot.reply_to(message, f"Довжина введеного тексту: {length} символів")

# Запуск бота
bot.polling()"""

"""import flask

app = flask.Flask(__name__)
@app.route('/')
def home():
    name = "Dimatest"
    age = 22
    hobby = "programming"
    place = "USA"
    return flask.render_template("index3.html", name=name, age=age,
                                 hobby=hobby, place=place)

if __name__ =='__main__':
    app.run(debug=True)"""

"""from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello world" 
@app.route("/info")
def info():
    return "My name is Dmytro"

if __name__ =='__main__':
    app.run(debug=True)"""

#8.2
"""from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Ласкаво просимо на мій сайт" 
@app.route("/about")
def about():
    return "Це мій другий веб-додаток на Flask!"
@app.route("/contact")
def contact():
    return "Зв’яжіться зі мною за email@example.com"

if __name__ =='__main__':
    app.run(debug=True)"""

"""from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/greet", methods=['POST'])
def greet():
    name = request.form['name']
    age = request.form['age']
    color = request.form['color']
    return f"Привіт, {name}! Тобі {age} років \
        і твій улюблений колір {color}"
if __name__ == '__main__':
    app.run(debug=True)"""
#8.3
"""import flask

app = flask.Flask(__name__)
@app.route('/')
def home():
    return flask.render_template("index2.html",age=15)

if __name__ =='__main__':
    app.run(debug=True)"""

#8.3
'''import flask

app = flask.Flask(__name__)
@app.route('/fruits')
def home():
    fruits_list = ["apple", "lemon", "waterlemon", "cherry", "orange"]
    return flask.render_template("index3.html",fruits = fruits_list)

if __name__ =='__main__':
    app.run(debug=True)'''

'''from flask import Flask, render_template, request

app = Flask(__name__)
fruits_list = [
    {"name": "Яблуко", "color": "red"},
    {"name": "Банан", "color": "yellow"},
    {"name": "Груша", "color": "green"},
    {"name": "Вишня", "color": "red"},
    {"name": "Киві", "color": "green"},
    {"name": "Апельсин", "color": "orange"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    fruits = fruits_list # За замовчуванням показуємо всі фрукти
    if request.method == "POST":
        filter_value = request.form.get("filter") # Отримуємо значення кнопки
        if filter_value == "red": # Якщо натиснули "Червоні фрукти"
            fruits = [fruit for fruit in fruits_list if fruit["color"] == "red"]
        elif filter_value == "green": # Якщо натиснули "Зелені фрукти"
            fruits = [fruit for fruit in fruits_list if fruit["color"] == "green"]
        elif filter_value == "all": # Якщо натиснули "Всі фрукти"
            fruits = fruits_list # Показуємо всі фрукти

    return render_template("index4.html", fruits=fruits)

if __name__ =='__main__':
    app.run(debug=True)'''

#8.4
'''from flask import Flask, render_template, request
app = Flask(__name__)
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        'cm': {'m': 0.01, 'km': 0.00001, 'inch': 0.393701, 'foot': 0.0328084},
        'm': {'cm': 100, 'km': 0.001, 'inch': 39.3701, 'foot': 3.28084},
        'km': {'cm': 100000, 'm': 1000, 'inch': 39370.1, 'foot': 3280.84},
        'inch': {'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'foot': 0.0833333},
        'foot': {'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'inch': 12}
        }
    if from_unit == to_unit:
        return value #Якщо одиниці однакові, повертаємо значення без змін

    return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            result = convert_units(value, from_unit, to_unit)
        except ValueError:
            result = "Помилка: введи число!"
    return render_template("converter.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)'''

#8.6
"""from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = "секретний_ключ"

@app.route("/")
def home():
    if "clicks" not in session:
        session["clicks"]=0
    return render_template("clicker_game_server.html", 
                           clicks= session["clicks"])
@app.route("/click")
def click():
    session['clicks']+=1
    return home()

if __name__ == "__main__":
    app.run(debug=True)"""

#8.7(1)
"""from flask import Flask, render_template
import requests
app = Flask(__name__)
PHP_API_URL = "https://justconsole.tech/python/api.php?table=users"
@app.route('/', methods=['GET'])
def get_users():
    try:
        response = requests.get(PHP_API_URL)
        users = response.json() #Отримуємо список користувачів
        return render_template("crm.html", users=users)
    except requests.exceptions.RequestException as e:
        return f"<p>Помилка при підключенні до сервера: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)"""

#8.7(2)
"""from flask import Flask, render_template, request
import requests
app = Flask(__name__)
PHP_API_URL = "https://justconsole.tech/python/api.php?table=users"
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            response = requests.get(PHP_API_URL)
            users = response.json() #Отримуємо список користувачів
            for user in users:
                if user['username'] == username and user['password'] == password:
                    return f"<h1>Вітаємо, {username}!</h1>" # Успішний вхід
            return render_template("login.html", error="Невірне ім'я користувача або пароль.")
        except requests.exceptions.RequestException as e:
            return f"<p>Помилка при підключенні до сервера: {str(e)}</p>"
    return render_template("login.html", error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5001)"""


#8.7(registation)
"""from flask import Flask, render_template, request, redirect, session
import requests
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# URL API для зберігання даних користувачів
PHP_API_URL = "https://justconsole.tech/python/api.php?table=users_new"
@app.route("/", methods =['GET'])
def home():
# Отримуємо список користувачів з API
    try:
        response = requests.get(PHP_API_URL)
        users = response.json()
        return render_template("registration.html", users=users)
    except requests.exceptions.RequestException as e:
        return f"<p>халепа з апі: {str(e)}</p>"
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # Зберігаємо пароль у відкритому вигляді (без хешування)
    data = {
        "username": username,
        "email": email,
        "password": password # Зберігаємо пароль у відкритому вигляді
    }
    try:
        response = requests.post(PHP_API_URL, json=data)
        if response.status_code == 200:
            return redirect('/')
        else:
            return f"<p>халепа: {response.text}</p>"
    except requests.exceptions.RequestException as e:
        return f"<p>халепа з апі: {str(e)}</p>"
@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        # Отримуємо список користувачів з API
        response = requests.get(PHP_API_URL)
        users = response.json()
        # Знаходимо користувача в базі
        user = next((user for user in users if user['username'] == username), None)
        if user:
            print(f"Знайдений користувач: {user['username']}, Пароль: {user['password']}") # Діагностика
            # Хешуємо введений пароль з 10 символами
            hashed_input_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')): # Порівнюємо збережений хеш з введеним паролем
                # Якщо користувача знайшли і пароль збігається
                session['user'] = user['username'] # Зберігаємо ім'я користувача в сесії
                return f"<h1>Ласкаво просимо, {user['username']}!</h1>"
            else:
                return "<p>Неправильний пароль!</p>"
        else:
            return "<p>Невірний логін!</p>"
    except requests.exceptions.RequestException as e:
        return f"<p>Помилка при перевірці: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5002)"""

#8.8(1)
"""import requests, json
PHP_API_URL = "https://justconsole.tech/python/api.php?table=comments"
response = requests.get(PHP_API_URL)
try:
    comments = response.json()
    print(json.dumps(comments, indent=4, ensure_ascii=False))    
except json.JSONDecodeError:
    print("Помилка: сервер повернув не JSON, а щось інше:", response.text)"""

#8.8(2)
"""from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
PHP_API_URL = "https://justconsole.tech/python/api.php?table=comments"
@app.route('/')
def get_comments():
    try:
        response = requests.get(PHP_API_URL)
        comments = response.json()
        return render_template("films_comments.html", comments=comments)
    except requests.exceptions.RequestException as e:
        return f"<p>халепа: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5002)"""
