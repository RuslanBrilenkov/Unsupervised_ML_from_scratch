
__author__ = "Ruslan Brilenkov"
__copyright__ = "Copyright 2020, Unsupervised ML in Python from scratch project"
__credits__ = ["Ruslan Brilenkov"]
__email__ = "ruslan.brilenkov@gmail.com"


def CreateAnimation():
	
	import imageio
	import glob
	
	# we will be creating the ,GIF animation using the following images
	print("we will be creating the ,GIF animation using the following images")
	pathToImages = "Plots/K_means_Plots/"
	sortedList = sorted(list(glob.glob(pathToImages+"*.png")))
	print(sortedList)
	
	data_images = []
	for image in sortedList:
		data_images.append(imageio.imread(image))
	
	#print(len(sortedList))
	
	#data_images = imageio.imread(sortedList)
	imageio.mimwrite(pathToImages+"Animation.gif", data_images, fps = 3, loop = 5)
	#plt.savefig(folderPlotsName+folderAlgorithmName+"k_means_step"+str(MyIndex)+".png", bbox_inches='tight', overwrite=True)
	#MyIndex += 1
		
# Let's try to call the class functions
if (__name__=='__main__'):
    
    CreateAnimation()
