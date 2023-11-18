from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Students
from train import Train
from face_recognotion import Faace_Recognition



class Face_recog_system:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1500x1400+0+25")
		self.root.title("face Recongnisation System")

		img = Image.open(r"college_images\BestFacialRecognition.jpg")
		img = img.resize((500, 130), Image.ANTIALIAS)
		self.photoimg = ImageTk.PhotoImage(img)

		f_lbl = Label(self.root, image=self.photoimg)
		f_lbl.place(x = 0, y = 0, width=500, height=130)

# new image1
		img1 = Image.open(r"college_images\facialrecognition.png")
		img1 = img1.resize((500, 130), Image.ANTIALIAS)
		self.photoimg1 = ImageTk.PhotoImage(img1)

		f_lbl = Label(self.root, image=self.photoimg1)
		f_lbl.place(x = 500, y = 0, width=500, height=130)

# new image2
		img2 = Image.open(r"college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
		img2 = img2.resize((500, 130), Image.ANTIALIAS)
		self.photoimg2 = ImageTk.PhotoImage(img2)

		f_lbl = Label(self.root, image=self.photoimg2)
		f_lbl.place(x = 1000, y = 0, width=500, height=130)


#background image
		img3 = Image.open(r"college_images\bg_img.jpg")
		img3 = img3.resize((1500, 570), Image.ANTIALIAS)
		self.photoimg3 = ImageTk.PhotoImage(img3)

		bg_img = Label(self.root, image=self.photoimg3)
		bg_img.place(x = 0, y = 130, width=1500, height=570)
        
		#adding title
		title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("times	new roman", 30, "bold"),  bg = "white", fg="red")
		title_lbl.place(x=0, y=0, width=1500, height=34)

#student button
		img4 = Image.open(r"college_images\student.jpg")
		img4 = img4.resize((220, 220), Image.ANTIALIAS)
		self.photoimg4 = ImageTk.PhotoImage(img4)

		b1 = Button(bg_img, image=self.photoimg4, command=self.student_details,  cursor="hand2")
		b1.place(x=200, y=100, width=220, height=170)

		b1_1 = Button(bg_img, text="Students Details", command=self.student_details,  cursor="hand2",  fg="white", bg="purple")
		b1_1.place(x=200, y=270, width=221, height=40)

#detect face button
		img5 = Image.open(r"college_images\face_detector1.jpg")
		img5 = img5.resize((220, 220), Image.ANTIALIAS)
		self.photoimg5 = ImageTk.PhotoImage(img5)

		b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
		b1.place(x=530, y=100, width=220, height=170)

		b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,  fg="white", bg="purple")
		b1_1.place(x=530, y=270, width=221, height=40)

#Attendence Button
		img6 = Image.open(r"college_images\smart-attendance.jpg")
		img6 = img6.resize((220, 220), Image.ANTIALIAS)
		self.photoimg6 = ImageTk.PhotoImage(img6)

		b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
		b1.place(x=920, y=100, width=220, height=170)

		b1_1 = Button(bg_img, text="Attendence Button", cursor="hand2",  fg="white", bg="purple")
		b1_1.place(x=920, y=270, width=221, height=40)

#help desk
		img7 = Image.open(r"college_images\help_desk.jpg")
		img7 = img7.resize((220, 220), Image.ANTIALIAS)
		self.photoimg7 = ImageTk.PhotoImage(img7)

		b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
		b1.place(x=1220, y=100, width=220, height=170)

		b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",  fg="white", bg="purple")
		b1_1.place(x=1220, y=270, width=221, height=40)

#train button
		img8 = Image.open(r"college_images\Train.jpg")
		img8 = img8.resize((220, 120), Image.ANTIALIAS)
		self.photoimg8 = ImageTk.PhotoImage(img8)

		b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
		b1.place(x=200, y=330, width=220, height=220)

		b1_1 = Button(bg_img, text="Train Button", cursor="hand2", command=self.train_data,  fg="white", bg="purple")
		b1_1.place(x=200, y=520, width=221, height=35)

#photo face button
		img9 = Image.open(r"college_images\face-recognition.png")
		img9 = img9.resize((220, 220), Image.ANTIALIAS)
		self.photoimg9 = ImageTk.PhotoImage(img9)

		b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
		b1.place(x=530, y=330, width=220, height=220)

		b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,  fg="white", bg="purple")
		b1_1.place(x=530, y=520, width=221, height=35)

#Developer
		img10 = Image.open(r"college_images\developer.jpg")
		img10 = img10.resize((220, 220), Image.ANTIALIAS)
		self.photoimg10 = ImageTk.PhotoImage(img10)

		b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
		b1.place(x=920, y=330, width=220, height=220)

		b1_1 = Button(bg_img, text="Developer", cursor="hand2",  fg="white", bg="purple")
		b1_1.place(x=920, y=520, width=221, height=35)

#Exit
		img11 = Image.open(r"college_images\exit.jpg")
		img11 = img11.resize((220, 220), Image.ANTIALIAS)
		self.photoimg11 = ImageTk.PhotoImage(img11)

		b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
		b1.place(x=1220, y=330, width=220, height=220)

		b1_1 = Button(bg_img, text="Exit", cursor="hand2",  fg="white", bg="purple")
		b1_1.place(x=1220, y=520, width=221, height=35)

	def open_img(self):
		os.startfile("data")













#   ===========Function Buttons=============
	#student
	def student_details(self):
		self.new_window = Toplevel(self.root)
		self.app = Students(self.new_window)

	#train
	def train_data(self):
		self.new_window = Toplevel(self.root)
		self.app = Train(self.new_window)

		#face recognitaion
	def face_data(self):
		self.new_window = Toplevel(self.root)
		self.app = Faace_Recognition(self.new_window)






















if __name__ == "__main__":
	root = Tk()
	obj = Face_recog_system(root)
	root.mainloop()
        
        # Create a container to hold everything inside the window.
		