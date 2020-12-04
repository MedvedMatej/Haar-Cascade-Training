import os

#we open the file neg.txt and write the names of all images in it
with open('neg1.txt','w') as f:
    for filename in os.listdir("NegS"):
        f.write('NegS/'+filename+ '\n')