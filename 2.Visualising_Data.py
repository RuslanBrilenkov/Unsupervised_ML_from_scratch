import os
import numpy as np
import matplotlib.pyplot as plt


def ReadData():
	
	data = np.loadtxt("Data/K-means-Data.txt", delimiter=',')
	labels = np.loadtxt("Data/K-means-Data-labels.txt", delimiter=',')
	
	return data, labels

def MakePlot(data, labels):
	
	# Checking if folder names "Plots/" is present / create one if not.
	folderPlotsName = "Plots/"
	if not os.path.exists(folderPlotsName):
		os.makedirs(folderPlotsName)
	
	plt.figure()
	plt.scatter(data[:,0], data[:,1], c=labels, cmap='viridis')
	plt.xlim(-120,120)
	plt.ylim(-120,120)
	plt.savefig(folderPlotsName+'random_blobs.png')

def Create_More_Plots(data, labels):
	
	# Checking if folder names "Plots/" is present / create one if not.
	folderPlotsName = "Plots/"
	if not os.path.exists(folderPlotsName):
		os.makedirs(folderPlotsName)
	
	# create a bit more advanced scatter plot than previous method
	plt.figure(figsize=[14,12])
	plt.scatter(data[:,0], data[:,1], c=labels, cmap='viridis', marker='+', s=500)
	plt.xlim(-120,120)
	plt.ylim(-120,120)
	plt.xlabel('feature 1', fontsize=18)
	plt.ylabel('feature 2', fontsize=18)
	plt.savefig(folderPlotsName+"data_colored.png", bbox_inches='tight', overwrite=True)

	# create another scatter plot
	plt.figure(figsize=[14,12])
	plt.scatter(data[:,0], data[:,1], color='black', marker='+', s=500)
	plt.xlim(-120,120)
	plt.ylim(-120,120)
	plt.xlabel('feature 1', fontsize=18)
	plt.ylabel('feature 2', fontsize=18)
	plt.savefig(folderPlotsName+"data_uncolored.png", bbox_inches='tight', overwrite=True)

if (__name__=="__main__"):
	
	# reading data and their labels
	Mydata, Mylabels = ReadData()
	
	MakePlot(Mydata, Mylabels)
	
	# If you would like a bit more advanced plotting 
	# with axes labels, 
	Create_More_Plots(Mydata, Mylabels)
