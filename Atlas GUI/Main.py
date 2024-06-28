import tkinter as tk
from tkinter import ttk
# Imported PIL with 'pip install Pillow'
from PIL import Image, ImageTk

#------------------------------------------------------------------ GUI WINDOW
# Creates GUI window
root = tk.Tk()

# Prevents resizing
root.resizable(width= False, height= False)

# Window title
root.title("All About Atlas")

#----------------------------------------------------------------------- IMAGES
# Use pillow to process image (resize requires a tuple)
# Made it a raw str to prevent '\' syntax error
image_logo = Image.open(r'images\dogpaw.png').resize((90,90))
# Displayable image
image_logo_ttk = ImageTk.PhotoImage(image_logo)

image_1 = Image.open(r'images\doggo1.png').resize((550,550))
image_1_ttk = ImageTk.PhotoImage(image_1)

image_2 = Image.open(r'images\doggo2.png').resize((550,550))
image_2_ttk = ImageTk.PhotoImage(image_2)

image_3 = Image.open(r'images\doggo3.png').resize((550,550))
image_3_ttk = ImageTk.PhotoImage(image_3)

image_4 = Image.open(r'images\doggo4.png').resize((550,550))
image_4_ttk = ImageTk.PhotoImage(image_4)

image_5 = Image.open(r'images\doggo5.png').resize((550,550))
image_5_ttk = ImageTk.PhotoImage(image_5)

image_6 = Image.open(r'images\doggo6.png').resize((550,550))
image_6_ttk = ImageTk.PhotoImage(image_6)

image_7 = Image.open(r'images\doggo7.png').resize((550,550))
image_7_ttk = ImageTk.PhotoImage(image_7)

image_8 = Image.open(r'images\doggo8.png').resize((550,550))
image_8_ttk = ImageTk.PhotoImage(image_8)

image_9 = Image.open(r'images\doggo9.png').resize((550,550))
image_9_ttk = ImageTk.PhotoImage(image_9)

image_10 = Image.open(r'images\doggo10.png').resize((550,550))
image_10_ttk = ImageTk.PhotoImage(image_10)

image_11 = Image.open(r'images\doggo11.png').resize((550,550))
image_11_ttk = ImageTk.PhotoImage(image_11)
#------------------------------------------------------------- VISUAL VARIABLES
# Color Pallet
dark_blue = "#48525c"
mid_blue = "#777f8a"
light_blue = "#c4c9cd"
dark_tan = "#9d9a93"
mid_tan = "#cdcbbe"
light_tan = "#e9e8e6"

#Fonts
cursive = "vladimir script"
plain_font1 = "corbel light"
plain_font2 = "bahnschrift semibold"

#---------------------------------------------------------------------- STYLING
#create an object that calls the 'Style' class
s = ttk.Style()

# congigure('name.TWidgettype) T specifices its a ttk widget
s.configure('top_frame.TFrame', background= dark_blue)
s.configure('side_frame.TFrame', background= dark_tan)
s.configure('main_frame.TFrame', background= mid_tan)

s.configure('top_label1.TLabel',
             background = dark_blue,
             foreground = light_tan,
             font = (cursive, 66, "italic"),
             padding = (250, -5, 10, 8)
             )

s.configure('top_label2.TLabel',
             background = dark_blue,
             foreground = light_tan,
             font = (plain_font1, 16, "bold"),
             padding = (300, -5, 0, 5)
             )

s.configure('top_label_logo.TLabel',
            background = dark_blue,
            padding = (10, 5, 0, 0)
            )

s.configure('button.TButton',
            #background only changes?
             background = mid_blue,
             foreground = dark_blue,
             width= 18,
             height = 50,
             font = (plain_font2, 12, "bold"),
             padding = (0, 5, 0, 5),
             )

s.configure('exit_button.TButton',
             background = mid_blue,
             foreground = dark_blue,
             width= 14,
             height = 50,
             font = (plain_font2, 12, "bold"),
             padding = (0, 0, 0, 0),
             )

