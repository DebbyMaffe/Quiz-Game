#import random as rnd
from random import randrange

import tkinter as tk
import datetime as dt
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import sys                                             # System Specific Parameter
import os                                              # Operative System Functionality
import subprocess                                      # for launching child processes
from PIL import Image, ImageTk


# Let's define some gloabl constants
CREATE = 1
APPEND = 2
READ = 3

def workOnAFile(filename, flag):
    if flag == CREATE:
        # Write
        f = open(filename, "w")
        with open(filename) as f:
            questions = f.read().splitlines()        # Return a list of the lines in the string
    else:
        # Read
        if flag == READ:
            print()
            index = 0                                # Initialization
            f = open(filename, "r")
            row = f.readline()                       # Read the first row of the file
            print("[", index, "]", row, end='')
            while row:                               # while there are rows to read
                row = f.readline()
                if row:
                    index = index + 1
                    print("[", index, "]", row, end='')
            print()
        else: 
            # Append
            f = open(filename, "a")
            f.write('\n')       # Appending a new line at th end opf the string
    f.close()

# Create File for the first time
workOnAFile("q1.txt", CREATE)
f1 = open("q1.txt", "w")
f1.write("A programm is executed statement by statement, following three keys stages:\n")
f1.write("4\n")
f1.write("Load, Execute and Output\n")
f1.write("Fetch, Execute and Decode\n")
f1.write("Decode, Fetch and Execute\n")
f1.write("Fetch, Decode and Execute\n")
f1.close()

workOnAFile("q2.txt", CREATE)
f2 = open("q2.txt", "w")
f2.write("What is HTTP?\n")
f2.write("1\n")
f2.write("A network protocol to transfer data between a server and clients\n")
f2.write("A programming language to transfer data between a server and clients\n")
f2.write("An operative system to transfer data between a server and clients\n")
f2.write("None of the above\n")
f2.close()

workOnAFile("q3.txt", CREATE)
f3 = open("q3.txt", "w")
f3.write("Who invented Python language?\n")
f3.write("2\n")
f3.write("Bill Gates\n")
f3.write("Guido Van Rossum\n")
f3.write("Albert Einstein\n")
f3.write("Steve Jobs\n")
f3.close()

workOnAFile("q4.txt", CREATE)
f4 = open("q4.txt", "w")
f4.write("The third column of ASCII table represents:\n")
f4.write("3\n")
f4.write("The actual bits combination corresponding to a character of the alphabet\n")
f4.write("The first column in hexadecimal base system\n")
f4.write("The first column in eight base system\n")
f4.write("The character of the alphabet\n")
f4.close()

workOnAFile("q5.txt", CREATE)
f5 = open("q5.txt", "w")
f5.write("The access time of a Magnetic Disk is given by:\n")
f5.write("1\n")
f5.write("Seek time + Rotational time + Transfer time\n")
f5.write("Rotational time + Transfer time + Reading time\n")
f5.write("Fetch time + Rotational time + Transfer time + Reading time\n")
f5.write("None of the above\n")
f5.close()

workOnAFile("q6.txt", CREATE)
f6 = open("q6.txt", "w")
f6.write("What is a Process?\n")
f6.write("2\n")
f6.write("An instance of the execution of a program and its data\n")
f6.write("An instance of the execution of a program\n")
f6.write("A program to guide the OS to the usage of a hardware component\n")
f6.write("A software that communicates with the hardware\n")
f6.close()

workOnAFile("q7.txt", CREATE)
f7 = open("q7.txt", "w")
f7.write("Common types of Networks:\n")
f7.write("4\n")
f7.write("PAN, LAN\n")
f7.write("LAN, MAN\n")
f7.write("MAN, WAN\n")
f7.write("LAN, WAN\n")
f7.close()

workOnAFile("q8.txt", CREATE)
f8 = open("q8.txt", "w")
f8.write("In 1992, the NCSA built the first browser called:\n")
f8.write("3\n")
f8.write("Netscape Navigator\n")
f8.write("World Wide Web\n")
f8.write("Mosaic\n")
f8.write("Internet Explorer\n")
f8.close()

