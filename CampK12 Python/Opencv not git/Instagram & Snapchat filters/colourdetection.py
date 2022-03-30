import cv2 as cv
import numpy as np
import pandas as pds
# pip install pandas
# Importing the image and the csv

image = 'colourpallete.jpeg'
img = cv.imread(image)

index = ['color','color_name', 'hex','R','G','B']
csv_data = pds.read_csv('colors.csv', names = index, header = None)

def getColorName(R,G,B):
    minimum = 10000 
    for i in range(len(csv_data)):
        data = abs(R-int(csv_data.loc[i,'R'])) +  abs(G-int(csv_data.loc[i,'G'])) + abs(B-int(csv_data.loc[i,'B']))

        if (data < minimum):
            minimum = data
            colorName = csv_data.loc(i,'color_name')
        return colorName

# 60 red and 40 blue
#  (x,y) 
def draw_function(event,x,y,flags,param):
  if event == cv.EVENT_LBUTTONDBLCLK:
    global b,g,r,xpos,ypos,clicked
    clicked = True
    xpos = x
    ypos = y
    b,g,r = img[y,x] # Colors in b,g,r format
    b = int(b)
    g = int(g)
    r = int(r)


cv.namedWindow('image')
cv.setMouseCallback('image',draw_function)

while(1):
    cv.imshow('image',img)
    if clicked == True:
        cv.rectangle(img, (21, 21),(64, 64),(b,g,r),-1)
        if cv.waitKey(20) & 0xFF == 'q':
            break
    
cv.destroyAllWindows()

  