import os
import shutil
import getpass


def Movelol():
    username = getpass.getuser()
    source = f"C:/Users/{username}/AppData/Roaming/Microsoft Flight Simulator/Packages/Community"
    destination = f"C:/Users/{username}/AppData/Roaming/AddonMover"

    file_names = os.listdir(source)
    for file_name in file_names:
        shutil.move(os.path.join(source, file_name), destination)