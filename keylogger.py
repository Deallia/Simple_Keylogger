import pynput.keyboard

keyboard_listener = pynput.keyboard.Listener


def process_key_press(key):
    print(key)



keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

# Start listening for key presses
keyboard_listener.start()