workOnAFile("q9.txt", CREATE)
f9 = open("q9.txt", "w")
f9.write("Which of the following statements is wrong?\n")
f9.write("2\n")
f9.write("A variable is a way to store a value\n")
f9.write("A primitive can be separated in other sub-operations\n")
f9.write("A flow-chart is a graphical representation of the algorithm steps\n")
f9.write("An algorithm is a set of well-defined instructions\n")
f9.close()

workOnAFile("q10.txt", CREATE)
f10 = open("q10.txt", "w")
f10.write("Which of the following is not an interpreted programming language?\n")
f10.write("1\n")
f10.write("C++\n")
f10.write("Python\n")
f10.write("R\n")
f10.write("Javascript\n")
f10.close()

workOnAFile("q11.txt", CREATE)
f11 = open("q11.txt", "w")
f11.write("A dictionary is a collection of information:\n")
f11.write("4\n")
f11.write("Not Ordered, Mutable and Indexed\n")
f11.write("Not Ordered, Not Mutable and Inedxed\n")
f11.write("Not Ordered, Not Mutable and Not Indexed\n")
f11.write("Ordered, Mutable and Indexed\n")
f11.close()

workOnAFile("q12.txt", CREATE)
f12 = open("q12.txt", "w")
f12.write("An array is a collection of information:\n")
f12.write("2\n")
f12.write("Heterogeneous, Ordered and Indexed\n")
f12.write("Homogeneous, Ordered and Inedxed\n")
f12.write("Homogeneous, Not Ordered and Indexed\n")
f12.write("Heterogeneous, Ordered and Not Indexed\n")
f12.close()

workOnAFile("q13.txt", CREATE)
f13 = open("q13.txt", "w")
f13.write("Through which NumPy function you can solve a quadratic polynomial?\n")
f13.write("3\n")
f13.write("root()\n")
f13.write("quad()\n")
f13.write("poly1d()\n")
f13.write("poly()\n")
f13.close()

workOnAFile("q14.txt", CREATE)
f14 = open("q14.txt", "w")
f14.write("li <- list(val = TRUE, a = c(1 ,3)). How we can access 'val'?\n")
f14.write("4\n")
f14.write("li$a\n")
f14.write("list$val\n")
f14.write("li£val\n")
f14.write("li$val\n")
f14.close()

workOnAFile("q15.txt", CREATE)
f15 = open("q15.txt", "w")
f15.write("A binary number has 5 digits. What is -3 in binary M&S?\n")
f15.write("1\n")
f15.write("10011\n")
f15.write("00011\n")
f15.write("10001\n")
f15.write("10011\n")
f15.close()

# Read the file
# workOnAFile("q1.txt", READ)
# workOnAFile("q2.txt", READ)
# workOnAFile("q3.txt", READ)
# workOnAFile("q4.txt", READ)
# workOnAFile("q5.txt", READ)
# workOnAFile("q6.txt", READ)
# workOnAFile("q7.txt", READ)
# workOnAFile("q8.txt", READ)
# workOnAFile("q9.txt", READ)
# workOnAFile("q10.txt", READ)
# workOnAFile("q11.txt", READ)
# workOnAFile("q12.txt", READ)
# workOnAFile("q13.txt", READ)
# workOnAFile("q14.txt", READ)
# workOnAFile("q15.txt", READ)

# Manage the content of each File
f1 = open("q1.txt", "r")

q1 = f1.readline()                         # question
i1 = f1.readline()     
a1 = f1.readline()                         # 1st answer
a2 = f1.readline()                         # 2nd answer
a3 = f1.readline()                         # 3rd answer
a4 = f1.readline()                         # 4th answer (correct)


f2 = open("q2.txt", "r")

