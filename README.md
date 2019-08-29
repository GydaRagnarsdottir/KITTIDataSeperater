# DataSeperater
Seperate KITTI data for Voxelnet. It can also be modified to seperate other data sample

Usage:
1. Copy seperateSamples.py to your [VoxelnetRoot] folder
2. Run it with command "python seperateSamples.py" in terminal
3. Enter the path of the file according to which you want your data to be seperated. (In the case of Voxelnet, the Protocol)
4. Enter the path of the root folder of the source data (Train/Validation/Test, once at a time)
5. Enter the path of the root folder of the destination data 
All three kinds of data(image_2,label_2,velodyne) will be copied from the corresponding folders in [sourceRoot] to those in [destinationRoot]
