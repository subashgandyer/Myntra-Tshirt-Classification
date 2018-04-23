import os
import pandas as pd

#data = pd.read_csv("sample.csv")

directory = os.getcwd()
print(directory)

directory = os.getcwd() + '/full_resized_train_onefolder'

imagesList = []
cnt = 0
for file_name in os.listdir(directory):
	if cnt < 67087:
		imagesList.append(file_name)
	cnt += 1

print(imagesList)
imagesList = imagesList[1:]
print(imagesList)

f = open("New_labels.csv", "w")
f.write("id" + "," + "class" + "\n")

for image in imagesList:
	class_name = image.split('_')[1]
	class_name = class_name.replace(" ", "_")
	print(image + "," + class_name)
	f.write(image + "," + class_name + "\n")

f.close()

