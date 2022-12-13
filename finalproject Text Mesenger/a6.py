# a5.py
# 
# ICS 32 
#
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
# v0.4
# 
# The following module provides a graphical user interface shell for the DSP journaling program.



import tkinter as tk
from tkinter import ttk, filedialog
from Profile import Message, Profile, Post
from ds_messenger import DirectMessage, DirectMessenger
import ds_client
from pathlib import Path
import tkinter.scrolledtext as st

chosencontact = None
"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the body portion of the root frame.
"""
class Body(tk.Frame):
    def __init__(self, root, select_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback

        # a list of the Post objects available in the active DSU file
        self._messages = {} #now dictionary object
        self._contacts = []
        
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance 
        self._draw()

    
    
    """
    Update the entry_editor with the full post entry when the corresponding node in the posts_tree
    is selected.
    """
    def node_select(self, event):
        global chosencontact
        self.text_area.config(state='normal')
        self.text_area.delete(0.0,'end')
        index = int(self.posts_tree.selection()[0])
        person = self._contacts[index]
        chosencontact = person
        msg_lst = self._messages[person] #msg_lst is list of dictionaries
        print('this is list')
        print(msg_lst)
        for msg in msg_lst: #msg = dictionary
            self.set_text_entry(msg['message'], msg['messenger'])
        self.text_area.config(state='disabled')
    
    """
    Returns the text that is currently displayed in the convo_editor and the chat box.
    """
    def get_text_entry(self) -> str:
        return self.convo_editor.get('1.0', 'end').rstrip()

    def get_text_area(self) -> str:
        return self.text_area.get('1.0', 'end').rstrip()

    """
    Sets the text to be displayed in the entry_editor widget.
    NOTE: This method is useful for clearing the widget, just pass an empty string.
    """
    def set_text_entry(self, text:str, person):
        if person == '':
            self.text_area.insert(tk.INSERT, '{}\n'.format(text))
        else:
            self.text_area.insert(tk.INSERT, '{}: {}\n'.format(person, text))
        
        #deletes all current text in self.entry_editor widget
        #inserts value contained in text parameter
    
    """
    Populates the self._posts attribute with posts from the active DSU file.
    """
    def set_messages(self, messages, contacts):
        self._messages = messages #messages = dictionary {contact: list of message dictionaries}
        self._contacts = contacts
        id = 0
        for contact in self._messages:
            print(contact)
            self._insert_post_tree(id, contact)
            id += 1

    def insert_contact(self, contact):
        '''Inserts a single contact in treeview'''
        if contact not in self._contacts:
            self._contacts.append(contact)
            id = len(self._contacts) - 1 #adjust id for 0-base of treeview widget
            self._insert_post_tree(id, contact)
            self._messages[contact] = []
    
    def insert_message(self, message):
        '''Inserts a single message'''
        self.text_area.config(state='normal')
        currentconvo = self.get_text_area() 
        self.text_area.delete(0.0,'end')
        self.set_text_entry(currentconvo, '')
        self.set_text_entry(message['message'], message['messenger'])
        self.text_area.config(state='disabled')

    """
    Resets all UI widgets to their default state. Useful for when clearing the UI is neccessary such
    as when a new DSU file is loaded, for example.
    """
    def reset_ui(self):
        self.set_text_entry("", "")
        self.text_area.configure(state=tk.NORMAL)
        self._messages = []
        self._contacts = []
        for item in self.posts_tree.get_children():
            self.posts_tree.delete(item)

    """
    Inserts a post entry into the posts_tree widget.
    """
    def _insert_post_tree(self, id, recipient):
        # In case of long user use only first 24
        if len(recipient) > 25:
            recipient = recipient[:24] + "..."
        
        self.posts_tree.insert('', id, id, text=recipient)
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250, bg = '#f2dbde')
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)
        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=10)

        # The message widget 
        self.text_area = st.ScrolledText(master=self, bg = '#f2dbde')
        self.text_area.pack(padx=20, pady=5)
        self.text_area.insert(tk.INSERT, "Chat log: ")
        self.text_area.config(state='disabled')

        # The textbox widget at bottom  
        convo_frame = tk.Frame(master=self, width= 400, bg = '#f2dbde')
        convo_frame.pack(fill=tk.X, side=tk.TOP, expand=False)
        
       
        
        scroll_bar = tk.Frame(master=convo_frame, bg="blue", width=10)
        scroll_bar.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        
        self.convo_editor = tk.Text(convo_frame, width=0, height = 8, bg = '#f2dbde')
        self.convo_editor.pack(fill=tk.X, side=tk.BOTTOM, expand=False)

        convo_editor_scrollbar = tk.Scrollbar(master=scroll_bar, command=self.convo_editor.yview)
        self.convo_editor['yscrollcommand'] = convo_editor_scrollbar.set
        convo_editor_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False, padx=0, pady=0)


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the footer portion of the root frame.
"""
class Footer(tk.Frame):
    def __init__(self, root, save_callback=None, online_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._save_callback = save_callback
        self._online_callback = online_callback
        # IntVar is a variable class that provides access to special variables
        self.is_online = tk.IntVar()
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Footer instance 
        self._draw()
    
    """
    Calls the callback function specified in the online_callback class attribute, if
    available, when the chk_button widget has been clicked.
    """
    def online_click(self):
        '''Check if the online button is clicked by calling callback function and getting is_online.'''
        if self.online_click is not None:
            self._online_callback(self.is_online.get())

    """
    Calls the callback function specified in the save_callback class attribute, if
    available, when the save_button has been clicked.
    """
    def save_click(self):
        if self._save_callback is not None:
            self._save_callback()

    """
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        save_button = tk.Button(master=self, text="Send Message", width=20)
        save_button.configure(command=self.save_click)
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)

"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the main portion of the root frame. Also manages all method calls for
the NaClProfile class.
"""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        # Initialize a new NaClProfile and assign it to a class attribute.
        self._direct_messenger = DirectMessenger(ds_client.HOST, username='codingcowgirls101',password='ccproduct12')
        
        self._is_online = False
        self._profile_filename = None
        self.file_path = None
        #self.chosencontact = None
        self.newcontact = None

        # After all initialization is complete, call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    """
    Creates a new DSU file when the 'New' menu item is clicked.
    """
    def new_profile(self):
        filename = tk.filedialog.asksaveasfile(filetypes=[('Distributed Social Profile', '*.dsu')])
        self._profile_filename = filename.name
        self.file_path = Path(self._profile_filename)
        self._direct_messenger.dm.profile.dsuserver= ds_client.HOST
        self._direct_messenger.dm.profile.username = 'codingcowgirls101'
        self._direct_messenger.dm.profile.password = 'ccproduct12'
        self._direct_messenger.dm.profile.save_profile(self.file_path)
        self.body.reset_ui()
    
    """
    Opens an existing DSU file when the 'Open' menu item is clicked and loads the profile
    data into the UI.
    """
    def open_profile(self):
        filename = tk.filedialog.askopenfile(filetypes=[('Distributed Social Profile', '*.dsu')])
        print(filename)
        self._profile_filename = filename.name
        self.file_path = Path(self._profile_filename)
        self._direct_messenger.dm.profile.load_profile(self._profile_filename)
        self.body.reset_ui()
        print("contact conversations")
        conversations, contacts = self._direct_messenger.dm.create_convos()
        self.body.set_messages(conversations, contacts)

    """
    Closes the program when the 'Close' menu item is clicked.
    """
    def close(self):
        self.root.destroy()

    def publish(self, message:Message, recipient):
        '''Send post to server and update widgets.'''
        main.update()
        self._direct_messenger.send(message,recipient)
    
    """
    Saves the text currently in the entry_editor widget to the active DSU file.
    """
    def save_profile(self):
        global chosencontact
        message = self.body.get_text_entry()
        self.publish(message, chosencontact)
        DM = self._direct_messenger.dm.create_dm() 
        self.body.insert_message(DM) #dictionary dm
        self._direct_messenger.dm.profile.save_profile(self.file_path)
        print("\nmessage sent")
        self.body.convo_editor.delete(0.0,'end')
    
    def timer_checkmail(self):
        msglst = self._direct_messenger.retrieve_new()
        conversations, contacts = self._direct_messenger.dm.create_convos()
        for contact in contacts:
            self.body.insert_contact(contact)
        self.body._messages = conversations
        for msg in msglst:
            sender = msg['from']
            self.footer.set_status(f"New message from {sender}")
        self.root.after(5000, self.timer_checkmail)
		

    """
    A callback function for responding to changes to the online chk_button.
    """
    def online_changed(self, value:bool):
        self._is_online = value
        if value == 1:
            self.footer.set_status("Dark Mode")
        else:
            self.footer.set_status("Light Mode")

    def new_contact(self):
        msg = tk.Tk()
        msg.withdraw()
        self.newcontact = tk.simpledialog.askstring("New Contact", "Please enter a new contact", parent=msg)
        self.body.insert_contact(self.newcontact)
    
    def choose_recipient(self): #get rid of soon
        global chosencontact
        msg = tk.Tk()
        msg.withdraw()
        chosencontact = tk.simpledialog.askstring("Choose Contact", "Enter contact to message", parent=msg)

    """
    Call only once, upon initialization to add widgets to root frame
    """
    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_contacts = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.new_profile)
        menu_file.add_command(label='Open...', command=self.open_profile)
        menu_file.add_command(label='Close', command=self.close)
        menu_bar.add_cascade(menu=menu_contacts, label='Contacts')
        menu_contacts.add_command(label='Add New', command=self.new_contact)#self.add_contact)
        menu_contacts.add_command(label='Choose Contact', command=self.choose_recipient)
        # NOTE: Additional menu items can be added by following the conventions here.
        # The only top level menu item is a 'cascading menu', that presents a small menu of
        # command items when clicked. But there are others. A single button or checkbox, for example,
        # could also be added to the menu bar. 

        # The Body and Footer classes must be initialized and packed into the root window.
        self.body = Body(self.root, self._direct_messenger)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        # TODO: Add a callback for detecting changes to the online checkbox widget in the Footer class. Follow
        # the conventions established by the existing save_callback parameter.
        # HINT: There may already be a class method that serves as a good callback function!
        self.footer = Footer(self.root, save_callback=self.save_profile, online_callback=self.online_changed)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("Coding Cowgirls Chat")

    # This is just an arbitrary starting point. You can change the value around to see how
    # the starting size of the window changes. I just thought this looked good for our UI.
    main.geometry("720x480")

    # adding this option removes some legacy behavior with menus that modern OSes don't support. 
    # If you're curious, feel free to comment out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the widgets used in the program.
    # All of the classes that we use, subclass Tk.Frame, since our root frame is main, we initialize 
    # the class with it.
    app = MainApp(main)
    # When update is called, we finalize the states of all widgets that have been configured within the root frame.
    # Here, Update ensures that we get an accurate width and height reading based on the types of widgets
    # we have used.
    # minsize prevents the root window from resizing too small. Feel free to comment it out and see how
    # the resizing behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    # And finally, start up the event loop for the program (more on this in lecture).
    main.after(5000, app.timer_checkmail)
    main.mainloop()
