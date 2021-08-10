
import tkinter as tk
import getpass
import os
#from os import *
#from tkinter import *
import shutil
import os.path
from tkinter import messagebox
import subprocess
from tkinter import ttk
from tkinter.messagebox import askyesno


root = tk.Tk()
root.title("AddonMover")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (800/2))
y_cordinate = int((screen_height/2) - (500/2))
root.geometry("{}x{}+{}+{}".format(800, 500, x_cordinate, y_cordinate))

def nocommunnity():
    messagebox.showerror("Error","No Community folder found")

def nobackupdata():
    messagebox.showerror("Error","No Addons to Backup")

def notinstallederror():
    messagebox.showerror("Error","AddonMover is not installed on your Computer")
    
def openmsfs():
    subprocess.call(f"C:/Program Files (x86)/Steam/steamapps/common/MicrosoftFlightSimulator/FlightSimulator.exe")
    print("Launched MSFS2020 sucessfully✔")
    
def installaddonmover():
    username = getpass.getuser()
    if os.path.isdir(f"C:/Users/{username}/AppData/Roaming/AddonMover"):
        messagebox.showerror("Error","AddonMover is already installed on your computer")
        print("AddonMover is already installed❌")
    else:
        username = getpass.getuser()
        os.mkdir(f"C:/Users/{username}/AppData/Roaming/AddonMover")
        print("AddonMover was sucessfully installed!✔")

def killapp():
    root.destroy()

def move():
    username = getpass.getuser()
    AddonMover = f"C:/Users/{username}/AppData/Roaming/AddonMover"
    if os.path.isdir(AddonMover):
        if len(os.listdir(AddonMover)) == 0:
            source = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"
            destination = f"C:/Users/{username}/AppData/Roaming/AddonMover"

            file_names = os.listdir(source)
            for file_name in file_names:
                shutil.move(os.path.join(source, file_name), destination)
            
            print("Moved Addons sucessfully✔")
        else:
            username = getpass.getuser()
            source = f"C:/Users/{username}/AppData/Roaming/AddonMover"
            destination = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"

            file_names = os.listdir(source)
            for file_name in file_names:
                shutil.move(os.path.join(source, file_name), destination)
            
            print("Moved Addons sucessfully✔")
    
    else: messagebox.showerror("Addonmover", "You must first install Addonmover!")

def uninstall():
    username = getpass.getuser()
    AddonMover = f"C:/Users/{username}/AppData/Roaming/AddonMover"
    Community = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"

    messagebox.showinfo("AddonMover", "If you you still have some Addons in the AddonMover folder, AddonMover will automatically move them into your community folder")
    
    if len(os.listdir(AddonMover)) == 0:
        os.rmdir(AddonMover)

    else: 
        username = getpass.getuser()
        source = f"C:/Users/{username}/AppData/Roaming/AddonMover"
        destination = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"

        file_names = os.listdir(source)
        for file_name in file_names:
            shutil.move(os.path.join(source, file_name), destination)

        os.rmdir(AddonMover)

        messagebox.showinfo("AddonMover", "AddonMover was uninstalled sucessfully")
        print("uninstalled AddonMover sucessfully")

    
            
            
            
            


def addonbackup():
    messagebox.showinfo("AddonMover", "The Backup Function will Backup Addons from the Community folder AND the AddonMover folder.")
    username = getpass.getuser()
    AddonMover = f"C:/Users/{username}/AppData/Roaming/AddonMover"
    Community = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"
    
    if os.path.isdir(AddonMover):
        if len(os.listdir(AddonMover)) == 0:
            if os.path.isdir(Community):
                if len(os.listdir(Community)) == 0:
                    messagebox.showerror("AddonMover", "No Addons to Backup found! AddonMover will Backup Addons that are either inside your Community folder, or inside the AddonMover folder.")
                
                else:
                    username = getpass.getuser()
                    os.mkdir(f"C:/Users/{username}/AppData/Roaming/AddonMoverBackup")
                    destination = f"C:/Users/{username}/AppData/Roaming/AddonMoverBackup"
                    file_names = os.listdir(Community)
                    for file_name in file_names:
                        shutil.copy(os.path.join(Community, file_name), destination)

            else: messagebox.showerror("Addonmover", "Oh no, Something went wrong... No Community folder found!")
    
        else: 
            username = getpass.getuser()
            os.mkdir(f"C:/Users/{username}/AppData/Roaming/AddonMoverBackup")
            source = f"C:/Users/{username}/AppData/Roaming/AddonMover"
            destination = f"C:/Users/{username}/AppData/Roaming/AddonMoverBackup"

            file_names = os.listdir(source)
            for file_name in file_names:
                shutil.copy(os.path.join(source, file_name), destination)
    
    else: messagebox.showerror("Addonmover", "No AddonMover folder found, you must first install Addonmover!")
                


        
Close = tk.Button(root, text="Close", command=killapp)
Install = tk.Button(root, text="Install AddonMover", command=installaddonmover())
Launch = tk.Button(root, text="Launch MSFS2020", command=openmsfs)
Move = tk.Button(root, text="Move", command=move())
uninstall = tk.Button(root, text="uninstall AddonMover", command=uninstall())
Backup = tk.Button(root, text="Backup Addons", command=addonbackup())



Install.pack()
Close.pack()
Move.pack()
Launch.pack()
uninstall.pack()

root.mainloop()
                                    