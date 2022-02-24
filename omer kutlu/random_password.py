"""
Random Password
General Information:
I want to use a program which can generate random password and display the result on user interface. 
Acceptance Criteria:
* Use tkinter package to solve the problem. (You can use the random student codes as template)
* Password length must be 10 characters long. 
* It must contain at least 2 upper case letter, 2 digits and 2 special symbols. 
* You must import some required modules or packages. 
* The GUI of program must contain at least a button and a label (customize the screen according to yourself) 
* The result should be display on the password label when the user click the generate button.
"""
import random
import string
import tkinter as tk
def random_passport():
    dgts=string.digits
    sym=string.punctuation
    low=string.ascii_lowercase
    up=string.ascii_uppercase
    all_of=(dgts+sym+low+up)
    passport=(random.sample(up,2)+(random.sample(dgts,2)+(random.sample(sym,2)+(random.sample(all_of,4)))))
    passport=list("".join(passport))
    random.shuffle(passport)
    print("".join(passport))
    label.config(text=passport)

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("600x300")
key_application = tk.Frame(window)
key_application.grid()
label_txt = tk.Label(key_application, text="Random Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)
# label
label = tk.Label(key_application, text="Please push the botton to generate new password ", font="arial 12")
label.grid(padx=110, pady=20)
# button
button1 = tk.Button(key_application, text=" GENERATE ", width=50, height=5, command=random_passport)
button1.grid(padx=110, pady=40)
window.mainloop()