q2 = f2.readline()                         # question
i2 = f2.readline()     
b1 = f2.readline()                         # 1st answer (correct)
b2 = f2.readline()                         # 2nd answer
b3 = f2.readline()                         # 3rd answer
b4 = f2.readline()                         # 4th answer


f3 = open("q3.txt", "r")

q3 = f3.readline()                         # question
i3 = f3.readline()     
c1 = f3.readline()                         # 1st answer
c2 = f3.readline()                         # 2nd answer (correct)
c3 = f3.readline()                         # 3rd answer
c4 = f3.readline()                         # 4th answer


f4 = open("q4.txt", "r")

q4 = f4.readline()                         # question
i4 = f4.readline()     
d1 = f4.readline()                         # 1st answer
d2 = f4.readline()                         # 2nd answer
d3 = f4.readline()                         # 3rd answer (correct)
d4 = f4.readline()                         # 4th answer


f5 = open("q5.txt", "r")

q5 = f5.readline()                         # question
i5 = f5.readline()     
e1 = f5.readline()                         # 1st answer (correct)
e2 = f5.readline()                         # 2nd answer
e3 = f5.readline()                         # 3rd answer
e4 = f5.readline()                         # 4th answer


f6 = open("q6.txt", "r")

q6 = f6.readline()                         # question
i6 = f6.readline()     
g1 = f6.readline()                         # 1st answer
g2 = f6.readline()                         # 2nd answer (correct)
g3 = f6.readline()                         # 3rd answer
g4 = f6.readline()                         # 4th answer


f7 = open("q7.txt", "r")

q7 = f7.readline()                         # question
i7 = f7.readline()     
h1 = f7.readline()                         # 1st answer
h2 = f7.readline()                         # 2nd answer
h3 = f7.readline()                         # 3rd answer
h4 = f7.readline()                         # 4th answer (correct)


f8 = open("q8.txt", "r")

q8 = f8.readline()                         # question
i8 = f8.readline()     
j1 = f8.readline()                         # 1st answer
j2 = f8.readline()                         # 2nd answer
j3 = f8.readline()                         # 3rd answer (correct)
j4 = f8.readline()                         # 4th answer


f9 = open("q9.txt", "r")

q9 = f9.readline()                         # question
i9 = f9.readline()     
k1 = f9.readline()                         # 1st answer
k2 = f9.readline()                         # 2nd answer (correct)
k3 = f9.readline()                         # 3rd answer
k4 = f9.readline()                         # 4th answer


f10 = open("q10.txt", "r")

q10 = f10.readline()                        # question
i10 = f10.readline()     
l1 = f10.readline()                         # 1st answer (correct)
l2 = f10.readline()                         # 2nd answer
l3 = f10.readline()                         # 3rd answer
l4 = f10.readline()                         # 4th answer


f11 = open("q11.txt", "r")

q11 = f11.readline()                        # question
i11 = f11.readline()     
m1 = f11.readline()                         # 1st answer 
m2 = f11.readline()                         # 2nd answer
m3 = f11.readline()                         # 3rd answer
m4 = f11.readline()                         # 4th answer (correct)


f12 = open("q12.txt", "r")

q12 = f12.readline()                        # question
i12 = f12.readline()     
n1 = f12.readline()                         # 1st answer 
n2 = f12.readline()                         # 2nd answer (correct)
n3 = f12.readline()                         # 3rd answer
n4 = f12.readline()                         # 4th answer 


f13 = open("q13.txt", "r")

q13 = f13.readline()                        # question
i13 = f13.readline()     
o1 = f13.readline()                         # 1st answer 
o2 = f13.readline()                         # 2nd answer 
o3 = f13.readline()                         # 3rd answer (correct)
o4 = f13.readline()                         # 4th answer 


f14 = open("q14.txt", "r")

q14 = f14.readline()                        # question
i14 = f14.readline()     
p1 = f14.readline()                         # 1st answer 
p2 = f14.readline()                         # 2nd answer 
p3 = f14.readline()                         # 3rd answer 
p4 = f14.readline()                         # 4th answer (correct)


