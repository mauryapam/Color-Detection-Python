from cv2 import cv2
import numpy as np
import pandas as pd 

#to read  image
#image should be in same folder 
#if no input is given by default image (cherryblossoms.jpg ) will be read as input
img_name =input("Enter image name : ")
if len(img_name)<1 : img_name = "cherryblossoms.jpg"
img= cv2.imread(img_name)

#to view image
#cv2.imshow("colors_win", img)
#cv2.waitKey(0)


#reading a csv file 
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv("colors.csv", names=index, header=None)

moved= False
r = g = b = xpos = ypos = 0

#to get the name of the color
def getName(R,G,B):
    min=10000
    for i in range(len(csv)):
        #distance= abs(Red- ithRedcolor)+abs(Green - ithGreencolor)+ abs(Blue- ithBluecolor)
        distance= abs(R- int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"]))+ abs(B - int(csv.loc[i,"B"]))
        if(distance<=min):
            min= distance 
            clrname= csv.loc[i,"color_name"]
    return clrname

def draw_function(event,x,y,flags,param):
    if event== cv2.EVENT_MOUSEMOVE:
        global b,g,r,xpos,ypos,moved
        moved= True
        xpos= x
        ypos= y
        b,g,r= img[y,x]     #BGR, since OpenCV represents images as NumPy arrays in reverse order
        b= int(b)
        g= int(g)
        r= int(r)

cv2.namedWindow("colors_win")
cv2.setMouseCallback("colors_win", draw_function)

while (1):
    cv2.imshow("colors_win", img)
    if(moved):

        #text display config
        cv2.rectangle(img,( 20,20), (750,60),(b,g,r), -1)

        text= getName(r,g,b)+ " R="+ str(r) +" G="+str(g)+ " B="+str(b)

        cv2.putText(img, text, (50,50), 2,0.8 ,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>= 600):
            cv2.putText(img,text, (50,50),2,0.8,(0,0,0),2, cv2.LINE_AA)
        moved= False
    if cv2.waitKey(20) & 0xFF==27:
        break                   #press esc to exit
cv2.destroyAllWindows()
