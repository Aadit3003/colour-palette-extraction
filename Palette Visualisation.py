# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, MiniBatchKMeans
from skimage import color
from collections import Counter
import cv2
import os

# 1) PROCESS THE 5-COLOUR EXTRACTED PALETTE
def rgb_from_hex(color_hex):
  # hex colours are R(0,1) G(2,3) B(4,5) in base 16
  return tuple(int(color_hex[i:i+2], 16) for i in (0,2,4))
# To sort the palette colours based on brightness
def sort_tuple(list_of_tuples):
    list_of_tuples.sort(key = lambda x: x[1]+x[0]+x[2])
    return list_of_tuples

def get_palette_from_string(palette_list):
  list = [rgb_from_hex(color[1:]) for color in palette_list]
  # Sort Colours by brightness (R+G+B roughly) (or else, Yellow Brown and Brown yellow are interpreted as different colours)
  return sort_tuple(list)
# Convert the Palettes from Hexadecimal to CIELAB colour space
def convert_palettes_to_lab(rgb_palettes):
  scaled_palettes = np.array([rgb_palettes]) / 255.0
  lab_palettes = color.rgb2lab(scaled_palettes)
  return lab_palettes.flatten()
# Obtain matrix of features X from a list of 5-colour palettes
def features_from_list_of_palettes(list_of_palettes):
    list_of_lists = []
    for palette_list in list_of_palettes:
        lab_palette = convert_palettes_to_lab(get_palette_from_string(palette_list))
        list_of_lists.append(lab_palette)

    X = np.array(list_of_lists)
    return X

def save_palette(palette, file_name):
    fig = plt.figure(figsize=(5, 1))
    length = len(palette)

    plt.bar(palette, [1] * length, color=palette, width=1)
    plt.axis('off')

    plt.savefig(file_name, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()

# 2) VISUALISE EXTRACTED COLOUR PALETTES (t-SNE)
# Obtain Image from the path given
def getImage(path, zoom):
    return OffsetImage(plt.imread(path), zoom=zoom)
# Add annotations (images of palettes) to the scatter plot
def scatter(X):
    fig, ax = plt.subplots(figsize=(32, 18))
    x = X[:, 0]
    y = X[:, 1]
    ax.scatter(x, y)
    for x0, y0, path in zip(x, y, paths):
        ab = AnnotationBbox(getImage(path, 0.08), (x0, y0), frameon=False)
        ax.add_artist(ab)
    plt.show()

# 3) DEMO
def main():
    # Input a list of 5-colour hexadecimal palettes
    list_of_palettes = [['#aca96a', '#030201', '#e0d689', '#c45a5f', '#f3f0ed'],
                        ['#000000', '#e4c2b4', '#9a7566', '#3a3534', '#685751'],
                        ['#807a70', '#f0de75', '#fbf9f8', '#020202', '#cac7c6'],
                        ['#000000', '#ebd28e', '#b98a71', '#3e3127', '#826150'],
                        ['#565867', '#b7c8d2', '#9197ae', '#ddebef', '#010101']]
    i = 0
    paths = [str(i) + ".png" for i in range(len(list_of_palettes))]
    for palette in list_of_palettes:
        save_palette(palette, paths[i])
        i += 1
    X = features_from_list_of_palettes(list_of_palettes)
    sc = StandardScaler()
    X = sc.fit_transform(X)

    from sklearn.manifold import TSNE

    X_embedding = TSNE(n_components=2).fit_transform(X)

    scatter(X_embedding)

if __name__ == "__main__":
    main()