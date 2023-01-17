from fiji.util.gui import GenericDialogPlus

# Create an instance of GenericDialogPlus
gui = GenericDialogPlus("HREM GUIde")

# Add some gui elements (Ok and Cancel button are present by default)
# Elements are stacked on top of each others by default (unless specified)

# Add possibility to choose some images already opened in Fiji
gui.addMessage("If Images are already open, select them below:")
gui.addImageChoice("HREM Stack Image","Some description for image1")
gui.addImageChoice("HREM Calibration Image","Some description for image2")

# We can add elements next to each other using the addToSameRow method
#gui.addToSameRow() # The next item is appended next to the tick box

gui.addMessage("If Images are not open, choose image folder below:")
# The GenericDialogPlus also allows to select files, folder or both using a browse button
gui.addDirectoryField("HREM Stack folder path", "DefaultFolderPath")
gui.addFileField("HREM Calibration Image file path", "DefaultFilePath")
def open_images():
	print("Sup yo")
gui.addButton("Open Images", open_images)
#Set name and date if not found by parameters
gui.addMessage("") #set extra line
gui.addMessage("Set some basic parameters for HREM Data")
gui.addStringField("Your Name :", "Paul Revere")
gui.addStringField("Aquistion Date (YYYYMMDD) : ", "17760704")

#gui.addNumericField("Image number for calibration slide", 10, 0) # 0 for no decimal part
#gui.addDirectoryOrFileField("Some_Path", "DefaultPath")

# Add a Help button in addition to the default OK/Cancel
gui.addHelp(r"https://imagej.net/scripting/generic-dialog") # clicking the help button will open the provided URL in the default browser
#gui.addNumericField("Some integer", 10, 0) # 0 for no decimal part
gui.addCheckbox("Tick Box to Invert data", True)
gui.addCheckbox("Flat Field Correct", True)
gui.addNumericField("Slice number flat field", 10, 0) 
gui.addChoice("Select output bit depth to save at", ["16", "8"], "16") # 16 bit is default here

#def invert():
#	print("Sup yo")
#gui.addButton("Invert Image", invert)
# Show dialog, the rest of the code is not executed before OK or Cancel is clicked
gui.showDialog() # dont forget to actually display the dialog at some point


# Recover the inputs in order of "appearance"
if gui.wasOKed():
    image1 = gui.getNextImage() # This method directly returns the ImagePlus object
    image2 = gui.getNextImage()

    # Path are recovered as string
    name   = gui.getNextString() #name
    date = gui.getNextString() #date
    somePath   = gui.getNextString()
    inString = gui.getNextString()
    inBool   = gui.getNextBoolean()
    inChoice = gui.getNextChoice() # one could alternatively call the getNextChoiceIndex too
    inNum    = gui.getNextNumber() # This always return a double (ie might need to cast to int)