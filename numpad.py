"""
Emulator of the old Nokia keyboard using Python 3.10.5.

Few known glitches:
1) Pressing 1 on the keyboard sometimes crashes the program
2) Pressing keys extremely rapidly might glitch the keyboard
3) Capslock is not supported

"""



import keyboard
import time
from threading import Timer
import subprocess

allowed_keys = [i for i in range (2,10)]

current_key = {
    'cycle' : 0,
    'previous_key': None,
    'key': None,
    'key_count': 0,
}

ascii_map = {
    2:[65,3],
    3:[68,3],
    4:[71,3],
    5:[74,3],
    6:[77,3],
    7:[80,4],
    8:[84,3],
    9:[87,4],
}

subprocess.Popen("notepad.exe")

def num_to_letters():
    if current_key['key'] != None:
        if current_key['key_count'] > ascii_map[current_key['key']][1]:
            keyboard.write(str(current_key['key']))
        else:
            ascii_code = ascii_map[current_key['key']][0]
            keyboard.write(chr(ascii_code+current_key['key_count'] - 1))
        
    
    current_key['previous_key'] = None
    current_key['key'] = None 
    current_key['key_count'] = 0
    current_key['cycle'] = 0

    
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function()
        

timer = RepeatTimer(2,num_to_letters)
timer.start()

def get_keystroke(event):

    if (event.name == "backspace"):
        keyboard.press("backspace")
        return 0    

    if current_key['cycle'] == 0:
        current_key['key'] = None
    else:
        current_key['key'] = int(event.name)

    if current_key['key'] == current_key['previous_key']:
        
        try:
            
            if int(event.name) in allowed_keys:
                current_key['key'] = int(event.name)
                current_key['key_count'] += 1
                current_key['previous_key'] = current_key['key']
                
                
                if current_key['key_count'] == ascii_map[current_key['key']][1] + 1:
                    num_to_letters()
                    current_key['previous_key'] = current_key['key']
    
            current_key['previous_key'] = current_key['key']
            current_key['cycle'] += 1

        except Exception as e:
            print(e)
            
    else:
       
        temp_key = current_key['key']
        current_key['key'] = current_key['previous_key']
        
        num_to_letters()
        current_key['key'] = temp_key
        current_key['key_count'] += 1

def main():
    keyboard.on_press(get_keystroke,suppress= True)
    time.sleep(0.1)
    
main()




