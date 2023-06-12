# Importing libraries. tkinter for the gui, winsound for my open and close sounds, atexit for exiting, and sys module
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog
import tkinter.messagebox
import winsound
import atexit
import sys

class Window:
    def __init__(self, master=None):
        self.master = master  # Assign the provided 'master' argument to the 'self.master' attribute
        self.master.geometry('991x555')  # Sets window size to '991x555' pixels
        self.master.title("LCARS PAD")  # Seting the window title to "LCARS PAD"

        img = Image.open('Lcars3.png')  # Open the image file 'Lcars3.png' for usage as the background
        tk_img = ImageTk.PhotoImage(img)  # This converts the image to a "PhotoImage" using ImageTk

        background_label = tk.Label(self.master, image=tk_img)  # Create a label with the image above
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # This places the label on the window
        background_label.image = tk_img  # Reference the image

        self.textspace = []  # Creates the empty list for the text space and for user input.

        self.textspace = tk.Text(self.master, bg='black', fg='white', font=("Swiss 911 Ultra Compressed", 12), highlightthickness=1)  # Create a text widget using the font the NCC1701D uses
        self.textspace.place(x=237, y=267, width=650, height=255)  # Place the text widget on the window in my specified location
        self.textspace.insert(tk.END, "Insert text here Captain.") # Temp text to let the user know where to type in the program

        # Creates the menubar at the top
        menubar = tk.Menu(self.master)

        # Creates the File menu in the menubar at the top
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.newfile)  # Adds New command
        filemenu.add_command(label="Open", command=self.openfile)  # Adds Open command
        filemenu.add_command(label="Save", command=self.savefile)  # Adds Save command
        filemenu.add_separator()  # Adds separator line
        filemenu.add_command(label="Quit", command=self.quit_program)  # Adds Quit command

        # Adds File to the menubar
        menubar.add_cascade(label="File", menu=filemenu)

        # Attaches the menubar to the tkinter window
        self.master.config(menu=menubar)

        # Used for loading images for the buttons
        new_image = ImageTk.PhotoImage(Image.open("New.png"))  # Load the image for the "New" button
        open_image = ImageTk.PhotoImage(Image.open("Open.png"))  # Load the image for the "Open" button
        save_image = ImageTk.PhotoImage(Image.open("Save.png"))  # Load the image for the "Save" button
        about_image = ImageTk.PhotoImage(Image.open("About.png"))  # Load the image for the "About" button
        quit_image = ImageTk.PhotoImage(Image.open("Quit.png"))  # Load the image for the "Quit" button

        # Creates buttons with the above images
        new_button = tk.Button(self.master, image=new_image, bd=0, highlightthickness=0, relief='flat', command=self.newfile)  # Creates New button
        new_button.place(x=646, y=70)  # Places the button on the window
        new_button.image = new_image  # Referencing the image

        open_button = tk.Button(self.master, image=open_image, bd=0, highlightthickness=0, relief='flat', command=self.openfile)  # Creates Open button
        open_button.place(x=646, y=128)   # Places the button on the window
        open_button.image = open_image  # Referencing the image

        save_button = tk.Button(self.master, image=save_image, bd=0, highlightthickness=0, relief='flat', command=self.savefile)  # Creates Save button
        save_button.place(x=813, y=70)   # Places the button on the window
        save_button.image = save_image  # Referencing the image

        about_button = tk.Button(self.master, image=about_image, bd=0, highlightthickness=0, relief='flat', command=self.show_about_info)  # Creates About button
        about_button.place(x=813, y=128)   # Places the button on the window
        about_button.image = about_image  # Referencing the image

        quit_button = tk.Button(self.master, image=quit_image, bd=0, highlightthickness=0, relief='flat', command=self.quit_program)  # Creates Quit button
        quit_button.place(x=0, y=500)   # Places the button on the window
        quit_button.image = quit_image  # Referencing the image

        winsound.PlaySound("viewscreen_on.wav", winsound.SND_FILENAME)  # This plays the viewscreen on sound when the program starts - Sound from: https://www.101soundboards.com/boards/27996-star-trek-tng-the-next-generation-soundboard

    def newfile(self):
        confirmation = tk.messagebox.askyesno("Confirmation Required", "Captain, are you sure you want to create a new file?")  # Asks user for confirmation with a message box before making a new file and clearing the textbox
        if confirmation:
            self.textspace.delete(0.0, tk.END)  # If Y the textbox is cleared

    def savefile(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])  # Save file option for the user and can browse to a custom path/file location
        if file_path:
            filecontents = self.textspace.get(0.0, tk.END)  # Get textspace contents
            with open(file_path, 'w+') as file:
                file.write(filecontents)  # Write the contents to the file

    def openfile(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # Open file option
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.textspace.delete(0.0, tk.END)  
                    self.textspace.insert(0.0, file.read())  # Write/replace the contents of the textspace
            except FileNotFoundError:
                tk.messagebox.showerror("RED ALERT", "Captain, there seems to be an error. I cannot open or find the file.")  # If the file is not found it will display this error message to the user

    def show_about_info(self, event=None):
        tk.messagebox.showinfo("About", "Welcome to the NCC-1701D LCARS PAD application. Version 1.0. Created by David Gregory")  # Shows the about button info in a dialog box to the user

    def quit_program(self):
        confirmation = tk.messagebox.askyesno("Confirmation Required", "Captain, are you sure you want to quit?")  # Asks for confirmation using a message box and displaying to the user for response/input
        if confirmation:
            self.master.destroy()  # If the user picks Yes it will destroy the main window and exit the program

def on_program_exit():
    winsound.PlaySound("viewscreen_off.wav", winsound.SND_FILENAME)  # This plays the viewscreen off sound when the program exits - Sound from: https://www.101soundboards.com/boards/27996-star-trek-tng-the-next-generation-soundboard

def main():
    root = tk.Tk()  # Creates the main window for the program
    Window(root)  # Creates an instance of the window class
    root.protocol("WM_DELETE_WINDOW", on_program_exit)  # Sets the WM_DELETE_WINDOW protocol to call on_program_exit() when the window is closed
    root.mainloop()  # Starts the Tk event loop

if __name__ == "__main__":
    atexit.register(on_program_exit)  # Register on_program_exit() to be called on program exit
    main()  # Starts the program!
