import time
import pynput
import tkinter as tk
import threading

#* Settings:
#* target_x
#* target_y
#* set_pos
#* return_cursor
#* milliseconds
#* enabled

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.configure(bg = "#2b5b84")
    root.geometry("253x205")
    root.resizable(0, 0)
    root.title("TA")
    running = False
    first_run = True
    click = 0

    target_x_list = [0]
    target_y_list = [0]
    milliseconds_list = [0]
    num_of_clicks_list = [1]
    set_pos_list = [0]
    return_cursor_list = [0]
    enabled_list = [0]

def update_button_callback():
    target_x_list[click] = int(target_x_entry.get())
    target_y_list[click] = int(target_y_entry.get())
    milliseconds_list[click] = int(milliseconds_entry.get())
    num_of_clicks_list[click] = int(num_of_clicks_entry.get())
    
    set_pos_list[click] = set_pos_value.get()
    return_cursor_list[click] = return_cursor_value.get()
    enabled_list[click] = enabled_value.get()

def backwards_button_callback():
    global click
    if click > 0:
        click -= 1
    click_display.configure(text = f"Click: {click}")
    set_entry(target_x_entry, target_x_list[click])
    set_entry(target_y_entry, target_y_list[click])
    set_entry(milliseconds_entry, milliseconds_list[click])
    set_entry(num_of_clicks_entry, num_of_clicks_list[click])
    
    global set_pos_value
    global return_cursor_value
    global enabled_value
    
    set_pos_value.set(set_pos_list[click])
    return_cursor_value.set(return_cursor_list[click])
    enabled_value.set(enabled_list[click])

def set_entry(entry, string):
    """
    Quick and small function that just lets me set entries faster.
    """
    entry.delete(0, tk.END)
    entry.insert(0, string)

def forwards_button_callback():
    """
    Callback for the forwards button.
    1: Changes the click display label.
    2: If the new click has not been seen before. It has default settings added to the settings arrays.
    3: Sets the entries to be the new values.
    """
    global click
    click += 1
    click_display.configure(text = f"Click: {click}") # 1
    if len(target_x_list) <= click: # 2
        target_x_list.append(0)
        target_y_list.append(0)
        milliseconds_list.append(0)
        num_of_clicks_list.append(1)
        set_pos_list.append(0)
        return_cursor_list.append(0)
        enabled_list.append(0)
    set_entry(target_x_entry, target_x_list[click]) # 3
    set_entry(target_y_entry, target_y_list[click])
    set_entry(milliseconds_entry, milliseconds_list[click])
    set_entry(num_of_clicks_entry, num_of_clicks_list[click])
    global set_pos_value
    global return_cursor_value
    global enabled_value
    
    set_pos_value.set(set_pos_list[click])
    return_cursor_value.set(return_cursor_list[click])
    enabled_value.set(enabled_list[click])

def on_press(key):
    """This function is used by Pynput to let me start and stop the program while Tkinter is running."""
    if str(key) == "Key.f6":
        global running
        global first_run
        running = not running
        start_program()
        # if first_run:
        #     firstRun = False
        #     start_program()

if __name__ == "__main__":
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    
    

    set_pos_value = tk.IntVar()
    return_cursor_value = tk.IntVar()
    enabled_value = tk.IntVar()

    target_x_label = tk.Label(text = "Target (X)", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    target_x_entry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

    target_y_label = tk.Label(text = "Target (Y)", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    target_y_entry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

    milliseconds_label = tk.Label(text = "Ms", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    milliseconds_entry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

    num_of_clicks_label = tk.Label(text = "# Of Clicks", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    num_of_clicks_entry = tk.Entry(borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")

    set_pos_label = tk.Label(text = "Set Position", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    set_pos_check_button = tk.Checkbutton(var = set_pos_value, borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84")

    return_cursor_label = tk.Label(text = "Return Cursor", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    return_cursor_check_button = tk.Checkbutton(var = return_cursor_value, borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84")

    current_mouse_coordinates_label = tk.Label(text = "", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    
    enabled_check_button = tk.Checkbutton(text = "Enabled", var = enabled_value, borderwidth = 2, relief = "groove", bg = "#FFD43B", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84")
    
    update_button = tk.Button(text = "Save Settings", borderwidth = 2, relief = "groove", bg = "#FFD43B", fg = "#2b5b84", activebackground = "#FFD43B", activeforeground = "#2b5b84", command = update_button_callback)
    
    backwards_button = tk.Button(text = "Previous Click", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea", command = backwards_button_callback, activebackground = "#FFD43B", activeforeground = "#2b5b84")
    
    forward_button = tk.Button(text = "Next Click", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea", command = forwards_button_callback, activebackground = "#FFD43B", activeforeground = "#2b5b84")
    
    click_display = tk.Label(text = "Click: 0", borderwidth = 2, relief = "groove", bg = "#4B8BBE", fg = "#e6e8ea")
    # * -----------------------------------------

    target_x_label.grid(row = 0, column = 0)
    target_x_entry.grid(row = 1, column = 0)
    target_x_entry.insert(0, "0")

    target_y_label.grid(row = 0, column = 1)
    target_y_entry.grid(row = 1, column = 1)
    target_y_entry.insert(0, "0")

    milliseconds_label.grid(row = 2, column = 0)
    milliseconds_entry.grid(row = 3, column = 0)
    milliseconds_entry.insert(0, "0")

    num_of_clicks_label.grid(row = 2, column = 1)
    num_of_clicks_entry.grid(row = 3, column = 1)
    num_of_clicks_entry.insert(0, "1")

    set_pos_label.grid(row = 4, column = 0)
    set_pos_check_button.grid(row = 5, column = 0)

    return_cursor_label.grid(row = 4, column = 1)
    return_cursor_check_button.grid(row = 5, column = 1)

    current_mouse_coordinates_label.grid(row = 6, column = 0)
    
    enabled_check_button.grid(row = 6, column = 1)
    
    update_button.grid(row = 7, column = 1)
    
    forward_button.grid(row = 8, column = 1)
    
    backwards_button.grid(row = 8, column = 0)
    
    click_display.grid(row = 7, column = 0)
    
    def on_move(x, y):
        current_mouse_coordinates_label.config(text = f"({x}, {y})")
    listener2 = pynput.mouse.Listener(on_move=on_move)
    listener2.start()

def start_program():
    mouse = pynput.mouse.Controller()
    # target_x = int(target_x_entry.get())
    # target_y = int(target_y_entry.get())
    # ms = int(milliseconds_entry.get())
    # num_of_clicks = int(num_of_clicks_entry.get())
    
    # set_pos = set_pos_value.get()
    # return_cursor = return_cursor_value.get()
    global running
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    
    while True:
        if running:
            for i in range(len(target_x_list)):
                if enabled_list[i]:
                    target_x = target_x_list[i]
                    target_y = target_y_list[i]
                    ms = milliseconds_list[i]
                    num_of_clicks = num_of_clicks_list[i]
                    set_pos = set_pos_list[i]
                    return_cursor = return_cursor_list[i]
                    
                    if set_pos:
                        oldPos = mouse.position
                        mouse.position = (target_x, target_y)
                    mouse.click(pynput.mouse.Button.left, num_of_clicks)
                    if set_pos:
                        mouse.position = oldPos
                    if ms != 0:
                        time.sleep(ms / 1000)
        else:
            break #! It just.. works, alright?

if __name__ == "__main__":
    root.mainloop()