
__author__ = "Ruslan Brilenkov"
__copyright__ = "Copyright 2020, Unsupervised ML in Python from scratch project"
__credits__ = ["Ruslan Brilenkov"]
__email__ = "ruslan.brilenkov@gmail.com"


def CreateAnimation(k):
	
	import imageio
	import glob
	
	# we will be creating the ,GIF animation using the following images
	print("we will be creating the ,GIF animation using the following images ...")
	
	try:
		
		pathToImages = "Plots/K_means_Plots/"+k+"/"
		pathToImages2 = "Plots/K_means_Plots/"
		sortedList = sorted(list(glob.glob(pathToImages+"*.png")))
		print(sortedList)
	
		data_images = []
		for image in sortedList:
			data_images.append(imageio.imread(image))
		
		#print(len(sortedList))
		
		#data_images = imageio.imread(sortedList)
		imageio.mimwrite(pathToImages2+"Animation_k="+k+".gif", data_images, fps = 3, loop = 5)
		#plt.savefig(folderPlotsName+folderAlgorithmName+"k_means_step"+str(MyIndex)+".png", bbox_inches='tight', overwrite=True)
		#MyIndex += 1
	except Exception as e:
		print(e)
		print("Ruslan: Check if folder " + pathToImages + " exists!")
		
# Let's try to call the class functions
if (__name__=='__main__'):
    
    
	import os, sys

	try: 
		clustNumber = sys.argv[1]
		print("You specified the number of clusters = {}".format(clustNumber))
	except Exception as e:
		print(e)
		print("You did not specify the number of clusters\nYou can run the code with the following option")
		print("\n>>python 3.K_means.py <number of clusters>\n")
		clustNumber = 2
		print("assuming number of clusters = {}".format(clustNumber))
    
	CreateAnimation(k=clustNumber)
    
