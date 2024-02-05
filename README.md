# Change Wallpaper
This Python script allows you to change your wallpaper in Windows. It utilizes the `ctypes` library to call the `SystemParametersInfoW` function from the `user32` library.

## Usage
1. Ensure you have Python installed on your system.
2. Download the `Change Wallpaper.py` file.
3. Modify the `path` variable in the script to point to the location of the image file you want to set as your wallpaper.
4. Run the script.

python
import ctypes

# Modify the path variable to point to the location of your image file
path = "KJ.jpg"

# Call SystemParametersInfoW to set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

## Notes
- Ensure that the path to the image file is correct and accessible.
- The script only works on Windows systems.
- This script sets the wallpaper temporarily. If you restart your system, you may need to run the script again to set the wallpaper.

Feel free to contribute and improve this script!