s.configure('main_label1.TLabel',
            background = dark_tan,
             foreground = dark_blue,
             width= 40,
             height = 1,
             font = (plain_font2, 14, "bold"),
             padding = (5, 5, 5, 5),
             )
#---------------------------------------------------------------------- WIDGETS
top_frame = ttk.Frame(root, width=800, height= 150, style= 'top_frame.TFrame')
#columnspan takes up column 0-1 aka 2 columns 
top_frame.grid(row= 0, column= 0, columnspan= 2, sticky= 'nesw')

side_frame = ttk.Frame(root, width=200, height= 650, style= 'side_frame.TFrame')
side_frame.grid(row= 1, column= 0)

main_frame = ttk.Frame(root, width=600, height= 650, style= 'main_frame.TFrame')
main_frame.grid(row= 1, column= 1)

#------------------------------------------------------------- TOP FRAME LABELS
top_lable1 = ttk.Label(top_frame, text="Welcome", style= 'top_label1.TLabel')
top_lable1.grid(row= 0, column= 0, columnspan= 2)

top_lable2 = ttk.Label(top_frame, text="To All About Atlas",\
            style= 'top_label2.TLabel')
#sticky can attach to NESW directions and can overrule width/height
top_lable2.grid(row= 0, column= 0, columnspan= 2, sticky = 's')

top_lable_logo = ttk.Label(top_frame, image= image_logo_ttk,\
            style= 'top_label_logo.TLabel')
top_lable_logo.grid(row= 0, column= 0, sticky = 'w')

#------------------------------------------------------------ MAIN FRAME LABELS

main_label1 = ttk.Label(main_frame, text="This is the bestest boy in the\
 whole world.", style= 'main_label1.TLabel')

# main_label_config(1)
main_label1.configure(
    image= image_1_ttk,
    compound= 'top'
    )

main_label2 = ttk.Label(main_frame, text="Bombastic side eye... \
criminal offensive side eye...", style= 'main_label1.TLabel')
# main_label_config(2)
main_label2.configure(
    image= image_2_ttk,
    compound= 'top'
    )

main_label3 = ttk.Label(main_frame, text="Atlas craves violence after\
 a fresh bath.", style= 'main_label1.TLabel')
# main_label_config(3)
main_label3.configure(
    image= image_3_ttk,
    compound= 'top'
    )

main_label4 = ttk.Label(main_frame, text="Kachow! Atlas is the fastest\
 doggo west of the Mississippi.", style= 'main_label1.TLabel')
# main_label_config(4)
main_label4.configure(
    image= image_4_ttk,
    compound= 'top'
    )

main_label5 = ttk.Label(main_frame, text="The inner workings of his mind is\
 an enigma.", style= 'main_label1.TLabel')
# main_label_config(5)
main_label5.configure(
    image= image_5_ttk,
    compound= 'top'
    )

main_label6 = ttk.Label(main_frame, text="Welcome to the DANGER ZONE!\
 Atlas lives his life on the edge.", style= 'main_label1.TLabel')
# main_label_config(6)
main_label6.configure(
    image= image_6_ttk,
    compound= 'top'
    )

main_label7 = ttk.Label(main_frame, text="*Sniff* *Sniff*\
 Atlas smells a cutie.", style= 'main_label1.TLabel')
# main_label_config(7)
main_label7.configure(
    image= image_7_ttk,
    compound= 'top'
    )

main_label8 = ttk.Label(main_frame, text="Atlas has had a long day of\
 dueling. Maybe its time for Gwent?", style= 'main_label1.TLabel')
# main_label_config(8)
main_label8.configure(
    image= image_8_ttk,
    compound= 'top'
    )

main_label9 = ttk.Label(main_frame, text="Atlas loves to cuddle with\
 his stuffed animals.", style= 'main_label1.TLabel')
