#Open images script in python
from ij import IJ, ImagePlus
from fiji.util.gui import GenericDialogPlus
from ij.plugin import FolderOpener

# Create an instance of GenericDialogPlus
gui = GenericDialogPlus("HREM GUIde")

# The GenericDialogPlus also allows to select files, folder or both using a browse button
gui.addDirectoryField("HREM Stack folder path", "DefaultFolderPath")
gui.addFileField("HREM Calibration Image file path", "DefaultFilePath")

gui.showDialog()

if gui.wasOKed():
	stack_path = gui.getNextString() #stack path string
	stackimage = FolderOpener.open(stack_path, "virtual");
	stackimage.show()
	grat_file = gui.getNextString() #grat file string
	gratimage = IJ.openImage(grat_file)
	gratimage.setTitle('Grat')
	gratimage.show()
