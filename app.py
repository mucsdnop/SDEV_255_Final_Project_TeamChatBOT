#Group 3 chatbot

from tkinter import *
 
# Initialize Tkinter
root = Tk()
root.title("Group 3 Chatbot")
 

# Receive and send message function
def send():
    send = "You: " + user_entry.get()
    txt.insert(END, "\n" + send)
 
    user = user_entry.get().lower()
 
    if (user == "hello" or user == "hi"):
        txt.insert(END, "\n" + "Bot: Hi there, how can I help?")
 
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot: fine! and you")
 
    elif (user == "great" or user == "fine" or user == "i am fine" or user == "i am doing well"):
        txt.insert(END, "\n" + "Bot: Great! How can I assist you?")
 
    elif (user == "thanks" or user == "thank you" or user == "ty"):
        txt.insert(END, "\n" + "Bot: No problem.")
 
    elif (user == "what do you sell?"):
        txt.insert(END, "\n" + "Bot: This is still under construction.")
 
    elif (user == "bye" or user == "goodbye" or user == "gb"):
        txt.insert(END, "\n" + "Bot: It was nice talking to you.")
 
    else:
        txt.insert(END, "\n" + "I have limited responses. Please try again.")
 
    user_entry.delete(0, END)
 
 
txt = Text(root, bg="Light Gray", fg="Black", width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
user_entry = Entry(root, bg="Light Gray", fg="Black", width=55)
user_entry.grid(row=2, column=0)
 
send = Button(root, text="Send", bg="Light Gray",
              command=send).grid(row=2, column=1)
 
root.mainloop()