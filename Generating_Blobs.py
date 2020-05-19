from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

def main():
	centers = [(-5, -10), (0, 5), (5, 15),  (10, -10), (-15, 5)]
	# create blobs
	data = make_blobs(n_samples=500, n_features=2, centers=centers, cluster_std=2.0, random_state=42)
	# create np array for data points
	points = data[0]

	color = ["red", "blue", "green", "orange", "violet", "brown"]

def MakePlot():
	
	
	plt.figure()
	plt.scatter(data[0][:,0], data[0][:,1], c=color[3], cmap='viridis')
	plt.xlim(-20,20)
	plt.ylim(-20,20)
	plt.savefig('random_blobs,png')

def Create_More_Plots():
	
	#data = main().data
	
	# create scatter plot
	plt.figure(figsize=[14,12])
	plt.scatter(data[0][:,0], data[0][:,1], c=data[1], cmap='viridis')
	plt.xlim(-20,20)
	plt.ylim(-20,20)
	plt.xlabel('feature 1', fontsize=18)
	plt.ylabel('feature 2', fontsize=18)
	plt.savefig("data_colored.png", bbox_inches='tight', overwrite=True)

	plt.figure(figsize=[14,12])
	plt.scatter(data[0][:,0], data[0][:,1], color='black')
	plt.xlim(-20,20)
	plt.ylim(-20,20)
	plt.xlabel('feature 1', fontsize=18)
	plt.ylabel('feature 2', fontsize=18)
	plt.savefig("data_uncolored.png", bbox_inches='tight', overwrite=True)

if (__name__=="__main__"):
	
	#main()
	
	centers = [(-5, -10), (0, 5), (5, 15),  (10, -10), (-15, 5)]
	# create blobs
	data = make_blobs(n_samples=500, n_features=2, centers=centers, cluster_std=2.0, random_state=42)
	# create np array for data points
	points = data[0]

	color = ["red", "blue", "green", "orange", "violet", "brown"]
	
	#MakePlot()	
	Create_More_Plots()

