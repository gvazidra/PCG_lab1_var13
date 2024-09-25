#variant 13
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox


def rgb_to_xyz(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0

    r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4

    x = r * 0.412453 + g * 0.357580 + b * 0.180423
    y = r * 0.212671 + g * 0.715160 + b * 0.072169
    z = r * 0.019334 + g * 0.119193 + b * 0.950227

    x_rounded = round(x * 100)
    y_rounded = round(y * 100)
    z_rounded = round(z * 100)

    if x != x_rounded or y != y_rounded or z != z_rounded:
        notification_label.config(text="XYZ values have been rounded.")
    else:
        notification_label.config(text="")

    return x_rounded, y_rounded, z_rounded


def xyz_to_rgb(x, y, z):
    x /= 100.0
    y /= 100.0
    z /= 100.0

    r = x *  3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y *  1.8758 + z *  0.0415
    b = x *  0.0557 + y * -0.2040 + z *  1.0570

    r = 12.92 * r if r <= 0.0031308 else 1.055 * (r ** (1 / 2.4)) - 0.055
    g = 12.92 * g if g <= 0.0031308 else 1.055 * (g ** (1 / 2.4)) - 0.055
    b = 12.92 * b if b <= 0.0031308 else 1.055 * (b ** (1 / 2.4)) - 0.055

    r = r * 255
    g = g * 255
    b = b * 255

    r_rounded = round(r)
    g_rounded = round(g)
    b_rounded = round(b)

    if r != r_rounded or g != g_rounded or b != b_rounded:
        notification_label.config(text="RGB values have been rounded.")
    else:
        notification_label.config(text="")

    return round(max(0, min(255, r_rounded))), round(max(0, min(255, g_rounded))), round(max(0, min(255, b_rounded)))


def rgb_to_cmyk(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return 0, 0, 0, 1

    c = 1 - (r / 255)
    m = 1 - (g / 255)
    y = 1 - (b / 255)
    k = min(c, m, y)

    c = (c - k) / (1 - k) if k < 1 else 0
    m = (m - k) / (1 - k) if k < 1 else 0
    y = (y - k) / (1 - k) if k < 1 else 0

    c_rounded = round(c * 100)
    m_rounded = round(m * 100)
    y_rounded = round(y * 100)
    k_rounded = round(k * 100)

    if c != c_rounded / 100 or m != m_rounded / 100 or y != y_rounded / 100 or k != k_rounded / 100:
        notification_label.config(text="CMYK values have been rounded.")
    else:
        notification_label.config(text="")

    return c_rounded, m_rounded, y_rounded, k_rounded


def cmyk_to_rgb(c, m, y, k):
    c /= 100.0
    m /= 100.0
    y /= 100.0
    k /= 100.0

    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    r_rounded = round(r)
    g_rounded = round(g)
    b_rounded = round(b)

    if r != r_rounded or g != g_rounded or b != b_rounded:
        notification_label.config(text="RGB values have been rounded.")
    else:
        notification_label.config(text="")

    return r_rounded, g_rounded, b_rounded


def update_entries(r, g, b, c, m, y, k, x, yy, z):
    r_entry.delete(0, tk.END)
    r_entry.insert(0, str(r))
    g_entry.delete(0, tk.END)
    g_entry.insert(0, str(g))
    b_entry.delete(0, tk.END)
    b_entry.insert(0, str(b))

    c_entry.delete(0, tk.END)
    c_entry.insert(0, str(c))
    m_entry.delete(0, tk.END)
    m_entry.insert(0, str(m))
    y_entry.delete(0, tk.END)
    y_entry.insert(0, str(y))
    k_entry.delete(0, tk.END)
    k_entry.insert(0, str(k))

    x_entry.delete(0, tk.END)
    x_entry.insert(0, str(x))
    yy_entry.delete(0, tk.END)
    yy_entry.insert(0, str(yy))
    z_entry.delete(0, tk.END)
    z_entry.insert(0, str(z))

    update_color_square(r, g, b)


def update_color_from_rgb():
    r = rgb_r.get()
    g = rgb_g.get()
    b = rgb_b.get()

    c, m, y, k = rgb_to_cmyk(r, g, b)
    x, yy, z = rgb_to_xyz(r, g, b)

    cmyk_c.set(c)
    cmyk_m.set(m)
    cmyk_y.set(y)
    cmyk_k.set(k)

    xyz_x.set(x)
    xyz_y.set(yy)
    xyz_z.set(z)

    update_entries(r, g, b, c, m, y, k, x, yy, z)


def update_color_from_cmyk():
    c = cmyk_c.get()
    m = cmyk_m.get()
    y = cmyk_y.get()
    k = cmyk_k.get()

    r, g, b = cmyk_to_rgb(c, m, y, k)
    rgb_r.set(r)
    rgb_g.set(g)
    rgb_b.set(b)

    x, yy, z = rgb_to_xyz(r, g, b)
    xyz_x.set(x)
    xyz_y.set(yy)
    xyz_z.set(z)

    update_entries(r, g, b, c, m, y, k, x, yy, z)


def update_color_from_xyz():
    x = xyz_x.get()
    yy = xyz_y.get()
    z = xyz_z.get()

    r, g, b = xyz_to_rgb(x, yy, z)
    rgb_r.set(r)
    rgb_g.set(g)
    rgb_b.set(b)

    c, m, y, k = rgb_to_cmyk(r, g, b)
    cmyk_c.set(c)
    cmyk_m.set(m)
    cmyk_y.set(y)
    cmyk_k.set(k)

    update_entries(r, g, b, c, m, y, k, x, yy, z)


def update_entry(var, entry, is_rgb=True):
    entry_value = entry.get().strip()

    if entry_value == "":
        entry.delete(0, tk.END)
        entry.insert(0, "0")
        var.set(0)
        value = 0
    else:
        try:
            value = int(entry_value) if is_rgb else float(entry_value)
            if is_rgb:
                if value < 0 or value > 255:
                    raise ValueError
            else:
                if value < 0 or value > 100:
                    raise ValueError
            var.set(value)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a value within the valid range.")
            return

    if is_rgb:
        update_color_from_rgb()
    elif entry in (c_entry, m_entry, y_entry, k_entry):
        update_color_from_cmyk()
    else:
        update_color_from_xyz()


def open_color_chooser():
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code:
        r, g, b = color_code[0]
        rgb_r.set(int(r))
        rgb_g.set(int(g))
        rgb_b.set(int(b))
        update_color_from_rgb()


def update_color_square(r, g, b):
    color_hex = f'#{r:02x}{g:02x}{b:02x}'
    color_canvas.itemconfig(color_square, fill=color_hex)


# interface
top = tk.Tk()
top.title("Color models")
top.resizable(False, False)
top.attributes("-fullscreen", False)
top.geometry("800x500")
canvas = tk.Canvas(top, width=1000, height=500)
canvas.pack()

color_btn = tk.Button(top, text="Choose Color", command=open_color_chooser)
color_btn.place(x=635, y=30)

color_canvas = tk.Canvas(top, width=150, height=150, bg="white")
color_canvas.place(x=600, y=100)
color_square = color_canvas.create_rectangle(10, 10, 140, 140, fill="#000000")
notification_label = tk.Label(top, text="", fg="blue")
notification_label.place(x=600, y=260)

canvas.create_rectangle(20, 20, 150, 80, fill="lightblue", outline="blue")
canvas.create_text(85, 50, text="RGB", fill="blue")
canvas.create_rectangle(220, 20, 350, 80, fill="lightblue", outline="blue")
canvas.create_text(285, 50, text="CMYK", fill="blue")
canvas.create_rectangle(420, 20, 550, 80, fill="lightblue", outline="blue")
canvas.create_text(485, 50, text="XYZ", fill="blue")

# RGB section
rgb_r = tk.IntVar(value=0)
rgb_g = tk.IntVar(value=0)
rgb_b = tk.IntVar(value=0)

canvas.create_rectangle(20, 120, 150, 180, fill="lightblue", outline="blue")
canvas.create_rectangle(20, 240, 150, 300, fill="lightblue", outline="blue")
canvas.create_rectangle(20, 360, 150, 420, fill="lightblue", outline="blue")
r_value = canvas.create_text(70, 150, text=f"R = ", fill="blue")
g_value = canvas.create_text(70, 270, text=f"G = ", fill="blue")
b_value = canvas.create_text(70, 390, text=f"B = ", fill="blue")

scaleR = tk.Scale(top, from_=0, to=255, orient='horizontal', length=130, variable=rgb_r, command=lambda value: update_color_from_rgb())
scaleR.place(x=18, y=181)
scaleG = tk.Scale(top, from_=0, to=255, orient='horizontal', length=130, variable=rgb_g, command=lambda value: update_color_from_rgb())
scaleG.place(x=18, y=301)
scaleB = tk.Scale(top, from_=0, to=255, orient='horizontal', length=130, variable=rgb_b, command=lambda value: update_color_from_rgb())
scaleB.place(x=18, y=421)

r_entry = tk.Entry(top, width=5)
r_entry.place(x=85, y=142)
g_entry = tk.Entry(top, width=5)
g_entry.place(x=85, y=262)
b_entry = tk.Entry(top, width=5)
b_entry.place(x=85, y=382)

r_entry.insert(0, str(rgb_r.get()))
g_entry.insert(0, str(rgb_g.get()))
b_entry.insert(0, str(rgb_b.get()))

r_entry.bind("<Return>", lambda event: update_entry(rgb_r, r_entry, True))
g_entry.bind("<Return>", lambda event: update_entry(rgb_g, g_entry, True))
b_entry.bind("<Return>", lambda event: update_entry(rgb_b, b_entry, True))
r_entry.bind("<FocusOut>", lambda event: update_entry(rgb_r, r_entry, True))
g_entry.bind("<FocusOut>", lambda event: update_entry(rgb_g, g_entry, True))
b_entry.bind("<FocusOut>", lambda event: update_entry(rgb_b, b_entry, True))

# CMYK section
cmyk_c = tk.IntVar(value=0)
cmyk_m = tk.IntVar(value=0)
cmyk_y = tk.IntVar(value=0)
cmyk_k = tk.IntVar(value=1)

canvas.create_rectangle(220, 120, 350, 150, fill="lightblue", outline="blue")
canvas.create_rectangle(220, 210, 350, 240, fill="lightblue", outline="blue")
canvas.create_rectangle(220, 300, 350, 330, fill="lightblue", outline="blue")
canvas.create_rectangle(220, 390, 350, 420, fill="lightblue", outline="blue")
canvas.create_text(270, 135, text="C = ", fill="blue")
canvas.create_text(270, 225, text="M = ", fill="blue")
canvas.create_text(270, 315, text="Y = ", fill="blue")
canvas.create_text(270, 405, text="K = ", fill="blue")

scaleC = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=cmyk_c, command=lambda value: update_color_from_cmyk())
scaleC.place(x=218, y=151)
scaleM = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=cmyk_m, command=lambda value: update_color_from_cmyk())
scaleM.place(x=218, y=241)
scaleY = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=cmyk_y, command=lambda value: update_color_from_cmyk())
scaleY.place(x=218, y=331)
scaleK = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=cmyk_k, command=lambda value: update_color_from_cmyk())
scaleK.place(x=218, y=421)

