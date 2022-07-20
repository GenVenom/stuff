from concurrent.futures import thread
import keyboard
import time
from threading import Timer

def num_to_letters():
    if current_key['key'] != None:
        ascii_code = ascii_map[current_key['key']]
        keyboard.write(chr(ascii_code+current_key['key_count'] - 1))
        
        current_key['key'] = None 
        current_key['key_count'] = 0

    
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function()
        

timer = RepeatTimer(2,num_to_letters)
timer.start()



allowed_keys = [i for i in range (2,9)]

current_key = {
    
    'key': None,
    'key_count': 0,
}

ascii_map = {
    2: 65,
    3:68,
    4:71,
    5:74,
    6:77,
    7:80,
    8:83,
    9:86

}

def get_keystroke(event):
    try:
        if int(event.name) in allowed_keys:
            current_key['key'] = int(event.name)
            current_key['key_count'] += 1
            #print(current_key['key_count'])
            
            
            if current_key['key_count'] == 3:
                num_to_letters()
    except:
        pass
    



def main():
    keyboard.on_press(get_keystroke,suppress=True)
    keyboard.press("BACKSPACE")
    time.sleep(0.1)
    

main()

