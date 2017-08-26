
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil, os, stat, time
from datetime import timedelta
from datetime import datetime

#Define class

class ParentWindow(Frame):
    #Frame is the Tkinter frame class that our own class will inherit from

        def __init__(self, master):
            #Initialize your class and Tkinter master-level frame

            #define the master frame configuration
            self.master = master
            self.master.minsize(500, 300) #height, width
            self.master.title("Daily Transfer") #window title
            self.master.configure(background="#deafea") #background color

            #define expected input type for Entry widget
            self.t1 = StringVar()
            self.t2 = StringVar()

            #create & name 1st Button widget
            self.button1 = ttk.Button(self.master, text = "Whence come the files?", width =
                                      30, command = self.inputFolder)#appearance & function
            self.button1.pack()
            
            #create & name 1st Entry widget
            self.txt1 = ttk.Entry(self.master, textvariable=self.t1)#parent 
            self.txt1.pack()

            #create & name 2nd Button widget
            self.button2 = ttk.Button(self.master, text = "Whither go the files?", width = 30,
                                      command = self.outputFolder)#appearance & function
            self.button2.pack()

            #create & name 2nd Entry widget
            self.txt2 = ttk.Entry(self.master, textvariable = self.t2)
            self.txt2.pack()

            #create & name 3rd Button widget
            self.button3 = ttk.Button(self.master, text = "Transfer!",
                                      width = 30, command = self.transfer)#appearance & function
            self.button3.pack()

        def inputFolder(self): #button1 function
            folderInput = filedialog.askdirectory() #use fileDialog module to access designated source path
            print("folderInput: {}".format(folderInput)) #print source path
           
            self.t1.set(folderInput) #set source path for transfer function

        def outputFolder(self): #button2 function
            folderOutput = filedialog.askdirectory() #use fileDialog module to access designated dest path
            print("folderOutput: {}".format(folderOutput)) #print destination path
           
            self.t2.set(folderOutput) #set dest path for transfer function

        def transfer(self): #button3 function
            now = datetime.now()
            fileFrom = self.t1.get() #create variable for source path
            fileTo = self.t2.get() #create variable for dest path
            today = datetime.today()
            last24Hours = str(today - timedelta(days = 1))

            
            sourceFiles = os.listdir(fileFrom)    
            for file in sourceFiles:
                if file.endswith(".txt"):
                    timeModified = datetime.fromtimestamp(os.path.getmtime(fileFrom + '/'+ file))
                    timeDiff = (now - timeModified)
                    if timeDiff > timedelta(days=1):
                        print (file, '\n' ,timeDiff, "\nStatus: Old\n")
                    else:
                        print (file, '\n' ,timeDiff, "\nStatus: New\n")
                        shutil.copy(fileFrom + '/' + file, fileTo)
                    

                    

#Python looks here first and runs the functions that fall below this line.

def main():

    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
if __name__ == "__main__": main()
