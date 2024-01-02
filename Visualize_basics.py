import numpy as np
import matplotlib.pyplot as plt
def color_transform(color = 'None'):
    if color == 'Black':
        RGB = [0, 0, 0]
    if color == 'White':
        RGB = [255, 255, 255]
    if color == 'Red':
        RGB = [255, 0, 0]
    if color == 'Blue':
        RGB = [0, 0, 255]
    if color == 'Yellow':
        RGB = [255, 255, 0]
    if color == 'intensity':
        return None
    RGB = np.asarray(RGB)
    return  RGB/255

def intensity_transformation(pcd):
    intensity = pcd[:, 3]
    min_intensity = np.min(intensity)
    max_intensity = np.max(intensity)
    colors = (intensity - min_intensity) / (max_intensity - min_intensity)
    return colors