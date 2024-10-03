# Anti-AFK Script for GarnetGaming DarkRP

## Overview

This script is designed to help avoid the anti-AFK system on the GarnetGaming DarkRP server by simulating user movement within the Garry's Mod window. It works by sending key press events to the game window, simulating circular movement with the WASD keys.

The script is packaged as a `.exe` file using PyInstaller for easy use without requiring any installation/pre-requisites.

## How It Works

1. **Window Detection:** The script searches for the Garry's Mod window by title.
2. **Simulated Key Presses:** Once Garry's Mod is found, it simulates pressing the `W`, `A`, `S`, and `D` keys in sequence, mimicking circular movement.
3. **Key Sending:** Keys are sent directly to the Garry's Mod window, making it appear that the player is still active.

## Features

- Detects the Garry's Mod window automatically.
- Simulates circular movement with the `W`, `A`, `S`, and `D` keys.
- Runs indefinitely until manually stopped.
- Lightweight and easy to use.

## Installation

1. Download the latest `.exe` release from the [Releases](#) section.
2. Run the `.exe` file (no installation needed).

## Usage

1. Start Garry's Mod and connect to the DarkRP server.
2. Run the `.exe` file.
3. The script will detect the Garry's Mod window and start sending simulated keypresses to avoid the anti-AFK slay/kill system.
4. Press `Ctrl + C` in the terminal to stop the script.

## Requirements

- Windows OS
- Garry's Mod (windowed or fullscreen)
  
The script uses the following Python libraries, which are bundled in the `.exe`, so no need to download them if running the `.exe` instead of the `.py`:

- `pygetwindow` for window handling
- `win32api`, `win32con`, and `win32gui` for simulating keypresses

## Disclaimer

This script is intended for personal use to avoid being kicked by anti-AFK systems in DarkRP. Please use it responsibly and ensure it complies with the server's rules. I am not responsible for anything that may come of you using this!