c_entry = tk.Entry(top, width=5)
c_entry.place(x=285, y=126)
m_entry = tk.Entry(top, width=5)
m_entry.place(x=285, y=216)
y_entry = tk.Entry(top, width=5)
y_entry.place(x=285, y=306)
k_entry = tk.Entry(top, width=5)
k_entry.place(x=285, y=396)

c_entry.insert(0, str(cmyk_c.get()))
m_entry.insert(0, str(cmyk_m.get()))
y_entry.insert(0, str(cmyk_y.get()))
k_entry.insert(0, str(cmyk_k.get()))

c_entry.bind("<Return>", lambda event: update_entry(cmyk_c, c_entry, False))
m_entry.bind("<Return>", lambda event: update_entry(cmyk_m, m_entry, False))
y_entry.bind("<Return>", lambda event: update_entry(cmyk_y, y_entry, False))
k_entry.bind("<Return>", lambda event: update_entry(cmyk_k, k_entry, False))
c_entry.bind("<FocusOut>", lambda event: update_entry(cmyk_c, c_entry, False))
m_entry.bind("<FocusOut>", lambda event: update_entry(cmyk_m, m_entry, False))
y_entry.bind("<FocusOut>", lambda event: update_entry(cmyk_y, y_entry, False))
k_entry.bind("<FocusOut>", lambda event: update_entry(cmyk_k, k_entry, False))


