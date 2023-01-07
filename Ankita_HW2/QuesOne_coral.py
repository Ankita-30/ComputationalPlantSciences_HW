"""
How have we defined length?

Let us consider traversing the fingerprint pattern by each row of pixels. So, we have defined total length as sum of length of each row. 
Length of each row is obtained by counting the no. of black pixels in the binary image and then calculating length of those 
pixels in inches using 'dpi'. Average length is obtained by dividing total length by size of the image/length of the list.

I have used just the Python Imaging Library (PIL) for my code.

"""

from PIL import Image
#load image from desktop
im = Image.open("coral.png")
#convert png to jpg
im2=im.convert("L")
#save converted image
im2.save("c.jpg")
#set your threshold
threshold = 100
#convert image into binary
img = im2.point(lambda p: p > threshold and 255)
#save binary image as binaryF
img.save("binaryC.jpg")
#Load pixels of image
pixels = img.load()
#Initialize count
cnt =0

#Initialize list for storing number of pixels in each row
P=[]
#Initialize list for storing length of each row
R=[]

#get dpi of image
L=img.info["dpi"]
dpi=L[0]

#Calculate number of black pixels in the image in each row
for i in range(img.size[0]):    
    for j in range(img.size[1]):
    	
        if(pixels[i,j]==0):
    		cnt = cnt+1

    #Append the number of black pixels in a row to list
    P.append(cnt)
    #get length of row in inches
    length=cnt/float(dpi)
    #Append the length of each row to list
    R.append(length)
    #Make cnt zero before moving to the next row
    cnt=0



#Calculate average length
Total_lengthpixels=sum(P)
Total_lengthinches=sum(R)

#Print your value
print "Total length of the coral pattern is " + str(Total_lengthpixels) +" pixels."
print "Total length of the coral pattern is " + str(Total_lengthinches) +" inches."

"""
I feel the value in inches is too high and that might be because of using 'dpi' to convert pixels into inches which might not be entirely correct. I am confused between 
'dpi' and 'ppi'. My reference for using 'dpi' is as follows: https://www.iprintfromhome.com/mso/understandingdpi.pdf.

"""

#Obtain average length in pixels
x=len(P)
Avg_lengthpixels=Total_lengthpixels/float(x)

#Obtain average length in inches
y=len(R)
Avg_lengthinches=Total_lengthinches/float(y)

#Print your value
print "Average length of the coral pattern is " + str(Avg_lengthpixels) +" pixels."
print "Average length of the coral pattern is " + str(Avg_lengthinches) +" inches."
