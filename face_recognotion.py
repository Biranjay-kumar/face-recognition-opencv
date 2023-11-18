from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import END
import cv2
import os
import numpy as np


#============face recognisation=============
class Faace_Recognition:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1500x800+0+25")
		self.root.title("face Recongnisation System")

		#adding title
		title_lbl = Label(self.root, text="Recognitation", font=("times	new roman", 30, "bold"),  bg = "darkblue", fg="white")
		title_lbl.place(x=0, y=0, width=1500, height=48)


		#First Image
		img_left = Image.open(r"college_images\face_detector1.jpg")
		img_left = img_left.resize((748, 750), Image.ANTIALIAS)
		self.photoimg_left = ImageTk.PhotoImage(img_left)

		f_lbl = Label(self.root, image=self.photoimg_left)
		f_lbl.place(x = 2, y = 47, width=748, height=750)

		#second Image
		img_right = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
		img_right = img_right.resize((748, 750), Image.ANTIALIAS)
		self.photoimg_right = ImageTk.PhotoImage(img_right)

		f_lbl = Label(self.root, image=self.photoimg_right)
		f_lbl.place(x = 750, y = 47, width=748, height=750)

		#Buttom
		b1 = Button(f_lbl,text = "Face Recognisation",  cursor="hand2",  command=self.face_recog, font=("times	new roman", 18, "bold"), bg="darkblue", fg="white");
		b1.place(x=250, y=660, width=240, height=40)


	# =============Faace_Recognition=========================
	def face_recog(self):
		def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
			gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

			coord = []

			for (x, y, w, h) in features:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 150, 150), 3)
				# font = cv.FONT_HERSHEY_SIMPLEX
				id, predict = clf.predict(gray_image[y:y+h, x:x+w])
				confidence = int((100*(1-predict/300)))

				conn = mysql.connector.connect(host = "localhost", username = "root", password = "biru@2002", database = "face_recognizer")
				my_cursur = conn.cursor()
				# SELECT * FROM student WHERE Student_id = 1;

				my_cursur.execute("SELECT Name FROM student WHERE Student_id ="+str(id))
				n = my_cursur.fetchone()
				n = "+".join(n)

				my_cursur.execute("SELECT Roll FROM student where Student_id ="+str(id))
				r= my_cursur.fetchone()
				r= "+".join(r)

				my_cursur.execute("SELECT  Phone FROM student where Student_id ="+str(id))
				i = my_cursur.fetchone()
				i = "+".join(i)

				# my_cursur.execute("SELECT Phone FROM student where Student_id ="+str(id))
				# p = my_cursur.fetchone()
				# p = "+".join(p)



				if confidence > 80:
					cv2.putText(img, f"Roll :{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (155, 155, 0), 2)
					cv2.putText(img, f"Name :{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (155, 155, 0), 2)
					cv2.putText(img, f"Phone :{i}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (155, 155, 0), 2)
				
				else:
					cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 30), 3)
					cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (155, 155, 0), 5)

				coord = [x, y, w, h]
			return coord
		

		def recognize(img, clf, faceCascade):
			coord = draw_boundry(img, faceCascade, 1.1, 10, (255, 100, 50), "Face", clf)
			return img

		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		clf = cv2.face.LBPHFaceRecognizer_create()
		clf.read('classifier.xml')

		video_cap = cv2.VideoCapture(0)
		while True:
			ret, img = video_cap.read()
			img = recognize(img, clf, faceCascade)
			cv2.imshow("Welcome To Face Recognisation", img)
			

			if cv2.waitKey(1) ==13:
				break
		video_cap.release()
		cv2.destroyAllWindows()


# gray_image

















if __name__ == "__main__":
	root = Tk()
	obj = Faace_Recognition(root)
	root.mainloop()