# XYZ section
xyz_x = tk.IntVar(value=0)
xyz_y = tk.IntVar(value=0)
xyz_z = tk.IntVar(value=0)

canvas.create_rectangle(420, 120, 550, 180, fill="lightblue", outline="blue")
canvas.create_text(470, 150, text="X = ", fill="blue")
canvas.create_rectangle(420, 240, 550, 300, fill="lightblue", outline="blue")
canvas.create_text(470, 270, text="Y = ", fill="blue")
canvas.create_rectangle(420, 360, 550, 420, fill="lightblue", outline="blue")
canvas.create_text(470, 390, text="Z = ", fill="blue")

scaleX = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=xyz_x, command=lambda value: update_color_from_xyz())
scaleX.place(x=418, y=181)
scaleY = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=xyz_y, command=lambda value: update_color_from_xyz())
scaleY.place(x=418, y=301)
scaleZ = tk.Scale(top, from_=0, to=100, orient='horizontal', length=130, variable=xyz_z, command=lambda value: update_color_from_xyz())
scaleZ.place(x=418, y=421)

x_entry = tk.Entry(top, width=5)
x_entry.place(x=485, y=142)
yy_entry = tk.Entry(top, width=5)
yy_entry.place(x=485, y=262)
z_entry = tk.Entry(top, width=5)
z_entry.place(x=485, y=382)

x_entry.insert(0, str(xyz_x.get()))
yy_entry.insert(0, str(xyz_y.get()))
z_entry.insert(0, str(xyz_z.get()))

x_entry.bind("<Return>", lambda event: update_entry(xyz_x, x_entry, False))
yy_entry.bind("<Return>", lambda event: update_entry(xyz_y, yy_entry, False))
z_entry.bind("<Return>", lambda event: update_entry(xyz_z, z_entry, False))
x_entry.bind("<FocusOut>", lambda event: update_entry(xyz_x, x_entry, False))
yy_entry.bind("<FocusOut>", lambda event: update_entry(xyz_y, yy_entry, False))
z_entry.bind("<FocusOut>", lambda event: update_entry(xyz_z, z_entry, False))

top.mainloop()