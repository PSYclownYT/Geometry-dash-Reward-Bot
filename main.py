import pyautogui
from time import sleep
import subprocess
gdpath = input('ayo whats your gd path bruv')

subprocess.Popen(gdpath, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import io
import sys
import time

def try_until_success(func, *args, **kwargs):
    target_message = "pyautogui.ImageNotFoundException"
    
    while True:
        # Capture output printed to the console
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout
        
        try:
            # Attempt to run the function
            result = func(*args, **kwargs)
            output = captured_output.getvalue()
            
            # Check if the specific error message is in the output
            if output.__contains__(target_message):
                raise ValueError("ImageNotFoundException printed")
                
            break  # Exit loop if no error or message is found
            
        except Exception as e:
            print(f"Error encountered: {e}. Retrying...")
            time.sleep(1)  # Wait 1 second between attempts for safety
        finally:
            sys.stdout = sys.__stdout__  # Reset stdout
    
    return result




def fandclick(path):
    button7location = pyautogui.locateOnScreen(path,confidence=0.8) # returns (left, top, width, height) of matching region
    button7location
    (1416, 562, 50, 41)
    buttonx, buttony = pyautogui.center(button7location)
    buttonx, buttony
    (1441, 582)
    pyautogui.click(buttonx, buttony)
    if 'button7location' in locals():
        return True

time.sleep(10)


    
gd = pyautogui.getWindowsWithTitle(title='Geometry Dash')
print(gd) 


if True:
    fandclick('icons\daily.png')
    sleep(1)  # clicks the center of where the button was found
    fandclick('icons\smallchest.png')
    sleep(3)
    fandclick('icons\ok.png')