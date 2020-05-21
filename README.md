# Unsupervised_ML_from_scratch
This repository is dedicated for those who would like to get a hands-on experiense in Unsupervised Machine Learning algorithms. The idea is to write the algorithms from scratch based on the intrinsic understanding of the algorithm, i.e., with the minimum necessary extra packages. I will describe the algorithm and upload my Python codes. The comments are welcome. I got an initial idea from the book "Machine Learning for Human Beings" by Mohit Deshpande however the further improvements and advances and the complete program I wrote by myself.


1) First of all, we will generate the sample dataset. Run the code as 
python Generating_Blobs.py

The code will create the Data/ folder if it is not present. And save the generated dataset into this folder. Also, we are saving the labels for each data point (for the visualization purposes).

2) Run the visualising code as
python 2.Visualising_Data.py

The code will read the .txt file from Data folder and visualize it, then save the plots into Plots/ folder (again, if it is not present the code takes care of creating it).

3) Run K-means, unsupervised machine learning algorithm for separating our unlabeled dataset. 
python 3.K_means.py
or run with the option to control the number of clusters to fit directly from the terminal, such as
python 3.K_means.py N 
--> to run the code for N clusters

The code runs the algorithm, updates the cluster centers for every step, and creates nice "step-by-step" plot.

4) Create the Animation from the result by running
python 4.Animating_K_means_clustering.py
or run with the option to control the number of clusters to fit directly from the terminal, such as
python 4.Animating_K_means_clustering.py N 
--> to run the code for N clusters

The code creates the animation using imageio python module and saves into the dedicated folder. The system of the folders is crated wise, so the user can easily orient in the output Plots/ folders.


