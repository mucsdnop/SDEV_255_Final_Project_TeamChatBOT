"""
Group 3 Helper Chatbot for Strickland Propane
Members:
Rojae Kadeem Murray
Adenike Adetola Oriolowo
John Martin III

SDEV220 10P

About: This program is a basic chatbot to help alleviate stress employees at a call center
may face with an influx of customers with simple questions.
"""

from tkinter import *

root = Tk()
root.title("Group 3")

class Intro:
    def __init__(self):
        
        #create variables for entry boxes
        fname_var = StringVar()
        lname_var = StringVar()
        email_var = StringVar()
        address_var = StringVar()
        city_var = StringVar()
        state_var = StringVar()
        zip_code_var = StringVar()

        #verify entries
        def verify_entries(*args):
            fname = fname_input.get()
            lname = lname_input.get()
            email = email_input.get()
            address = address_input.get()
            city = city_input.get()
            state = state_input.get()
            zip_code = zip_code_input.get()
            if fname and lname and email and address and city and state and zip_code:
                submit_btn.config(state="normal")
            else:
                submit_btn.config(state="disabled")

        fname_var.trace("w", verify_entries)
        lname_var.trace("w", verify_entries)
        email_var.trace("w", verify_entries)
        address_var.trace("w", verify_entries)
        city_var.trace("w", verify_entries)
        state_var.trace("w", verify_entries)
        zip_code_var.trace("w", verify_entries)

        #Add labels to describe what each entry box is for
        fname = Label(text = "First Name:")
        fname.grid(row=1, column=0)
        lname = Label(text = "Last Name:")
        lname.grid(row=2, column=0)
        email = Label(text = "E-mail:")
        email.grid(row=3, column=0)
        address = Label(text = "Address:")
        address.grid(row=4, column=0)
        city = Label(text = "City:")
        city.grid(row=5, column=0)
        state = Label(text = "State:")
        state.grid(row=6, column=0)
        zip_code = Label(text = "Zip code:")
        zip_code.grid(row=7, column=0)

        #create entry boxes using the above variables created for it
        fname_input = Entry(root, textvariable = fname_var)
        fname_input.grid(row=1, column=1)
        lname_input = Entry(root, textvariable = lname_var)
        lname_input.grid(row=2, column=1)
        email_input = Entry(root, textvariable = email_var)
        email_input.grid(row=3, column=1)
        address_input = Entry(root, textvariable = address_var)
        address_input.grid(row=4, column=1)
        city_input = Entry(root, textvariable = city_var)
        city_input.grid(row=5, column=1)
        state_input = Entry(root, textvariable = state_var)
        state_input.grid(row=6, column=1)
        zip_code_input = Entry(root, textvariable = zip_code_var)
        zip_code_input.grid(row=7, column=1)

        def chat_continue():
            self.fname = fname_input.get()
            self.lname = lname_input.get()
            self.email = email_input.get()
            self.address = address_input.get()
            self.city = city_input.get()
            self.state = state_input.get()
            self.zip_code = zip_code_input.get()
            self.cust_info = {"FirstName": self.fname, "LastName": self.lname, "Email": self.email, "Address": self.address, "City":self.city, "State": self.state, "Zipcode":self.zip_code} #Create a dictionary
            ChatBot.open_win(self.cust_info)

        #Buttons to continue or quit
        submit_btn=Button(root, state=DISABLED, text = "Continue", command=lambda:[root.withdraw(), chat_continue()])
        submit_btn.grid(row=9, column=0, columnspan=1, pady=10)
        quit_btn=Button(root,text = "Quit", command = root.destroy)
        quit_btn.grid(row=9, column=1, columnspan=1, pady=10)

        root.mainloop()


class ChatBot(Intro):
    def __init__(self):
        pass
    
    def open_win(cust_info): #Open a new window
        new = Toplevel(root)
        new.title("Helper ChatBot")

        def send():
            send = "You: " + user_entry.get()
            txt.insert(END, "\n" + send)
        
            user = user_entry.get().lower()
        
            if (user == "hello" or user == "hi"):
                txt.insert(END, "\n" + "Bot: Hi there, how can I help? Try saying !sales, !hours, or !help")
            elif (user == "how are you"):
                txt.insert(END, "\n" + "Bot: fine! and you")
            elif (user == "great" or user == "fine" or user == "i am fine" or user == "i am doing well"):
                txt.insert(END, "\n" + "Bot: Great! How can I assist you? Try saying !sales, !hours, or !help")
            elif (user == "thanks" or user == "thank you" or user == "ty"):
                txt.insert(END, "\n" + "Bot: No problem.")
            elif (user == "what do you sell?"):
                txt.insert(END, "\n" + "Bot: Strickland Propane sells propane and propane accessories.")
            elif (user == "bye" or user == "goodbye" or user == "gb"):
                txt.insert(END, "\n" + "Bot: It was nice talking to you. Have a nice day!")
            elif (user == "!sales"):
                txt.insert(END, "\n" + "Bot: We sell propane and propane accessories.")
            elif (user == "!hours"):
                txt.insert(END, "\n" + "Bot: Strickland Propane is open from 6am-8pm all week.")
            elif (user == "!help"):
                txt.insert(END, "\n" + "Bot: For information type any of the following: !sales, !hours, or !help to repeat this message.")
            else:
                txt.insert(END, "\n" + "Bot: I have limited responses. Please try again or type !help")
        
            user_entry.delete(0, END)
        
        fname = Label(new, text = cust_info['FirstName'])
        fname.grid(row=1, column=0)
        lname = Label(new, text = cust_info['LastName'])
        lname.grid(row=2, column=0)
        email = Label(new,text = cust_info['Email'])
        email.grid(row=3, column=0)
        address = Label(new,text = cust_info['Address'])
        address.grid(row=4, column=0)
        city = Label(new,text = cust_info['City'])
        city.grid(row=5, column=0)
        state = Label(new,text = cust_info['State'])
        state.grid(row=6, column=0)
        zip_code = Label(new,text = cust_info['Zipcode'])
        zip_code.grid(row=7, column=0)
        
        txt = Text(new, bg="Light Gray", fg="Black", width=60)
        txt.grid(row=1, column=1, columnspan=2, rowspan=7)
        
        scrollbar = Scrollbar(txt)
        scrollbar.place(relheight=1, relx=1)
        
        user_entry = Entry(new, bg="Light Gray", fg="Black", width=55)
        user_entry.grid(row=8, column=1)
        
        send = Button(new, text="Send", bg="Light Gray",
                    command=send).grid(row=8, column=2)
        finish_conv = Button(new,text="Finish",command=lambda:[new.withdraw(), ThankYou.open_thanks()]).grid(row=8, column=0, pady=10) #Open a new window thanking the customer

class ThankYou(ChatBot):
    def __init__(self):
        pass


    def open_thanks():  #Opens a thank you window 
        last = Toplevel(root)
        last.title("Thank you")
        Label(last, text="Thank you for your continued support.").grid(row=0, column=0, padx=2, pady=2)
        quit_btn=Button(last,text="Close",command=root.destroy).grid(row=3, column=0, padx=2, pady=2)
        last.mainloop()

start_bot = Intro()