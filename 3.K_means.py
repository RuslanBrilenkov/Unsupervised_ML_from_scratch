
__author__ = "Ruslan Brilenkov"
__copyright__ = "Copyright 2020, Unsupervised ML in Python from scratch project"
__credits__ = ["Ruslan Brilenkov"]
__email__ = "ruslan.brilenkov@gmail.com"


class KMeans(object):
	"""
	Implementation of K-Means Clustering
	"""

	# __init__ method will run authomatically upon calling the class
	# we want import a number of clusters which we want to fit to our data
	def __init__(self, k):
		self.k = int(k)
    
	def ReadData(self):

		data = np.loadtxt("Data/K-means-Data.txt", delimiter=',')
		#labels = np.loadtxt("Data/K-means-Data-labels.txt", delimiter=',')

		return data#, labels
	
	'''
	def plot(self, X):
		
		# randomly creating the cluster centers
		self.centers = X[np.random.randint(X.shape[0], size=self.k)]
		
		plt.figure(figsize=[14,12])        
		
		# plotting the data points as blue plusses
		plt.plot(X[:,0], X[:,1], 'b+', markersize=30, markeredgewidth = 5)
				# plotting randomly generated K-centers as red circles
		plt.plot(self.centers[:,0], self.centers[:,1], 'ro', markersize = 32)
		plt.xlabel('feature 1', fontsize=18)
		plt.ylabel('feature 2', fontsize=18)
		plt.show()
	'''
     

	def get_cmap(self, n, name='jet'):
		# This is taken from https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib
		'''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
		RGB color; the keyword argument name must be a standard mpl colormap name.'''
		return plt.cm.get_cmap(name, n)
		
	def ColorPlotInitialize(self, X):
		
		
		
		'''
		Initializing k-clusters at random positions and assigning 
		the nearest data points to the closest cluster center
		'''		
		
		# Checking if folder names "Plots/" is present / create one if not.
		folderPlotsName = "Plots/"
		if not os.path.exists(folderPlotsName):
			os.makedirs(folderPlotsName)

		# creating colors to paint data points
		# !!! This part should be improved to the case of arbitrary number of clusters
		colorArray = ["red", "blue", "green", "orange", "violet", "brown"]
		colors = random.choice(colorArray)

		# randomly assigning the positions of cluster centers
		#print(X.shape[0])
		#print(self.k)
		#print(np.random.randint(low=-50, high=+50, size=int(self.k)))
		self.centers = X[np.random.randint(X.shape[0], size=self.k )]
		
		#print(self.centers)
		
		# calculating the distances from each cluster center to every point in the dataset
		distances = np.sqrt(np.sum((X - self.centers[:, np.newaxis]) ** 2, axis=2))
		# chosing the closest data points
		closestClusters = np.argmin(distances, axis=0)
		
		# Visualizing the initial random cluster distribution
		plt.figure(figsize=[14,12])        

		# plotting data ploints with the colors relative to which cluster they are assigned to.
		# and plotting randomly generated K-centers as red circles with relative colors
		self.cmap = self.get_cmap(self.k)
		for j in range(self.k ):
			plt.scatter(X[:,0][closestClusters == j], X[:,1][closestClusters == j], color=self.cmap(j), marker='+', s=500)
			plt.plot(self.centers[j,0], self.centers[j,1], 'o', c = self.cmap(j), markersize = 32)

		plt.xlabel('feature 1', fontsize=18)
		plt.ylabel('feature 2', fontsize=18)
		#plt.show()
		plt.savefig(folderPlotsName+"k_means_initialize_color.png", bbox_inches='tight', overwrite=True)
		
		
	def MeatOfProgram(self, X):
		
		'''
		1) Initializing k-clusters at random positions and assigning 
		the nearest data points to the closest cluster center
		
		2) Determining the mean of the 
		'''		
		
		# Checking if folder names "Plots/" is present / create one if not.
		folderPlotsName = "Plots/"
		if not os.path.exists(folderPlotsName):
			os.makedirs(folderPlotsName)

		# Creating another folder - to contain the plots of the algorithm
		folderAlgorithmName = "K_means_Plots/"
		if not os.path.exists(folderPlotsName+folderAlgorithmName):
			os.makedirs(folderPlotsName+folderAlgorithmName)
			
		# Creating a folder to save a set of plots from each particular k-value
		folderKvalueName = str(self.k)+"/"
		if not os.path.exists(folderPlotsName+folderAlgorithmName+folderKvalueName):
			os.makedirs(folderPlotsName+folderAlgorithmName+folderKvalueName)
			
		# creating colors to paint data points
		# !!! This part should be improved to the case of arbitrary number of clusters
		colors = ["red", "blue", "green", "orange", "violet", "brown"]

		# randomly assigning the positions of cluster centers
		self.centers = X[np.random.randint(X.shape[0], size=self.k)]

		# There is a meat of the algorithm - for this we will have to loop this part until 
		# the algorithm converges
		        
		
		MyIndex = 0
		
		while True:
			# calculating the distances from each cluster center to every point in the dataset
			distances = np.sqrt(np.sum((X - self.centers[:, np.newaxis]) ** 2, axis=2))
			# chosing the closest data points
			closestClusters = np.argmin(distances, axis=0)

			# assigning new k clusters based on the mean of the closest centers
			newCenters = np.array([np.mean(X[closestClusters == c], axis=0) for c in range(self.k)])
			
			# To break the loop in case of convergence 
			if np.all(self.centers - newCenters < 1e-5):
				break
			self.centers = newCenters
			
			# Visualizing the initial random cluster distribution
			plt.figure(figsize=[14,12])

			# plotting data ploints with the colors relative to which cluster they are assigned to.
			# and plotting randomly generated K-centers as red circles with relative colors
			self.cmap = self.get_cmap(self.k)
			for j in range(self.k):
				plt.scatter(X[:,0][closestClusters == j], X[:,1][closestClusters == j], color=self.cmap(j), marker='+', s=500)
				plt.plot(self.centers[j,0], self.centers[j,1], 'o', c = self.cmap(j), markersize = 32)

			plt.xlabel('feature 1', fontsize=18)
			plt.ylabel('feature 2', fontsize=18)
			#plt.show()
			plt.savefig(folderPlotsName+folderAlgorithmName+folderKvalueName+"k="+str(self.k)+"_k_means_step"+str(MyIndex)+".png", bbox_inches='tight', overwrite=True)
			MyIndex += 1
		
# Let's try to call the class functions
if (__name__=='__main__'):
    
	import numpy as np
	import matplotlib.pyplot as plt

	import random
	import os, sys
		
	# The usage of this addition would be:
	# python 3.K_means.py <number of clusters>
	# if number of clusters is not specified, then taken, for instance, 2.
	
	try: 
		clustNumber = sys.argv[1]
		print("You specified the number of clusters = {}".format(clustNumber))
	except Exception as e:
		print(e)
		print("You did not specify the number of clusters\nYou can run the code with the following option")
		print("\n>>python 3.K_means.py <number of clusters>\n")
		clustNumber = 2
		print("assuming number of clusters = {}".format(clustNumber))
		
		
	#print(clustNumber)
	
	# calling the class methods
	kmeans = KMeans(k=clustNumber)
	
	# reading data and their labels (by calling the method inside the class)
	Mydata = kmeans.ReadData()
	
	# Initializing k-clusters at random positions and assigning data to the nearest cluster
	# (by calling the method inside the class)
	kmeans.ColorPlotInitialize(Mydata)
	
	# The "meat" of teh lagorithm - reassigning the cluster centers based on the mean of all assigned points
	kmeans.MeatOfProgram(Mydata)