f15 = open("q15.txt", "r")

q15 = f15.readline()                        # question
i15 = f15.readline()     
r1 = f15.readline()                         # 1st answer (correct)
r2 = f15.readline()                         # 2nd answer 
r3 = f15.readline()                         # 3rd answer 
r4 = f15.readline()                         # 4th answer 

# Store all the QUESTIONS (first row of each File)
Questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]
print(Questions)

# Store all the POSSIBLE answers for each Question
a = [a1, a2, a3, a4]
b = [b1, b2, b3, b4]
c = [c1, c2, c3, c4]
d = [d1, d2, d3, d4]
e = [e1, e2, e3, e4]
g = [g1, g2, g3, g4]
h = [h1, h2, h3, h4]
j = [j1, j2, j3, j4]
k = [k1, k2, k3, k4]
l = [l1, l2, l3, l4]
m = [m1, m2, m3, m4]
n = [n1, n2, n3, n4]
o = [o1, o2, o3, o4]
p = [p1, p2, p3, p4]
r = [r1, r2, r3, r4]

# Store ALL the answers
Options = [a, b, c, d, e, g, h, j, k, l, m, n, o, p, r]
print(Options)

# Store only the CORRECT answers
Answers = [a4, b1, c2, d3, e1, g2, h4, j3, k2, l1, m4, n2, o3, p4, r1]
print(Answers)

# Store the INDEXES of the correct answer (second row of each File)
Indexes = [4, 1, 2, 3, 1, 2, 4, 3, 2, 1, 4, 2, 3, 4, 1]
print(Indexes)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()
f15.close()


# GENERATE RANDOM QUESTION 
i = randrange(len(Questions))
question_text = Questions[i]
correct_answer = Answers[i]
options = Options[i]
index = Indexes[i]

print("The index is:")
print(i)                          # index
print("The question is:")
print(question_text)              # i-th question
print("The correct answer is:")
print(correct_answer)             # i-th correct answer
print("The options are:")
print(options)                    # i-th possible answers
print("The index of the correct answer is:")
print(index)



###########--------------------------------------------
# Create the GUI        
window = tk.Tk()
window.title("IT-Quiz App")
window.geometry('830x480+350+150')
window.iconbitmap('./quiz.ico')
window.resizable(True, True)

window.minsize(600, 200)
window.maxsize(980, 680)
window.attributes('-topmost', 1)

# Insert a MENU widget
my_menu = Menu(window)
window.config(menu = my_menu)

# Create a Frame containing the Text Box
my_frame = tk.Frame(window)
my_frame.pack_forget()

# Create the Scrollbar for the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

# Create Text Box
my_text = tk.Text(my_frame, width = 97, height = 25, font = ('Helvetica', 13), selectbackground = 'yellow', selectforeground = 'black', yscrollcommand = text_scroll.set)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command = my_text.yview)

# Set variable for open file name
global open_status_name
open_status_name = False

# Create New File Function
def new_file():
    user_screen.pack_forget()
    root.pack_forget() 
    result.pack_forget()
    score.pack_forget()
    my_frame.pack(pady = 5)
    # Delete previous text
    my_text.delete("1.0", END)
    window.title('New File - TextPad!')
    
# Open Files
def open_file():
    user_screen.pack_forget()
    root.pack_forget() 
    result.pack_forget()
    score.pack_forget()
    my_frame.pack(pady = 5)
    # Delete previous text
    my_text.delete("1.0", END)
    # Grab Filename
    filename = filedialog.askopenfilename(parent = window)
    # Check to see if there is a file name
    if filename:
        # Make filename global so we can access it later
        global open_status_name
        open_status_name = filename
    # Open the file
    text_file = open(filename, 'r')
    stuff = text_file.read()
    # Add file to Text Box
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Save Files
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

