# Quiz-Game Application using File handling
**Simple Quiz Application using File handling** - University Project

## 01. FILE OPERATION

Once imported necessary modules for GUI development (**tkinter**), date and time (**datetime**), system-specific parameters (**sys**), operating system functionality (**os**), and image processing (**PIL**), let's define three *constants* representing file operations: **CREATE**, **APPEND**, and **READ**. 

The function **workOnAFile** takes a *filename* and a *flag* as parameters to create, append, or read a file. It also performs specific operations based on the flag.
The script creates **15 quiz** files (q1.txt to q15.txt) with *questions*, answer *options*, and *correct* answers, and manage their content. In particular, it reads the content of each file, **extracting** *questions* from the first row of each file, *options*, and *correct* answers from the second line, **storing** them in separate variables.

Therefore, the script generates a **random** *index* to select a question from the created files and prints the question, correct answer, options, and index.

## 02. GRAPHICAL USER INTERFACE

The further code uses the **tkinter** library to create a graphical user interface (**GUI**) for the quiz application. It sets the *window* title, dimensions, icon, and configurability, and it defines a *menu bar* (**my_menu**) with File and Quiz options. To enhance the visual experience, the GUI uses *images* (icons, background, etc.).

A frame (**my_frame**) is created to contain a text box (**my_text**) for displaying text content. Therefore, the script implements functions for *creating* a new file, *opening* a file, *saving* a file, and opening predefined IT-related quiz files.

The GUI includes a sign-in screen (**user_screen**) with a username and password entry, and a sign-in button (**button1**). 

The script manages the *quiz screen* (**root**), which includes a label for the question, radio buttons for multiple-choice answers, and a "Next" button to move to the next question. It tracks the user's **score** and *updates* the display accordingly. After completing all questions, it displays the user's score and a corresponding *message*.

The application allows the user to **try** the quiz **again** by restarting the program.
