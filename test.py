from tkinter import *

def handle_click(event):
    global click_var
    if event.x > 100 and event.y > 100:  # Check if the click occurs in a specific region
        click_var.set(1)  # Set the variable to indicate the desired click event occurred

#Create game window
gameWindow=Tk(screenName="Briscola",className="Briscola")
gameWindow.geometry('300x200')

# Create an IntVar variable
click_var = IntVar()

# Bind the click event to the frame widget
gameWindow.bind("<Button-1>", handle_click)

# Wait until the variable is set
gameWindow.wait_variable(click_var)

# Perform further actions after the desired click event
print("Clicked on the desired region!")

# Start the tkinter event loop
gameWindow.mainloop()
