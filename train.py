from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import END
import cv2
import os
import numpy as np
# from PIL import Image
# Import-Module PSReadLine
class Train:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1500x800+0+25")
		self.root.title("face Recongnisation System")


		#adding title
		title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times	new roman", 30, "bold"),  bg = "white", fg="red")
		title_lbl.place(x=0, y=0, width=1500, height=34)

		# Top images
		img_top = Image.open(r"college_images\2-AI-invades-automobile-industry-in-2019.jpeg")
		img_top = img_top.resize((1500, 390), Image.ANTIALIAS)
		self.photoimg_top = ImageTk.PhotoImage(img_top)

		f_lbl = Label(self.root, image=self.photoimg_top)
		f_lbl.place(x = 2, y = 38, width=1495, height=357)

		#Train button
		b1 = Button(self.root,text = "Train Data", command=self.train_classifier,  cursor="hand2", font=("times	new roman", 26, "bold"), bg="darkblue", fg="white");
		b1.place(x=2, y=395, width=1495, height=50)

		#Buttom Images
		img_buttom = Image.open(r"college_images\facialrecognition.png")
		img_buttom = img_buttom.resize((1500, 380), Image.ANTIALIAS)
		self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)

		f_lbl = Label(self.root, image=self.photoimg_buttom)
		f_lbl.place(x = 2, y = 445, width=1495, height=350)
	

	def train_classifier(self):
		data_dir = ("data")
		path = [os.path.join (data_dir, file)for file in os.listdir(data_dir)]

		faces = []
		ids = []

		for image in path:
			img = Image.open(image).convert('L')	#Gray scale image
			imageNp = np.array(img, 'uint8')
			id = int(os.path.split(image)[1].split('.')[1])

			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Training", imageNp)
			cv2.waitKey(1) == 13
		
		ids = np.array(ids)

		# ============ Train  the classifier and save it=============
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces, ids)
		clf.write("classifier.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("result", "Training Completed!!!")

		















if __name__ == "__main__":
	root = Tk()
	obj = Train(root)
	root.mainloop()