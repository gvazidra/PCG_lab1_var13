# PCG_lab1_var13
Color Models Converter
This application provides a graphical user interface (GUI) for converting colors between three color models: RGB, CMYK, and XYZ. Users can input color values in any of the models and get real-time updates in the other models. Additionally, the application allows users to choose a color using a color picker and see the corresponding values across all models.

Features
Convert between RGB, CMYK, and XYZ color models.
Real-time updates as you change color values.
Integrated color picker to select a color and get its corresponding values in RGB, CMYK, and XYZ.
Notifications for any rounding of values during conversions.
Interactive GUI with sliders and input fields for adjusting color values.

Requirements
Python 3.x
Tkinter (built-in with Python's standard library)

How to Use
1. Launching the Application
To launch the application, open main.exe file.

2. User Interface
The main application window is divided into sections for each color model (RGB, CMYK, XYZ), with corresponding sliders and input fields.

RGB Section
R, G, and B sliders allow you to adjust Red, Green, and Blue values from 0 to 255.
Alternatively, you can manually enter values for R, G, and B in the text fields.
CMYK Section
C, M, Y, and K sliders allow you to adjust Cyan, Magenta, Yellow, and Black values from 0 to 100.
You can also manually input values in the respective fields.
XYZ Section
X, Y, and Z sliders allow you to adjust the values of the XYZ color space (range 0-100).
Manual input is also supported in the text fields.
Color Picker
Click on the "Choose Color" button to open a color picker.
Select a color, and the application will automatically update the values for RGB, CMYK, and XYZ.
Color Display
The selected color is displayed in a square on the screen. As you change the color values, the square updates in real-time to reflect the color.
3. Converting Colors
When you adjust any color model (RGB, CMYK, or XYZ), the application automatically updates the values in the other two models.
If any values are rounded during conversion, the application will notify you with a message.
4. Error Handling
If you enter a value outside of the valid range (0-255 for RGB, 0-100 for CMYK and XYZ), an error message will appear, prompting you to enter a valid value.

Code Overview
Functions
rgb_to_xyz(r, g, b): Converts RGB values to the XYZ color model.
xyz_to_rgb(x, y, z): Converts XYZ values to the RGB color model.
rgb_to_cmyk(r, g, b): Converts RGB values to the CMYK color model.
cmyk_to_rgb(c, m, y, k): Converts CMYK values to the RGB color model.
update_entries(r, g, b, c, m, y, k, x, yy, z): Updates all input fields and sliders based on the current color model values.
update_color_from_rgb(): Updates the color based on RGB values.
update_color_from_cmyk(): Updates the color based on CMYK values.
update_color_from_xyz(): Updates the color based on XYZ values.
open_color_chooser(): Opens a color picker dialog.
update_color_square(r, g, b): Updates the displayed color square with the selected color.
Example Usage
Adjust the RGB sliders or enter values directly to see the corresponding CMYK and XYZ values.
Use the CMYK sliders to adjust Cyan, Magenta, Yellow, and Black, and watch as the RGB and XYZ values update.
Choose a color using the "Choose Color" button to set its RGB, CMYK, and XYZ equivalents.
The color square on the right side will update to show the selected color in real-time.

