import numpy as np
import scipy


def gaussian_filter_center(image, sigma):
    z, y, x = image.shape

    mid_z = z // 4
    mid_y = y // 4
    mid_x = x // 4

    filtered_image = np.array(image)
    filtered_image[mid_z:3 * mid_z, mid_y:3 * mid_y, mid_x:3 * mid_x] = scipy.ndimage.gaussian_filter(image[mid_z:3 * mid_z, mid_y:3 * mid_y, mid_x:3 * mid_x], sigma=sigma)
    
    return filtered_image


def gaussian_filter_except_center(image, sigma):
    z, y, x = image.shape

    mid_z = z // 4
    mid_y = y // 4
    mid_x = x // 4

    filtered_image = scipy.ndimage.gaussian_filter(image, sigma=sigma)
    filtered_image[mid_z:3 * mid_z, mid_y:3 * mid_y, mid_x:3 * mid_x] = image[mid_z:3 * mid_z, mid_y:3 * mid_y, mid_x:3 * mid_x]
    
    return filtered_image
