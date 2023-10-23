from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk,ImageEnhance,ImageDraw
import os
import cv2
from tkinter import messagebox as tmsg

#exitting
def exitting():
    quit()


img=None
#selecting image
def select_image():
    global new_img
    global img_name
    img_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image",filetype=(("JPG files","jpg"),("PNG files","*.png")))

    global img
    global img_width
    global img_height
    img=Image.open(img_name)
    img_size=img.size
    # print(f"pil width={img_size[0]},height={img_size[1]}")
    img_width=int(img_size[0]/10)
    img_height=int(img_size[1]/10)
    if img_width<100 or img_height<100:
        img_width=img_width*15
        img_height=img_height*15
    elif img_width>100 or img_height>100:
        img_width=img_width*5
        img_height=img_height*5
    img=img.resize((img_width,img_height))
    new_img=img
    show_image(img)
    

#saving images
def saving_image():
    save_img=filedialog.asksaveasfilename(initialdir=os.getcwd(),filetypes=[('Image files','*.jpg'),('Image files','*.png')],defaultextension='Im&ObjbyPraveen.jpg')
    func_save_img(save_img)
    
    

def func_save_img(name_of_img):
    if counter_tk==0:
        cv2.imwrite(name_of_img,cv2_img)
        tmsg.showinfo("Saving Information","You have Successfully Saved Your Image")
    elif counter_tk==1:
        pil_img.save(name_of_img)
        tmsg.showinfo("Saving Information","You have Successfully Saved Your Image")

    
    
#Show image funtion
def show_image(im):

    im=ImageTk.PhotoImage(im)
    img_label.configure(image=im)
    img_label.image=im

#show image function for open cv
def show_cv2_image(im):

    im=cv2.resize(im,(img_width,img_height))
    cv2_img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    img_tk=ImageTk.PhotoImage(Image.fromarray(cv2_img))
    img_label.configure(image=img_tk)
    img_label.image=img_tk

#hovering effect

#btn1
def hover_1(event):
    btn1["bg"]="royalblue"
    btn1["fg"]="white"
    
def remove_hover_1(event):
    btn1["bg"]="white"
    btn1["fg"]="black"
#btn2
def hover_2(event):
    btn2["bg"]="royalblue"
    btn2["fg"]="white"
    
def remove_hover_2(event):
    btn2["bg"]="white"
    btn2["fg"]="black"
#btn3
def hover_3(event):
    btn3["bg"]="royalblue"
    btn3["fg"]="white"
    
def remove_hover_3(event):
    btn3["bg"]="white"
    btn3["fg"]="black"
#btn4
def hover_4(event):
    btn4["bg"]="royalblue"
    btn4["fg"]="white"
    
def remove_hover_4(event):
    btn4["bg"]="white"
    btn4["fg"]="black"

#btn8
def hover_8(event):
    btn8["bg"]="royalblue"
    btn8["fg"]="white"
    
def remove_hover_8(event):
    btn8["bg"]="white"
    btn8["fg"]="black"
#btn9
def hover_9(event):
    btn9["bg"]="royalblue"
    btn9["fg"]="white"
    
def remove_hover_9(event):
    btn9["bg"]="white"
    btn9["fg"]="black"
#btn10
def hover_10(event):
    btn10["bg"]="royalblue"
    btn10["fg"]="white"
    
def remove_hover_10(event):
    btn10["bg"]="white"
    btn10["fg"]="black"

# btn12
def hover_12(event):
    btn12["bg"]="royalblue"
    btn12["fg"]="white"
    
def remove_hover_12(event):
    btn12["bg"]="white"
    btn12["fg"]="black"
# btn13
def hover_13(event):
    btn13["bg"]="royalblue"
    btn13["fg"]="white"
    
def remove_hover_13(event):
    btn13["bg"]="white"
    btn13["fg"]="black"

#btn14
def hover_14(event):
    btn14["bg"]="royalblue"
    btn14["fg"]="white"
    
def remove_hover_14(event):
    btn14["bg"]="white"
    btn14["fg"]="black"

#btn15
def hover_15(event):
    btn15["bg"]="royalblue"
    btn15["fg"]="white"
    
def remove_hover_15(event):
    btn15["bg"]="white"
    btn15["fg"]="black"




