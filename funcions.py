import numpy as np
from PyQt5 import QtGui
from qimage2ndarray import gray2qimage

def array_to_pixmap(array):

    transformedimg_qimg = gray2qimage(array)
    pixmapimage = QtGui.QPixmap.fromImage(transformedimg_qimg)
    return pixmapimage

def box(clwidth, rowwidth, img, imgwidth, imgheight):
    img[0:rowwidth, 0:] = 0  # row1
    img[imgheight - rowwidth:imgheight, 0:] = 0  # row2
    img[0:, 0:clwidth] = 0  # col1
    img[0:, imgwidth - clwidth:imgwidth] = 0  # col2
    return img



def Bluring_FourierTransform(Recievedimg,counter,cols,rows):
    f = np.fft.fft2(Recievedimg)
    fshift = np.fft.fftshift(f)
    fshift = box(counter, counter, fshift, cols, rows)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    #magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    return  magnitude_spectrum

def Bluring_InverseFourierTransform(Recievedimg,counter,cols,rows):
    f = np.fft.fft2(Recievedimg)
    fshift = np.fft.fftshift(f)
    fshift = box(counter, counter, fshift, cols, rows)
    f_inverseshift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_inverseshift)
    img_back = np.abs(img_back)
    #img_back = np.asarray(img_back, dtype=np.uint8)
    return img_back



def Edge_Detection_Fourier_Transform(img,counter,rows,cols):

    crow = int(rows/2)
    ccol = int(cols/2)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    fshift[crow - counter:crow + counter, ccol - counter:ccol + counter] = 0
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    #magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    return magnitude_spectrum

def Edge_Detection_Inverse_Fourier_Transform(img,counter,rows,cols):

    crow=int(rows/2)
    ccol=int(cols/2)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    fshift[crow - counter:crow + counter, ccol - counter:ccol + counter] = 0
    f_inverseshift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_inverseshift)
    img_back = np.abs(img_back)
    #img_back = np.asarray(img_back, dtype=np.uint8)
    return img_back
