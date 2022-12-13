# ics-32-w22-final-project
ics-32-w22-final-project created by GitHub Classroom

DISCLAIMER: to successfully send messages back and forth two fully loaded dsu files and gui's must be up, or at least you must be messaging an existing profile. AKA must be messaging an existing user that is stored in a file.
When you run our program, you must open a new or existing profile. 
Then, you must select your contact and type your message into the text box and then click send when ready to send your
message. Our program will then send your message to the correct contact and update the chat log every 5 seconds which you
may see by reclicking the contact. You may add a contact by selecting “add contact” in the menu bar. 

When you select a contact, our program sets the recipient of the message to the selected contact. 
After typing a message into the box, when you click send, our program will convert the message into a dm which we 
append to the message list for each profile. Then, when we call get messages for each profile, we can get all the 
messages sent to and from the profile which we can store in the new conversation we created. This allows the messages 
between each contact to be easily accessed. Additionally, when you add a new contact, our program will update the tree 
of contacts to include the new contact as well as set the program up to receive and store any new messages. 

Our ds_messenger.py does a lot of the work by returning a list of messages when you call retrieve_new or retrieve_all, but
there are other function calls embedded within those functions to update the profile along the way or creating conversations, 
virtually the only thing that must be manually done by calling the name of the profile object is saving with the path.
