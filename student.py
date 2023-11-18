from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import END
import cv2
# from PIL import Image
# Import-Module PSReadLine
class Students:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1500x800+0+25")
		self.root.title("face Recongnisation System")
		# ============= Variables ===============
		self.var_dep = StringVar()
		self.var_course = StringVar()
		self.var_year = StringVar()
		self.var_semester = StringVar()
		self.var_std_id = StringVar()
		self.var_std_name = StringVar()
		self.var_div = StringVar()
		self.var_roll = StringVar()
		self.var_gender = StringVar()
		self.var_dob = StringVar()
		self.var_address = StringVar()
		self.var_phone = StringVar()
		self.var_email = StringVar()
		self.var_blood_group = StringVar()

		img = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\Team-Management-Software-Development.jpg")
		img = img.resize((500, 130), Image.ANTIALIAS)
		self.photoimg = ImageTk.PhotoImage(img)

		f_lbl = Label(self.root, image=self.photoimg)
		f_lbl.place(x = 0, y = 0, width=500, height=130)

# new image1
		img1 = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\student-portal_1.jpg")
		img1 = img1.resize((500, 130), Image.ANTIALIAS)
		self.photoimg1 = ImageTk.PhotoImage(img1)

		f_lbl = Label(self.root, image=self.photoimg1)
		f_lbl.place(x = 500, y = 0, width=500, height=130)

# new image2
		img2 = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\opencv_face_reco_more_data.jpg")
		img2 = img2.resize((500, 130), Image.ANTIALIAS)
		self.photoimg2 = ImageTk.PhotoImage(img2)

		f_lbl = Label(self.root, image=self.photoimg2)
		f_lbl.place(x = 1000, y = 0, width=500, height=130)

#bg image
		img3 = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\bg_img.jpg")
		img3 = img3.resize((1500, 570), Image.ANTIALIAS)
		self.photoimg3 = ImageTk.PhotoImage(img3)

		bg_img = Label(self.root, image=self.photoimg3)
		bg_img.place(x = 0, y = 130, width=1500, height=650)
        
		#adding title
		title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times	new roman", 30, "bold"),  bg = "white", fg="red")
		title_lbl.place(x=0, y=0, width=1500, height=34)

#MAKING FRAME
		main_frame = Frame(bg_img, bd = 2, bg="white")
		main_frame.place(x = 19, y=45, width=1450, height=750)

#Left label frame
		left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman",  12, "bold"))
		left_frame.place(x=20, y=10, width=680, height=580)

		#image in left frame
		img_left = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\har.jpg")
		img_left = img_left.resize((670, 130), Image.ANTIALIAS)
		self.photoimg_left = ImageTk.PhotoImage(img_left)

		f_lbl = Label(left_frame, image=self.photoimg_left)
		f_lbl.place(x = 5, y = 8, width=670, height=130)

		#current course
		current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,text="current course information Details", font=("times new roman",  12, "bold"))
		current_course_frame.place(x=5, y=135, width=668, height=100)

		#depatment
		dep_label = Label(current_course_frame, text="Department", font=("times new roman",  12, "bold"), bg="white")
		dep_label.grid(row=0, column=0, padx=10, sticky=W)

		dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman",  12, "bold"), width=15 , state="readonly")
		dep_combo['values'] = ("select Department", "Computer Science and Engineering","Electronics and Communication Engineering","Mechanical Engineering")
		dep_combo.current(0)
		dep_combo.grid(row=0, column=1,padx = 2,pady=2, sticky=W)
		
		#course
		course_label = Label(current_course_frame, text="Course", font=("times new roman",  12, "bold"), bg="white")
		course_label.grid(row=0, column=2, padx=10, sticky=W)

		course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman",  12, "bold"), width=15 , state="readonly")
		course_combo['values'] = ("Select Course", "B.Tech", "M.Tech", "P.H.D", "Bca", "Mca")
		course_combo.current(0)
		course_combo.grid(row=0, column=3,padx = 2,pady=2, sticky=W )
		
		#year
		year_label = Label(current_course_frame, text="Year", font=("times new roman",  12, "bold"), bg="white")
		year_label.grid(row=1, column=0, padx=10, sticky=W)

		year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman",  12, "bold"), width=15 , state="readonly")
		year_combo['values'] = ("Select Year",  "2020-24","2021-25", "2022-26", "2024-28", "2025-29", "2026-30")
		year_combo.current(0)
		year_combo.grid(row=1, column=1,padx = 2,pady=2, sticky=W )
		
		#semestem
		semestem_label = Label(current_course_frame, text="Semester", font=("times new roman",  12, "bold"), bg="white")
		semestem_label.grid(row=1, column=2, padx=10, sticky=W)

		semestem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman",  12, "bold"), width=15 , state="readonly")
		semestem_combo['values'] = ("Select Sem", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
		semestem_combo.current(0)
		semestem_combo.grid(row=1, column=3,padx = 2,pady=2, sticky=W )
		
#Class student information
		class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,text="Class student information", font=("times new roman",  12, "bold"))
		class_student_frame.place(x=5, y=245, width=668, height=310)

