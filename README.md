

# Colour Palette extraction using Unsupervised Learning
Extracting 5-colour palettes from various images using unsupervised learning and visualising their relation to one another
## Code
The source code is split into two parts:
1. Python code to extract a 5-Colour Hexadecimal Palette from an image.
2. Python code to visualise the relation between a list of the above extracted palettes.
## 1) Palette Extraction
The 5 colour palettes were extracted by converting the image to a 2D matrix of RGB Values(Nx3), which was used as input for the Mini Batch K-Means Clustering algorithm to return the colours(hex) from the five cluster centers. Here are some examples:
 
![Palette Examples](https://user-images.githubusercontent.com/82210227/129468364-f7f9a8a8-f2bb-491e-94bc-cf5d3c9d4b9b.png)
- *(Image 1: Schiaparelli Fall 21 Couture (Look 23))*
- *(Image 2: Van Gogh-Sunflowers (fourth version))*
## 2) Palette Visualisation
![FW 21 Kernel PCA](https://user-images.githubusercontent.com/82210227/129468412-38535f23-6856-408b-8b58-d7238a69bb4e.png)
## Part 3
![FW 21 t-SNE](https://user-images.githubusercontent.com/82210227/129468410-a9a90e88-7d1d-4ead-8e8e-cf7e7bcaccb1.png)

## Part 4
![Netflix](https://user-images.githubusercontent.com/82210227/129468416-0bec85cf-67e6-4532-a1ed-617b0455db08.png)
![Fall 21 Couture](https://user-images.githubusercontent.com/82210227/129468419-04e7a777-a80c-4569-8131-e0c3a0dbd6d2.png)
