# prediction_labeling
### Before usage
Just run the python code to start. 
"python prediction_labeling.py"
might need"pip install tkinter"

### General usage
please change the 
pic_path = "D:\\Users\\xiaom\\Documents\\2023_IROS_EXPLORATION\\one_tenth_image_with_label (1)\\one_tenth_image"
to the corresponding path to the folder location that you have saved

On the left hand side, the bottoms are corresponding to: 
7 (pitch top most)
6 (pitch top moderate)
5 (pitch top low)
4 (pitch netural)
5 (pitch down low)
6 (pitch down moderate)
7 (pitch down most)

On the bottom, the bottoms are corresponding to:
1 (row left most)
2 (row left moderate)
3 (row left low)
4 (row netural)
5 (row right low)
6 (row right moderate)
7 (row right most)

These are potential commands that you want to send it to the robot to gather most information. 

The black and white are the representation of depth, the color ones are  the object of your interest.

Your goal is to avoid the balck object that is too close to your but gather most information for the colored area.

Please select one buttom from the "pitch"(on the left hand side column) and one bottom form the "yaw"(on the bottom row), then click submit.

If you happened to make the wrong choice, please select reset.

Please contact xlin01@terpmail.umd.edu if you have question using the labeling tool.

Thanks