# main_label_config(9)
main_label9.configure(
    image= image_9_ttk,
    compound= 'top'
    )

main_label10 = ttk.Label(main_frame, text="\"Water, earth, colder water,\
 and looking fire. Long ago...\"", style= 'main_label1.TLabel')
# main_label_config(10)
main_label10.configure(
    image= image_10_ttk,
    compound= 'top'
    )

main_label11 = ttk.Label(main_frame, text="The photo speaks for\
 itself.", style= 'main_label1.TLabel')
# main_label_config(11)
main_label11.configure(
    image= image_11_ttk,
    compound= 'top'
    )

#------------------------------------------------------------ SIDE FRAME LABELS
def click(label, clicked_button):
    for l in main_labels:
        l.place_forget()
    label.place(x=20, y=20)

    for button in buttons:
        button.config(state=tk.NORMAL)
    clicked_button.config(state=tk.DISABLED)

def enable_only_current_button(clicked_button):
    return lambda: click(main_labels, clicked_button)

def exit_program():
    root.quit()


button1 = ttk.Button(side_frame, text="The Atlas Doggo",\
            style= 'button.TButton')
button1.place(x= 15 ,y= 15)
button1.configure(command=lambda: click(main_label1, button1))

button2 = ttk.Button(side_frame, text="Side Eye Doggo",\
            style= 'button.TButton')
button2.place(x= 15 ,y= 65)
button2.configure(command=lambda: click(main_label2, button2))

button3 = ttk.Button(side_frame, text="Bath Doggo",\
            style= 'button.TButton')
button3.place(x= 15 ,y= 115)
button3.configure(command=lambda: click(main_label3, button3))

button4 = ttk.Button(side_frame, text="Lightning McDoggo",\
            style= 'button.TButton')
button4.place(x= 15 ,y= 165)
button4.configure(command=lambda: click(main_label4, button4))

button5 = ttk.Button(side_frame, text="Dorky Borky Doggo",\
            style= 'button.TButton')
button5.place(x= 15 ,y= 215)
button5.configure(command=lambda: click(main_label5, button5))

button6 = ttk.Button(side_frame, text="Danger Doggo",\
            style= 'button.TButton')
button6.place(x= 15 ,y= 265)
button6.configure(command=lambda: click(main_label6, button6))

button7 = ttk.Button(side_frame, text="Detective Doggo",\
            style= 'button.TButton')
button7.place(x= 15 ,y= 315)
button7.configure(command=lambda: click(main_label7, button7))

button8 = ttk.Button(side_frame, text="Wizard 101 Doggo",\
            style= 'button.TButton')
button8.place(x= 15 ,y= 365)
button8.configure(command=lambda: click(main_label8, button8))

button9 = ttk.Button(side_frame, text="Nat 1 Athletics Doggo",\
            style= 'button.TButton')
button9.place(x= 15 ,y= 415)
button9.configure(command=lambda: click(main_label9, button9))

button10 = ttk.Button(side_frame, text="Avatar Doggo",\
            style= 'button.TButton')
button10.place(x= 15 ,y= 465)
button10.configure(command=lambda: click(main_label10, button10))

button11 = ttk.Button(side_frame, text="Majestic Doggo",\
            style= 'button.TButton')
button11.place(x= 15 ,y= 515)
button11.configure(command=lambda: click(main_label11, button11))

exit_button = ttk.Button(side_frame, text="EXIT",\
            style= 'exit_button.TButton', command=exit_program)
exit_button.place(x= 32 ,y= 595)

buttons = [
    button1,
    button2,
    button3,
    button4,
    button5,
    button6,
    button7,
    button8,
    button9,
    button10,
    button11,
]
main_labels =[
     main_label1,
     main_label2,
     main_label3,
     main_label4,
     main_label5,
     main_label6,
     main_label7,
     main_label8,
     main_label9,
     main_label10,
     main_label11,
]
root.mainloop()
