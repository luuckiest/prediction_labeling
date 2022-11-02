import tkinter as tk
import glob
from tkinter import Frame,Label
from PIL import ImageTk, Image
import os
import json
import random
class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x600")
        
        self.frame = Frame(self.root, width=600, height=400)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
        self.yaw_pressed = 0
        self.pitch_pressed = 0
        self.direction_prediction = {}
        self.direction_prediction['yaw']=[]
        self.direction_prediction['pitch']=[]
        global pics,photos_label,label_counter
        pic_path = "D:\\Users\\xiaom\\Documents\\2023_IROS_EXPLORATION\\one_tenth_image_with_label (1)\\one_tenth_image"
        pics = glob.glob(pic_path+'\\seg_depth\\*.png')
        random.shuffle(pics)
        # if render output dir not present, make one
        self.labels_out_dir = os.path.join(pic_path, "labels")
        if not os.path.exists(self.labels_out_dir):
            os.makedirs(self.labels_out_dir)
        photos_label = [x for x in pics]
        label_counter=0
        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open(photos_label[label_counter]))

        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame, image = self.img)
        self.label.pack()
        #first 7 bottoms are for yaw, 8-14 is for pitch
        self.button1 = tk.Button(self.root,
                                 text = "1",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor1)
        self.button2 = tk.Button(self.root,
                                 text = "2",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor2)
        self.button3 = tk.Button(self.root,
                                 text = "3",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor3)
        self.button4 = tk.Button(self.root,
                                 text = "4",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor4)
        self.button5 = tk.Button(self.root,
                                 text = "5",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor5)
        self.button6 = tk.Button(self.root,
                                 text = "6",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor6)
        
        self.button7 = tk.Button(self.root,
                                 text = "7",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor7)
        self.button8 = tk.Button(self.root,
                                 text = "7",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor8)
        self.button9 = tk.Button(self.root,
                                 text = "6",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor9)
        self.button10 = tk.Button(self.root,
                                 text = "5",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor10)
        self.button11 = tk.Button(self.root,
                                 text = "4",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor11)
        self.button12 = tk.Button(self.root,
                                 text = "3",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor12)
        self.button13 = tk.Button(self.root,
                                 text = "2",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor13)
        self.button14 = tk.Button(self.root,
                                 text = "1",
                                 bg = "white",
                                 fg = "black",
                                command=self.changeColor14)
        self.button_submit = tk.Button(self.root,
                                 text = "submit",
                                 bg = "white",
                                 fg = "black",
                                activebackground='blue',
                                command=self.change_img)
        self.button_reset = tk.Button(self.root,
                                 text = "reset",
                                 bg = "white",
                                 fg = "black",
                                activebackground='blue',
                                command=self.reset)
        