#studentId level
		#student Id
		studentId_label = Label(class_student_frame, text="StudentId ", font=("times new roman",  12, "bold"), bg="white")
		studentId_label.grid(row=0, column=0, padx=10, sticky=W)

		studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman",  12, "bold"))
		studentId_entry.grid(row=0, column=1, padx = 2,pady=2, sticky=W)
		
		#student Name
		studentName_label = Label(class_student_frame, text="Student's Name ", font=("times new roman",  12, "bold"), bg="white")
		studentName_label.grid(row=0, column=2, padx=10, sticky=W)

		studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman",  12, "bold"))
		studentName_entry.grid(row=0, column=3, padx = 2,pady=2, sticky=W)
		
		#class division
		class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman",  12, "bold"), bg="white")
		class_div_label.grid(row=1, column=0, padx=10, sticky=W)

		# class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman",  12, "bold"))
		# class_div_entry.grid(row=1, column=1, padx = 2,pady=2, sticky=W)
		class_div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman",  12, "bold"), width=18 , state="readonly")
		class_div_combo['values'] = ("A", "B", "C", "D", "E", "F")
		class_div_combo.current(0)
		class_div_combo.grid(row=1, column=1,padx = 2,pady=2, sticky=W )

		#Roll No. 
		roll_no_label = Label(class_student_frame, text="Roll No.", font=("times new roman",  12, "bold"), bg="white")
		roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

		roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman",  12, "bold"))
		roll_no_entry.grid(row=1, column=3, padx = 2,pady=2, sticky=W)

		#Gender
		gender_label = Label(class_student_frame, text="Gneder", font=("times new roman",  12, "bold"), bg="white")
		gender_label.grid(row=2, column=0, padx=10, sticky=W)

		# gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=("times new roman",  12, "bold"))
		# gender_entry.grid(row=2, column=1, padx = 2,pady=2, sticky=W)
		gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman",  12, "bold"), width=18 , state="readonly")
		gender_combo['values'] = ("Gender", "He", "She", "It", "This", "That", "Other")
		gender_combo.current(0)
		gender_combo.grid(row=2, column=1,padx = 2,pady=2, sticky=W )

		#D.O.B
		dob_label = Label(class_student_frame, text="Date of Birth", font=("times new roman",  12, "bold"), bg="white")
		dob_label.grid(row=2, column=2, padx=10, sticky=W)

		dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman",  12, "bold"))
		dob_entry.grid(row=2, column=3, padx = 2,pady=2, sticky=W)

		#Contact number
		phone_number_label = Label(class_student_frame, text="Contact number", font=("times new roman",  12, "bold"), bg="white")
		phone_number_label.grid(row=3, column=0, padx=10, sticky=W)

		phone_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman",  12, "bold"))
		phone_number_entry.grid(row=3, column=1, padx = 2,pady=2, sticky=W)

		#email 
		email_label = Label(class_student_frame, text="Email", font=("times new roman",  12, "bold"), bg="white")
		email_label.grid(row=3, column=2, padx=10, sticky=W)

		email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman",  12, "bold"))
		email_entry.grid(row=3, column=3, padx = 2,pady=2, sticky=W)

		#Address
		class_div_label = Label(class_student_frame, text="Address", font=("times new roman",  12, "bold"), bg="white")
		class_div_label.grid(row=4, column=0, padx=10, sticky=W)

		class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman",  12, "bold"))
		class_div_entry.grid(row=4, column=1, padx = 2,pady=2, sticky=W)
		
		#Blood Group
		blood_grouplabel = Label(class_student_frame, text="Blood Group", font=("times new roman",  12, "bold"), bg="white")
		blood_grouplabel.grid(row=4, column=2, padx=10, sticky=W)

		
		blood_groupentry = ttk.Entry(class_student_frame, textvariable=self.var_blood_group, width=20, font=("times new roman",  12, "bold"))
		blood_groupentry.grid(row=4, column=3, padx = 2,pady=2, sticky=W)

