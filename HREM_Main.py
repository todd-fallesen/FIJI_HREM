from fiji.util.gui import GenericDialogPlus
gui = GenericDialogPlus("HREM GUIde")

def open_images():
	print("Sup yo")

gui.addMessage("Basic Functions for HREM analysis") #set extra line
gui.addMessage("") #set extra line
gui.addButton("Open Images", open_images)
gui.addMessage("") #set extra line
gui.addButton("Calibrate Grat", open_images)
gui.addMessage("") #set extra line
gui.addButton("Set Metadata", open_images)
gui.addMessage("") #set extra line
gui.addButton("Save Image Stack", open_images)
gui.addMessage("") #set extra line

gui.showDialog()