# Open IT_Coding file
def open_IT():
    user_screen.pack_forget()
    root.pack_forget() 
    result.pack_forget()
    score.pack_forget()
    my_frame.pack(pady = 5)
    # Delete previous text
    my_text.delete("1.0", END)
    # Open the file
    text_file = open('IT_Coding.txt', 'r')
    stuff = text_file.read()
    # Add file to Text Box
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Open User file
def open_result():
    user_screen.pack_forget()
    root.pack_forget() 
    result.pack_forget()
    score.pack_forget()
    my_frame.pack(pady = 5)
    # Delete previous text
    my_text.delete("1.0", END)
    # Open the file
    text_file = open('user.txt', 'r')
    stuff = text_file.read()
    # Add file to Text Box
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Restart the Quiz
def restart():
    # Reconstruct the correct path to your Python script, and pass it as an argument to the Python interpreter
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
    sys.argv[1:])

# Create a File Menu item
file_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = window.quit)

# Create a Quiz Menu item
quiz_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'Quiz', menu = quiz_menu)
quiz_menu.add_command(label = "About IT", command = open_IT)
quiz_menu.add_command(label = 'Result', command = open_result)
quiz_menu.add_separator()
quiz_menu.add_command(label = 'Try Again', command = restart)




# Manage the SIGN-IN Screen
user_screen = tk.Frame()
user_screen.pack(padx = 5, pady = 5)

