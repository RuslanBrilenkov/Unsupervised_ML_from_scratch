from sklearn.datasets import make_blobs
import numpy as np
import os


def main():
	centers = [(-5, -10), (0, 5), (5, 15),  (10, -10), (-15, 5)]
	# create blobs
	data = make_blobs(n_samples=500, n_features=2, centers=centers, cluster_std=2.0, random_state=42)

	# Create the folder called "Data/" if it is not present
	folderName = "Data/"
	if not os.path.exists(folderName):
		os.makedirs(folderName)
	
	# saving blobs/data into folder "Data/"
	np.savetxt(folderName+'K-means-Data.txt', data[0], delimiter=',')
	np.savetxt(folderName+'K-means-Data-labels.txt', data[1], delimiter=',')

if (__name__=="__main__"):
	
	main()
