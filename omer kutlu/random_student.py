"""
Random Student (Problem Solving Example)
General Information:
I want to choose a random student in Pyton Class-2 Coursiers
Acceptance Criteria:
* Make changes to the random student codes that has been shared with you.
* In current state, the program chooses a random one from the list when the button is pressed.
* What is expected of you is to ensure that the selected person is not selected during 3 hands.
"""
import random
import string
import tkinter as tk
std_list=["Emrullah Bey", "Ertan Bey", "Fethullah Bey", "Furkan Bey", 
    "Hasan Bey", "Mehmet Bey", "Ömer Bey", "Tayyip Bey", 
    "Yunus Emre Bey", "Merve Hanım", "Mustafa Bey", "Murat Bey"]
templist=[]
def random_student():    
    student=random.sample(std_list,1) 
    templist.insert(0,student[0])
    if len(templist)==4:
        std_list.append(templist[-1])
    elif len(templist)>4:
        std_list.append(templist[3])
        templist.remove(templist[-1])
    #print(student)
    str = ''
    for i in student:
        str += i
        std_list.remove(str)
        print(std_list)
        print(templist)
        print(str)
        label.config(text=str)  
        #return str
window = tk.Tk()

window.title("Random Student")
window.geometry("600x300")

key_application = tk.Frame(window)
key_application.grid()

# label
label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)

# label
label = tk.Label(key_application, text="Please push the botton to choose a next student ", font="arial 12")
label.grid(padx=110, pady=20)

# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_student)
button1.grid(padx=110, pady=40)

window.mainloop()