This project detects the number of fingers held up ...

For this to work optimally :
1. Make sure you're using this in a place where there is minimal background noise ie plain background is prefered 
2. Make sure you're face isnt in the region of intrest which is marked by the white box  


This model was made by given pictures of my fingers 
It was compiled by using 20 training images and 5 test images , and the results are pretty decent if used as instructed .


Algorithm :
1. Make training and testing images 
2. resize them to 64x64 size grayscale images
3. pass them into a neural network and make a ".h5" file 
4. make another python script which would use openCV to use the camera and make a Region of intrest (roi)
5. This roi will be converted into a 64x64 size grayscale image 
6. This new roi will be passed into the model and its corresponding output/value is printed.