# radio Buttons
		self.var_radio1 = StringVar()
		Radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take a Photo Sample", value="Yes")
		Radiobtn1.grid(row=6, column=0)

		Radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
		Radiobtn2.grid(row=6, column=1)

#button frame
		btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
		btn_frame.place(x=2, y=190, height=40, width=660)

		#save button
		save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman",  12, "bold"), fg="white", bg="darkgreen" , width=17)
		save_btn.grid(column=0, row=0)

		#update
		Update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman",  12, "bold"), fg="white", bg="darkblue" , width=17)
		Update_btn.grid(column=1, row=0)

		#delete
		delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman",  12, "bold"), fg="white", bg="red" , width=17)
		delete_btn.grid(column=2, row=0)

		#reset
		reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman",  12, "bold"), fg="white", bg="blue" , width=17)
		reset_btn.grid(column=3, row=0)

#button frame
		btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
		btn_frame1.place(x=2, y=234, height=40, width=660)
		#take photo sample
		take_photo_sample_btn = Button(btn_frame1, text="Take photo sample", command=self.generate_dataset, font=("times new roman",  12, "bold"), fg="white", bg="darkblue" , width=36)
		take_photo_sample_btn.grid(column=0, row=0)

		#update photo sample
		update_photo_sample_btn = Button(btn_frame1, text="Update photo sample", font=("times new roman",  12, "bold"), fg="white", bg="darkblue" , width=35)
		update_photo_sample_btn.grid(column=1, row=0)


#Right label frame
		right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman",  12, "bold"))
		right_frame.place(x=705, y=10, width=685, height=580)

		#image in right frame
		img_right = Image.open(r"C:\Users\Biranjay\OneDrive\Desktop\face_recog_system\college_images\smart-attendance.jpg")
		# img_right = img_right.resize((670, 130), Image.ANTIALIAS)
		img_right = img_right.resize((670, 130), Image.ANTIALIAS)
		# img_right = img_right.resize((670, 130), Image.LANCZOS)
		self.photoimg_right = ImageTk.PhotoImage(img_right)

		f_lbl = Label(right_frame, image=self.photoimg_right)
		f_lbl.place(x = 5, y = 8, width=670, height=130)

#		========== Searching System ========
		Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,text="Search System", font=("times new roman",  12, "bold"))
		Search_frame.place(x=5, y=135, width=668, height=70)

		#level for search
		search_label = Label(Search_frame, text="search By", font=("times new roman",  12, "bold"), bg="red", fg="white")
		search_label.grid(row=0, column=0, padx=10, sticky=W)

		#combo box
		search_combo = ttk.Combobox(Search_frame,font=("times new roman",  12, "bold"), width=15 , state="readonly")
		search_combo['values'] = ("Select", "Roll_no", "Phone_no")
		search_combo.current(0)
		search_combo.grid(row=0, column=1,padx = 2,pady=2, sticky=W )

#button
		#entry fill
		studentName_entry = ttk.Entry(Search_frame, width=17, font=("times new roman",  12, "bold"))
		studentName_entry.grid(row=0, column=2, padx = 2,pady=2, sticky=W)
		
		#update
		Search_btn = Button(Search_frame, text="Search", font=("times new roman",  12, "bold"), fg="white", bg="darkblue" , width=13)
		Search_btn.grid(column=3, row=0, padx=2)

		#delete
		ShowAll_btn = Button(Search_frame, text="ShowAll", font=("times new roman",  12, "bold"), fg="white", bg="red" , width=13)
		ShowAll_btn.grid(column=4, row=0, padx=2)