#         self.button1.grid(column=11, row = 17)
#         self.button2.grid(column=12, row = 17)
#         self.button3.grid(column=13, row = 17)
#         self.button4.grid(column=14, row = 17)
#         self.button5.grid(column=15, row = 17)
#         self.button6.grid(column=16, row = 17)
#         self.button7.grid(column=17, row = 17)
#         self.button_submit.grid(column=14, row = 18)
        self.button1.place(rely=0.9, relx = 0.2)
        self.button2.place(rely=0.9, relx = 0.3)
        self.button3.place(rely=0.9, relx = 0.4)
        self.button4.place(rely=0.9, relx = 0.5)
        self.button5.place(rely=0.9, relx = 0.6)
        self.button6.place(rely=0.9, relx = 0.7)
        self.button7.place(rely=0.9, relx = 0.8)
        self.button_submit.place(rely=0.95, relx = 0.5)
        self.button_reset.place(rely=0.95, relx = 0.6)
        self.button8.place(relx=0.01, rely = 0.2)
        self.button9.place(relx=0.01, rely = 0.3)
        self.button10.place(relx=0.01, rely = 0.4)
        self.button11.place(relx=0.01, rely = 0.5)
        self.button12.place(relx=0.01, rely = 0.6)
        self.button13.place(relx=0.01, rely = 0.7)
        self.button14.place(relx=0.01, rely = 0.8)
        # Define the geometry of the window
        self.root.mainloop()
    def changeColor1(self):
        if self.yaw_pressed == 0:
            self.button1.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[1]
        else:
            pass
    def changeColor2(self):
        if self.yaw_pressed == 0:
            self.button2.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[2]
        else:
            pass
    def changeColor3(self):
        if self.yaw_pressed == 0:
            self.button3.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[3]
        else:
            pass
    def changeColor4(self):
        if self.yaw_pressed == 0:
            self.button4.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[4]
        else:
            pass
    def changeColor5(self):
        if self.yaw_pressed == 0:
            self.button5.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[5]
        else:
            pass
    def changeColor6(self):
        if self.yaw_pressed == 0:
            self.button6.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[6]
        else:
            pass
    def changeColor7(self):
        if self.yaw_pressed == 0:
            self.button7.configure(bg="green")
            self.yaw_pressed =1
            self.direction_prediction['yaw']=[7]
        else:
            pass
    def changeColor8(self):
        if self.pitch_pressed == 0:
            self.button8.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[7]
        else:
            pass
    def changeColor9(self):
        if self.pitch_pressed == 0:
            self.button9.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[6]
        else:
            pass
    def changeColor10(self):
        if self.pitch_pressed == 0:
            self.button10.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[5]
        else:
            pass
    def changeColor11(self):
        if self.pitch_pressed == 0:
            self.button11.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[4]
        else:
            pass
    def changeColor12(self):
        if self.pitch_pressed == 0:
            self.button12.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[3]
        else:
            pass
    def changeColor13(self):
        if self.pitch_pressed == 0:
            self.button13.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[2]
        else:
            pass
    def changeColor14(self):
        if self.pitch_pressed == 0:
            self.button14.configure(bg="green")
            self.pitch_pressed =1
            self.direction_prediction['pitch']=[1]
        else:
            pass
    def change_img(self):
        global pics,photos_label,label_counter
        label_counter+=1
        img=ImageTk.PhotoImage(Image.open(photos_label[label_counter]))
        self.label.configure(image=img)
        self.label.image=img
        #output file
        label_path = os.path.join(self.labels_out_dir,photos_label[label_counter].split('\\')[-1]).split('.')[0]+ ".json"
        with open(label_path, 'w') as fp:
            json.dump(self.direction_prediction, fp)
        #import pdb; pdb.set_trace()
        #reset_colors
        self.button1.configure(bg="white")
        self.button2.configure(bg="white")
        self.button3.configure(bg="white")
        self.button4.configure(bg="white")
        self.button5.configure(bg="white")
        self.button6.configure(bg="white")
        self.button7.configure(bg="white")
        self.button8.configure(bg="white")
        self.button9.configure(bg="white")
        self.button10.configure(bg="white")
        self.button11.configure(bg="white")
        self.button12.configure(bg="white")
        self.button13.configure(bg="white")
        self.button14.configure(bg="white")
        self.yaw_pressed  = 0
        self.pitch_pressed = 0
        self.direction_prediction['yaw']=[]
        self.direction_prediction['pitch']=[]
    def reset(self):
        #reset_colors
        self.button1.configure(bg="white")
        self.button2.configure(bg="white")
        self.button3.configure(bg="white")
        self.button4.configure(bg="white")
        self.button5.configure(bg="white")
        self.button6.configure(bg="white")
        self.button7.configure(bg="white")
        self.button8.configure(bg="white")
        self.button9.configure(bg="white")
        self.button10.configure(bg="white")
        self.button11.configure(bg="white")
        self.button12.configure(bg="white")
        self.button13.configure(bg="white")
        self.button14.configure(bg="white")
        self.yaw_pressed  = 0
        self.pitch_pressed = 0
        self.direction_prediction['yaw']=[]
        self.direction_prediction['pitch']=[]

        
        
if __name__ == '__main__':
    app=Test()  #Call through procedure.