photo = Image.open('img1.png')
new_photo = photo.resize((300, 190), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(new_photo)

title = tk.Label(user_screen, text = "IT-Coding Quiz", font = ('Georgia', 19, 'bold'), bg = 'teal', fg = 'white', justify = 'center', image = img1, compound = "bottom")
title.pack(padx = 10, pady = 10, expand = True)

# Login
def signin():
    username = user_entry.get()
    password = pw_entry.get()
    root.pack()

    if username == 'admin' and password == 'Quiz13':
        user_screen.pack_forget()
        root.pack()
    elif username!='admin' and password!='Quiz13':
        messagebox.showerror("Invalid", "Invalid username and password!")
    elif password!='Quiz13':
        messagebox.showerror("Invalid", "Invalid password!") 
    elif username!='admin':
        messagebox.showerror("Invalid", "Invalid username!") 
    
label_user = tk.Label(user_screen, text = "Username", font = ('Georgia', 9, 'bold'), fg = 'teal')
label_user.pack(padx = 10, pady = 10)

username = StringVar()
user_entry = tk.Entry(user_screen, textvariable = username, width = 30)
user_entry.pack()
user_entry.focus()

label_pw = tk.Label(user_screen, text = "Password", font = ('Georgia', 9, 'bold'), fg = 'teal')
label_pw.pack(padx = 10, pady = 10)

password = StringVar()
pw_entry = tk.Entry(user_screen, textvariable = password, show = "*", width = 30)
pw_entry.pack()

button1 = tk.Button(user_screen, text = "Sign in", bg = 'teal', fg = 'white', width = 7, borderwidth = 2, command = signin)
button1.pack(padx = 20, pady = 20)



# Manage the QUIZ Screen
root = tk.Frame()
root.pack_forget()                   # to make invisible during the login

question = tk.Label(root, width = 60, font = ('Verdana', 13, 'bold'), text = question_text, bg = 'salmon', fg = 'white')
question.pack(padx = 10, pady = 25, ipadx = 10, ipady = 10, expand = True)

v = IntVar()                         # each RadioButton has to be associated with the same variable

# Create Multiple Choise
option1 = tk.Radiobutton(root, bg = 'lavender', variable = v, value = 1, font = ('Verdana', 11), text = options[0])
option1.pack(padx = 5, pady = 5)
option2 = tk.Radiobutton(root, bg = 'lavender', variable = v, value = 2, font = ('Verdana', 11), text = options[1])
option2.pack(padx = 5, pady = 5, fill = tk.Y, expand = True)
option3 = tk.Radiobutton(root, bg = 'lavender', variable = v, value = 3, font = ('Verdana', 11), text = options[2])
option3.pack(padx = 5, pady = 5, fill = tk.Y, expand = True)
option4 = tk.Radiobutton(root, bg = 'lavender', variable = v, value = 4, font = ('Verdana', 11), text = options[3])
option4.pack(padx = 5, pady = 5, fill = tk.Y, expand = True)

Score = IntVar()
Score.set(0)
#Total_No_Questions = len(Questions)         
Total_No_Questions = 5                       # total number of questions
Question_no = IntVar()
Question_no.set(1)                           # set() to change the value of the variable
#print(Question_no.get())                    # question number 

def nextQuestion():
    print(v.get())                           # get() to read the current value of the variable
    if v.get() == 1:
        selected_option = 1
    elif v.get() == 2:
        selected_option = 2
    elif v.get() == 3:
        selected_option = 3
    elif v.get() == 4:
        selected_option = 4
    else:
        selected_option = -1                 # none selected
        
    # Questions has to be selected randomly
    for i in range(0, len(Questions)):
        if(Indexes[i] == selected_option and i == Question_no.get() -1):
            Score.set(Score.get() + 1)   
            #Questions.pop(i)                        # to remove the current question from the available ones  
            #Answers.pop(i)                          # to remove the current answer from the available ones
            #Options.pop(i)                          # to remove the current options from the available ones
            #Indexes.pop(i)                          # to remove the current index from the available ones             
    print("Score: ")
    print(Score.get())
    Question_no.set(Question_no.get() + 1)
    if Score.get() == 5:
        note = 'Excellent! You are ready to pass the exam with the best mark!'
    elif Score.get() == 4:
        note = 'Well Done! You are above the average standard but with some errors!'
    elif Score.get() == 3:
        note = 'Sufficient! Your performance meets the minimum criteria!'
    else:
        note = 'Fail! Considerable further work is required!'

    note = tk.Label(window, font = ('Georgia', 14), bg = 'salmon', fg = 'white', justify = 'center', text = note)
    note.pack_forget()
    
    if Question_no.get() > Total_No_Questions:
        root.pack_forget()
        result.pack(padx = 40, pady = 30)
        score.pack(padx = 20, pady = 20)
        score.config(text = "Score: " + str(Score.get()) + " / " + str(Total_No_Questions))  
        note.pack(padx = 20, pady = 20)

        # Creazione FILE, containing Username - Timestamp - Score 
        workOnAFile("user.txt", APPEND)
        f = open("user.txt", "a")
        username = user_entry.get()
        timestamp = str(dt.datetime.now())
        point = str(Score.get())
        Point = Score.get()
        f.write("Username: \t" + str(username) + "\n")
        f.write("Timestamp: \t" + timestamp + "\n")
        f.write("Score: \t" + point + " / " + str(Total_No_Questions) + "\n")
        f.close()
        
    else: 
        v.set(0)
        question.config(text = Questions[Question_no.get() - 1])
        option1.config(text = Options[Question_no.get() - 1][0])
        option2.config(text = Options[Question_no.get() - 1][1])
        option3.config(text = Options[Question_no.get() - 1][2])
        option4.config(text = Options[Question_no.get() - 1][3])
        
    #if Question_no.get() == len(Options):
    if Question_no.get() == Total_No_Questions:
            next_b['text'] = 'Check the Results'


next_b = tk.Button(root, bg = "#fff", font = ('Verdana', 10), text = "Next", command = nextQuestion)
next_b.pack(padx = 20, pady = 20)

brain = Image.open('Cod_Brain.png')
new_brain = brain.resize((300, 205), Image.ANTIALIAS)
imgb = ImageTk.PhotoImage(new_brain)

result = tk.Label(window, image = imgb, fg = 'white', bg = 'salmon', justify = 'center', compound = 'bottom')
result.place_forget()

score = tk.Label(window, font = ('Georgia', 15, 'bold'), bg = 'white', fg = 'salmon', justify = 'center')
score.place_forget()



# Mainloop
window.mainloop()