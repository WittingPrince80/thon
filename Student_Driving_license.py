# Basic tkinter template
from tkinter import *
root= Tk()

root.title("Driving Licence")
root.geometry("400x200")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
idd ='ID: 9127282019'
show_result["text"]=idd

name ='Name: Mr Name'
show_result["text"]=name

DOM ='Date Of Birth: 99/99/999'
show_result["text"]=DOB

PIN ='PIN: 84630'
show_result["text"]=PIN

Add ='Address: 19 Name Street Mars'
show_result["text"]=Add


Ath ='Licence for: Flying Car, 8 wheel drive'
show_result["text"]=Ath

# Define the function

    
    
# Create a button



# tkinter basic template end statement
root.mainloop()