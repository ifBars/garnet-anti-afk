import time
import pygetwindow as gw
import win32api
import win32con
import win32gui
import win32process  # Import win32process for process information

def get_gmod_windows():
    """Get a list of window handles for all Garry's Mod instances along with their PIDs."""
    gmod_windows = []
    windows = gw.getAllTitles()
    for window_title in windows:
        if "Garry's Mod" in window_title:
            window = gw.getWindowsWithTitle(window_title)[0]
            hwnd = window._hWnd
            # Get the PID using win32process
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            gmod_windows.append((window, pid))  # Store tuple of (window, pid)
    return gmod_windows

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

def choose_window(gmod_windows):
    """Allow the user to choose a Garry's Mod window from a list, displaying title and PID."""
    print("Available Garry's Mod windows:")
    for i, (window, pid) in enumerate(gmod_windows):
        print(f"{i + 1}: {window.title} (PID: {pid})")
    
    while True:
        try:
            choice = int(input("Select a window number (or 0 to exit): "))
            if choice == 0:
                print("Exiting...")
                return None
            if 1 <= choice <= len(gmod_windows):
                return gmod_windows[choice - 1][0]._hWnd  # Return the window handle
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Anti-AFK script started. Press Ctrl+C to stop.")
    gmod_windows = get_gmod_windows()
    if not gmod_windows:
        print("Could not find any Garry's Mod windows.")
        return
    
    hwnd = choose_window(gmod_windows)
    if hwnd is None:
        return

    while True:
        move_in_circle(hwnd)
        time.sleep(1)

if __name__ == "__main__":
    main()
