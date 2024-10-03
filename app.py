import time
import pygetwindow as gw
import win32api
import win32con
import win32gui

def get_gmod_window():
    """Get the window handle for Garry's Mod."""
    windows = gw.getAllTitles()
    for window_title in windows:
        if "Garry's Mod" in window_title:
            return gw.getWindowsWithTitle(window_title)[0]
    return None

def send_key_to_window(hwnd, key):
    """Send a key press event to the specified window."""
    scan_code = win32api.MapVirtualKey(key, 0)

    # Send WM_KEYDOWN
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, (scan_code << 16) | 1)
    time.sleep(0.5)  # Simulate key hold time

    # Send WM_KEYUP
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, (scan_code << 16) | (1 << 31) | 1)

def move_in_circle(hwnd):
    """Simulates circular movement by sending WASD keys to Garry's Mod window."""
    # Virtual key codes for W, A, S, D
    keys = [0x57, 0x41, 0x53, 0x44]  # W, A, S, D
    for key in keys:
        send_key_to_window(hwnd, key)
        time.sleep(0.2)  # Delay between key presses

def main():
    print("Anti-AFK script started. Press Ctrl+C to stop.")
    gmod_window = get_gmod_window()
    if not gmod_window:
        print("Could not find Garry's Mod window.")
        return
    else:
        print("Found Garry's Mod window.")
    
    hwnd = gmod_window._hWnd
    while True:
        move_in_circle(hwnd)
        time.sleep(1)

if __name__ == "__main__":
    main()