#face Detection
def Object_detection(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=0
            global cv2_img
            cv2_img=cv2.imread(f'{img_name}')
            thres = 0.45
            classNames= []
            classFile = 'coco.names'
            with open(classFile,'rt') as f:
                classNames = f.read().rstrip('\n').split('\n')

            configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
            weightsPath = 'frozen_inference_graph.pb'

            net = cv2.dnn_DetectionModel(weightsPath,configPath)
            net.setInputSize(320,320)
            net.setInputScale(1.0/ 127.5)
            net.setInputMean((127.5, 127.5, 127.5))
            net.setInputSwapRB(True)


            classIds, confs, bbox = net.detect(cv2_img,confThreshold=thres)
            print(classIds,bbox)

            if len(classIds) != 0:
                for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                    cv2.rectangle(cv2_img,box,color=(0,255,0),thickness=2)
                    cv2.putText(cv2_img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(cv2_img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            show_cv2_image(cv2_img)
    except:
        pass

#edge_detection
def edge_detection(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=0
            global cv2_img
            cv2_img=cv2.imread(f'{img_name}')
            cv2_img=cv2.Canny(cv2_img,100,100)
            show_cv2_image(cv2_img)
    except:
        pass


#photo_sketching
def photo_sketching(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=0
            global cv2_img
            pencil_img = cv2.imread(f'{img_name}')
            gray_image = cv2.cvtColor(pencil_img,cv2.COLOR_BGR2GRAY)
            inverted_gray_image = (255-gray_image)
            blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)
            inverted_blurred_img = (255-blurred_img)
            cv2_img=cv2.divide(gray_image,inverted_blurred_img,scale=256.0)
            show_cv2_image(cv2_img)
    except:
        pass


#make_cartoon
def make_cartoon(event):
    try:
            if img==None:
                tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
            else:
                global counter_tk
                counter_tk=0
                global cv2_img
                make_cartoon_img=cv2.imread(f'{img_name}')
                grey_img=cv2.cvtColor(make_cartoon_img,cv2.COLOR_BGR2GRAY)
                grey_img=cv2.medianBlur(grey_img,5)
                edges_img=cv2.adaptiveThreshold(grey_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,9)
                color=cv2.bilateralFilter(make_cartoon_img,9,250,250)
                cv2_img=cv2.bitwise_and(color,color,mask=edges_img)
                show_cv2_image(cv2_img)
    except:
        pass

#adjust_brightness
def adjust_brightness(event):
    try:
        if img == None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            tmsg.showinfo("Information","Please select the appropriate value for your image and tha initial value is 5")
            new_tk_root=Tk()
            new_tk_root.geometry("455x130")
            new_tk_root.title("Adjust Enhance")
            def adjusting_brightness(event):
                global counter_tk
                counter_tk=1
                global pil_img
                value_factor=int(slider1.get())
                value_factor=value_factor/5
                enhan_img=ImageEnhance.Brightness(img)
                pil_img=enhan_img.enhance(value_factor)
                show_image(pil_img)

            
            def adjust_color(event):
                global counter_tk
                counter_tk=1
                global pil_img
                value_factor=int(slider2.get())
                value_factor=value_factor/5
                enhan_img=ImageEnhance.Color(img)
                pil_img=enhan_img.enhance(value_factor)
                show_image(pil_img)

            def adjust_sharpness(event):
                global counter_tk
                counter_tk=1
                global pil_img
                value_factor=int(slider3.get())
                value_factor=value_factor/5
                enhan_img=ImageEnhance.Sharpness(img)
                pil_img=enhan_img.enhance(value_factor)
                show_image(pil_img)


            def adjust_contrast(event):
                global counter_tk
                counter_tk=1
                global pil_img
                value_factor=int(slider4.get())
                value_factor=value_factor/5
                enhan_img=ImageEnhance.Contrast(img)
                pil_img=enhan_img.enhance(value_factor)
                show_image(pil_img)



            text_label_slider1=Label(new_tk_root,text="Brightness")
            text_label_slider1.grid(row=0,column=0)
            slider1=Scale(new_tk_root,from_=1,to=50,bg="Royal blue",fg="white",borderwidth=5,relief=GROOVE,orient=HORIZONTAL,tickinterval=24)
            slider1.set(5)
            slider1.grid(row=1,column=0)
            slider_btn2=Button(new_tk_root,text="adjust now",relief=SUNKEN,borderwidth=2,font="lucida 10 bold",bg="white",fg="royal blue")
            slider_btn2.grid(row=2,column=0)
            slider_btn2.bind('<Button-1>',adjusting_brightness)

            text_labe2_slider1=Label(new_tk_root,text="Color")
            text_labe2_slider1.grid(row=0,column=1)
            slider2=Scale(new_tk_root,from_=1,to=50,bg="Royal blue",fg="white",borderwidth=5,relief=GROOVE,orient=HORIZONTAL,tickinterval=24)
            slider2.set(5)
            slider2.grid(row=1,column=1)
            slider_btn1=Button(new_tk_root,text="adjust now",relief=SUNKEN,borderwidth=2,font="lucida 10 bold",bg="white",fg="royal blue")
            slider_btn1.grid(row=2,column=1)
            slider_btn1.bind('<Button-1>',adjust_color)

            text_label_slider3=Label(new_tk_root,text="Sharpness")
            text_label_slider3.grid(row=0,column=2)
            slider3=Scale(new_tk_root,from_=1,to=50,bg="Royal blue",fg="white",borderwidth=5,relief=GROOVE,orient=HORIZONTAL,tickinterval=24)
            slider3.set(5)
            slider3.grid(row=1,column=2)
            slider_btn3=Button(new_tk_root,text="adjust now",relief=SUNKEN,borderwidth=2,font="lucida 10 bold",bg="white",fg="royal blue")
            slider_btn3.grid(row=2,column=2)
            slider_btn3.bind('<Button-1>',adjust_sharpness)

            text_label_slider4=Label(new_tk_root,text="Contrast")
            text_label_slider4.grid(row=0,column=3)
            slider4=Scale(new_tk_root,from_=1,to=50,bg="Royal blue",fg="white",borderwidth=5,relief=GROOVE,orient=HORIZONTAL,tickinterval=24)
            slider4.set(5)
            slider4.grid(row=1,column=3)
            slider_btn4=Button(new_tk_root,text="adjust now",relief=SUNKEN,borderwidth=2,font="lucida 10 bold",bg="white",fg="royal blue")
            slider_btn4.grid(row=2,column=3)
            slider_btn4.bind('<Button-1>',adjust_contrast)
            new_tk_root.mainloop()
    except:
        pass

#cropping

def crop_starting(event):
    global x_start
    global y_start
    x_start=event.x
    y_start=event.y
    

def crop_ending(event):
    global crop_img
    
    global x_end
    global y_end
    x_end=event.x
    y_end=event.y


def cropping(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            tmsg.showinfo("Information","select the portion which you want to crop and then press on crop")
            global counter_tk
            counter_tk=1
            global pil_img
            pil_img=img.crop((x_start,y_start,x_end,y_end))
            show_image(pil_img)
    except:
        pass


#transformming
def mirror(event):
    try:        
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=1
            global pil_img
            pil_img=img.transpose(Image.FLIP_LEFT_RIGHT)
            show_image(pil_img)
    except:
        pass

#flipping
def flipping(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=1
            global pil_img
            pil_img=img.rotate(angle=180.0)
            show_image(pil_img)
    except:
        pass

#rotating

def start_rotate(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            new_tk_root=Tk()
            def rotating(event):
                global pil_img
                global counter_tk
                counter_tk=1
                rotate_angle=float(slider.get())
                pil_img=img.rotate(angle=rotate_angle)
                show_image(pil_img)
            

            
            slider=Scale(new_tk_root,from_=0,to=360,bg="Royal blue",fg="white",borderwidth=5,relief=GROOVE,orient=HORIZONTAL,tickinterval=180)
            slider.pack()
            btn=Button(new_tk_root,text="rotate")
            btn.pack()
            btn.bind('<Button-1>',rotating)
    except:
        pass


#bluring
def bluring(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=0
            global cv2_img
            cv2_img=cv2.imread(f'{img_name}')
            cv2_img=cv2.GaussianBlur(cv2_img,(7,7),0)
            show_cv2_image(cv2_img)
    except:
        pass
    

#grey_scale
def grey_scale(event):
    try:
        if img==None:
            tmsg.showerror("Image not found","Please select the image first and then proceed ahead")
        else:
            global counter_tk
            counter_tk=0
            global cv2_img
            cv2_img=cv2.imread(f'{img_name}')
            cv2_img=cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY)
            show_cv2_image(cv2_img)
    except:
        pass
    


#main method

root=Tk()
tk_width=950
tk_height=850

root.geometry(f"{tk_width}x{tk_height}")
root.minsize(tk_width,tk_height)
root.maxsize(tk_width,tk_height)


root.title("Image Ediitor and Objet Finder")

#file menu

file_menu=Menu(root)
root.config(menu=file_menu)

# file_menu
sub_file_menu=Menu(file_menu,tearoff=0)
sub_file_menu.add_command(label="Select New Image",command=select_image)
sub_file_menu.add_command(label="Save Changes",command=saving_image)
file_menu.add_cascade(label="FILE",menu=sub_file_menu)

#exit menu

sub_exit_menu=Menu(file_menu,tearoff=0)
sub_exit_menu.add_command(label="Exit",command=exitting)
file_menu.add_cascade(label="EXIT",menu=sub_exit_menu)


#making frames

frame1 =Frame(root,bg="royalblue",borderwidth=5,relief=SUNKEN)
frame1.pack(side=BOTTOM,pady=5,fill=X)
name=Label(frame1,text="Image Editor & Object Finder by PRAVEEN..",borderwidth=5,bg="white",font=f"lucida 15 bold")
name.pack(fill=X)

frame2 = Frame(root,bg="royalblue",borderwidth=5,relief=SUNKEN,height=850,width=200)
frame2.pack(side=LEFT,padx=9)

frame3 = Frame(root,bg="royalblue",borderwidth=5,relief=SUNKEN,height=850,width=745)
frame3.pack(side=RIGHT)

frame4 = Frame(frame3,borderwidth=5,relief=GROOVE,height=840,width=730,pady=2,padx=2)
frame4.pack()

#label for images
img_label=Label(frame4)
img_label.pack()
img_label.bind('<ButtonPress-1>',crop_starting)
img_label.bind('<ButtonRelease-1>',crop_ending)

#making buttons
btn1=Button(frame2,text="Object Detection",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn1.pack(anchor=NE,padx=5,pady=3)
btn1.bind('<Enter>',hover_1)
btn1.bind('<Leave>',remove_hover_1)
btn1.bind('<Button-1>',Object_detection)


#this is the starting of new button
btn2=Button(frame2,text="Edge Detection",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn2.pack(anchor=NE,padx=5,pady=3)
btn2.bind('<Enter>',hover_2)
btn2.bind('<Leave>',remove_hover_2)
btn2.bind('<Button-1>',edge_detection)


#this is the starting of new button
btn3=Button(frame2,text="Photo Sketching",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn3.pack(anchor=NE,padx=5,pady=3)
btn3.bind('<Enter>',hover_3)
btn3.bind('<Leave>',remove_hover_3)
btn3.bind('<Button-1>',photo_sketching)


#this is the starting of new button
btn4=Button(frame2,text="Make Cartoon",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn4.pack(anchor=NE,padx=5,pady=3)
btn4.bind('<Enter>',hover_4)
btn4.bind('<Leave>',remove_hover_4)
btn4.bind('<Button-1>',make_cartoon)


#this is the starting of new button

btn8=Button(frame2,text="Adjust Brightness",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn8.pack(anchor=NE,padx=5,pady=3)
btn8.bind('<Enter>',hover_8)
btn8.bind('<Leave>',remove_hover_8)
btn8.bind('<Button-1>',adjust_brightness)




#this is the starting of new button
btn9=Button(frame2,text="Cropping",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn9.pack(anchor=NE,padx=5,pady=3)
btn9.bind('<Enter>',hover_9)
btn9.bind('<Leave>',remove_hover_9)
btn9.bind('<Button-1>',cropping)



#this is the starting of new button
btn10=Button(frame2,text="Mirror",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn10.pack(anchor=NE,padx=5,pady=3)
btn10.bind('<Enter>',hover_10)
btn10.bind('<Leave>',remove_hover_10)
btn10.bind('<Button-1>',mirror)


#this is the starting of new button
btn12=Button(frame2,text="Flip",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn12.pack(anchor=NE,padx=5,pady=3)
btn12.bind('<Enter>',hover_12)
btn12.bind('<Leave>',remove_hover_12)
btn12.bind('<Button-1>',flipping)


#this is the starting of new button
btn13=Button(frame2,text="Rotate",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn13.pack(anchor=NE,padx=5,pady=3)
btn13.bind('<Enter>',hover_13)
btn13.bind('<Leave>',remove_hover_13)
btn13.bind('<Button-1>',start_rotate)
# btn3.bind('<Button-2>',end_rotate)


#this is the starting of new button
btn14=Button(frame2,text="Blur",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn14.pack(anchor=NE,padx=5,pady=3)
btn14.bind('<Enter>',hover_14)
btn14.bind('<Leave>',remove_hover_14)
btn14.bind('<Button-1>',bluring)


#this is the starting of new button
btn15=Button(frame2,text="GreyScale",borderwidth=2,relief=SUNKEN,bg="white",width=25,height=2)
btn15.pack(anchor=NE,padx=5,pady=3)
btn15.bind('<Enter>',hover_15)
btn15.bind('<Leave>',remove_hover_15)
btn15.bind('<Button-1>',grey_scale)

root.mainloop()