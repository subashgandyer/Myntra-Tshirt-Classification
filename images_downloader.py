import urllib.request
import csv
from time import sleep

#IMAGE_COLUMN = 14
#ROOT_URL = 'http://www.fakesite.com/pimages/'

#####  Dictionary version #######
# with open('myntra_train_first_10k.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=",")
#     images_dict = { row[4] : row[5] if row[4] != '' else 'NOLINK' for row in readCSV }

# #print(images_dict, type(images_dict))

# count = 1
# for key,val in images_dict.items():
# 	if key != '':
# 		print("Image # " + str(count) + " downloading from " + key + "    Stored as " + val+'-'+str(count)+'.jpg')
# 		url = key
# 		urllib.request.urlretrieve(url, val+'-'+str(count)+'.jpg')
# 		count += 1





#### LIST version ######
images_list = []
with open('myntra_train_first_10k.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    images_list = [ (row[4], row[5]) for row in readCSV ]

print(images_list, type(images_list))

count = 0
for key,val in images_list:
	#print(key,val)
	count += 1
	if key != '':
		url = key
		urllib.request.urlretrieve(url, val+'-'+str(count)+'.jpg')
		if (count % 5) == 0:
			print("Image # " + str(count) + " downloading from " + key + "    Stored as " + val+'-'+str(count)+'.jpg')
		if (count % 25) == 0:
			sleep(5)
		