#		========== Table Frame ========
		Table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
		Table_frame.place(x=5, y=207, width=668, height=350)

		#screll bar
		scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
		scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

		self.student_table = ttk.Treeview(Table_frame, columns=("department", "Course", "year", "Sem", "ID", "Name", "Div", "roll", "Gender", "DOB", "Email", "Phone", "Address", "Blood Group", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.configure(command=self.student_table.xview)
		scroll_y.configure(command=self.student_table.yview)

		#write heading
		self.student_table.heading("department", text = "Department")
		self.student_table.heading("Course", text = "Course")
		self.student_table.heading("year", text = "Year")
		self.student_table.heading("Sem", text = "Sem")
		self.student_table.heading("ID", text = "ID")
		self.student_table.heading("Name", text = "Name")
		self.student_table.heading("Div", text = "Div")
		self.student_table.heading("roll", text = "Roll")
		self.student_table.heading("Gender", text = "Gender")
		self.student_table.heading("DOB", text = "Date of Birth")
		self.student_table.heading("Phone", text = "Phone No.")
		self.student_table.heading("Email", text = "Email ID")
		self.student_table.heading("Address", text = "Address")
		self.student_table.heading("Blood Group", text = "Blood Group")
		self.student_table.heading("Photo", text = "Photo")

		#showing
		self.student_table["show"] = "headings"


		#setting width of columns
		self.student_table.column("department", width = 100)
		self.student_table.column("Course", width = 100)
		self.student_table.column("year", width = 50)
		self.student_table.column("Sem", width = 50)
		self.student_table.column("ID", width = 100)
		self.student_table.column("Name", width = 100)
		self.student_table.column("Div", width = 50)
		self.student_table.column("roll", width = 50)
		self.student_table.column("Gender", width = 50)
		self.student_table.column("DOB", width = 100)
		self.student_table.column("Phone", width = 100)
		self.student_table.column("Email", width = 100)
		self.student_table.column("Address", width = 100)
		self.student_table.column("Blood Group", width = 50)
		self.student_table.column("Photo", width = 100)


		self.student_table.pack(fill=BOTH, expand=1)
		self.student_table.bind("<ButtonRelease>",  self.get_cursor)
		self.fetch_data()

	# ================= Function Declerations ==================
	def add_data(self):
		if self.var_dep.get() == "Select Department" or self.var_std_id.get() =="" or self.var_std_name.get() == "":
			messagebox.showerror("Error", "all filled are req.", parent = self.root)
		else:
			# messagebox.showinfo("Success", "Welcome Biru")
			try:
				conn = mysql.connector.connect(host = "localhost", username = "root", password = "biru@2002", database = "face_recognizer")
				my_cursur = conn.cursor()
				my_cursur.execute("INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
																																																		self.var_dep.get(), 
																																																		self.var_course.get(), 
																																																		self.var_year.get(), 
																																																		self.var_semester.get(),
																																																		self.var_std_id.get(), 
																																																		self.var_std_name.get(), 
																																																		self.var_div.get(), 
																																																		self.var_roll.get(), 
																																																		self.var_gender.get(), 
																																																		self.var_dob.get(), 
																																																		self.var_email.get(), 
																																																		self.var_phone.get(), 
																																																		self.var_address.get(), 
																																																		self.var_blood_group.get(), 
																																																		self.var_radio1.get()
																																																))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("seccess", "student detail has been added", parent = self.root)
			except Exception as es:
				messagebox.show("Error", f"Due to : {str(es)}", parent = self.root)
	
	# ================fetching the data====================
	def fetch_data(self):
		conn = mysql.connector.connect(host = "localhost", username = "root", password = "biru@2002", database = "face_recognizer")
		my_cursur = conn.cursor()
		my_cursur.execute("SELECT * FROM student")
		data = my_cursur.fetchall()

		if len(data) != 0:
			self.student_table.delete(*self.student_table.get_children())
			for i in data:
				self.student_table.insert("", END, values = i)
			conn.commit()
		conn.close()


	# ===================Get cursor================
	def get_cursor(self, event = ""):
		cursor_focus = self.student_table.focus()
		content = self.student_table.item(cursor_focus)
		data = content["values"]

		self.var_dep.set(data[0]), 
		self.var_course.set(data[1]), 
		self.var_year.set(data[2]), 
		self.var_semester.set(data[3]),
		self.var_std_id.set(data[4]),
		self.var_std_name.set(data[5]),
		self.var_div.set(data[6]),
		self.var_roll.set(data[7]),
		self.var_gender.set(data[8]),
		self.var_dob.set(data[9]),
		self.var_email.set(data[10]),
		self.var_phone.set(data[11]),
		self.var_address.set(data[12]),
		self.var_blood_group.set(data[13]),
		self.var_radio1.set(data[14])
		


	# ============Update Function===========
	# ... (previous code)

# ============ Update Function ============
	def update_data(self):
		if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
			messagebox.showerror("Error", "All fields are required.", parent=self.root)
		else:
			try:
				Updatee = messagebox.askyesno("Update", "Do you want to update", parent=self.root)
				if Updatee > 0:
					conn = mysql.connector.connect(host="localhost", username="root", password="biru@2002", database="face_recognizer")
					my_cursor = conn.cursor()
					my_cursor.execute(
						"UPDATE student SET Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Blood_Group = %s, PhotoSample = %s WHERE Student_id = %s",
						(
							self.var_dep.get(),
							self.var_course.get(),
							self.var_year.get(),
							self.var_semester.get(),
							self.var_std_name.get(),
							self.var_div.get(),
							self.var_roll.get(),
							self.var_gender.get(),
							self.var_dob.get(),
							self.var_email.get(),
							self.var_phone.get(),
							self.var_address.get(),
							self.var_blood_group.get(),
							self.var_radio1.get(),
							self.var_std_id.get()
						)
					)
					messagebox.showinfo("Success", "Student Details Updated Successfully", parent=self.root)
					conn.commit()
					self.fetch_data()
					conn.close()
			except Exception as es:
				messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

# ======================Delete Function====================
	def delete_data(self):
		if self.var_std_id == "":
			messagebox.showerror("Error", "Student_id is required", parent = self.root)
		else:
			try:
				delete = messagebox.askyesno("Confirmation", "Are You Sure To Delete?", parent=self.root)
				if delete > 0:
					conn = mysql.connector.connect(host="localhost", username="root", password="biru@2002", database="face_recognizer")
					my_cursor = conn.cursor()
					sql = "delete from student where Student_id = %s"
					val = (self.var_std_id.get(), )
					my_cursor.execute(sql, val)
				else:
					if not delete :
						return 

				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Messege", "Deleted🤷‍♀️", parent=self.root)
			except Exception as es:
				messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

	# =================Reset button =================
	def reset_data(self):
		self.var_dep.set("Select Department")
		self.var_course.set("Course")
		self.var_year.set("Select Year")
		self.var_semester.set("Semester")
		self.var_std_id.set("")
		self.var_std_name.set("")
		self.var_div.set("Division")
		self.var_roll.set("")
		self.var_gender.set("Gender")
		self.var_dob.set("")
		self.var_email.set("")
		self.var_phone.set("")
		self.var_address.set("")
		self.var_blood_group.set("")
		self.var_radio1.set("")


		# =============Generate data set and take photo sample============
	def generate_dataset(self):
		if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
			messagebox.showerror("Error", "All fields are required.", parent=self.root)
		else:
			try:
				conn = mysql.connector.connect(host="localhost", username="root", password="biru@2002", database="face_recognizer")
				my_cursor = conn.cursor()
				my_cursor.execute("SELECT * FROM student")
				myresult = my_cursor.fetchall()
				id = 0
				for x in myresult:
					id+=1
				my_cursor.execute(
					"UPDATE student SET Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Blood_Group = %s, PhotoSample = %s WHERE Student_id = %s",
					(
						self.var_dep.get(),
						self.var_course.get(),
						self.var_year.get(),
						self.var_semester.get(),
						self.var_std_name.get(),
						self.var_div.get(),
						self.var_roll.get(),
						self.var_gender.get(),
						self.var_dob.get(),
						self.var_email.get(),
						self.var_phone.get(),
						self.var_address.get(),
						self.var_blood_group.get(),
						self.var_radio1.get(),
						self.var_std_id.get() == id+1
					)
				)
				conn.commit()
				self.fetch_data()
				self.reset_data()
				conn.close()


				#============Load predefined data on  face frontol from opencv==============
				face_calssifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
				def face_cropped(img):
					gray = cv2.cvtColor(img,   cv2.COLOR_BGR2GRAY)
					faces = face_calssifier.detectMultiScale(gray, 1.3, 5)
					#scaling factor = 1.3
					#minimum neighbour = 5

					for (x, y, w, h) in faces:
						face_cropped = img[y:y+h, x:x+w]
						return face_cropped
						
				cap = cv2.VideoCapture(0)
				img_id = 0
				while(True):
					ret, my_frame = cap.read()
					if face_cropped(my_frame) is not None:
						img_id += 1
						
						face = cv2.resize(face_cropped(my_frame), (450, 450))
						face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
						file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
						cv2.imwrite(file_name_path, face)
						cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 150), 2)
						cv2.imshow('Face', face)

					if cv2.waitKey(1) == 13 or int(img_id) == 100:
						break
				cap.release()
				cv2.destroyAllWindows()

				messagebox.showinfo("Result", "Generating data set Complited sussefully!!!")
				
			except Exception as es:
				messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)

























if __name__ == "__main__":
	root = Tk()
	obj = Students(root)
	root.mainloop()
        