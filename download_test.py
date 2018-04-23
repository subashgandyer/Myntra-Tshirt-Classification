import os
from IPython.display import clear_output
import pandas as pd  # For manipulating CSV files
import urllib.request  # For downloading files from the provided links
import time
from termcolor import colored

test_dir='testing'
#train_dir='Train'

#traincsv = pd.read_csv('myntra_train_dataset.csv')
testcsv = pd.read_csv('Submission_online.csv')

# if not os.path.exists(train_dir):
#     os.mkdir(train_dir)
# start = time.time()
# for i in range(traincsv.shape[0]):
#     link = traincsv.iloc[i]['Link_to_the_image']
#     name = (traincsv.iloc[i]['Sub_category'])
#     full_name = name+'_'+str(i)+'.jpg'
#     img_name = full_name
#     full_name = os.path.join(train_dir, img_name)
#     if not os.path.exists(full_name):
#         try:
#             clear_output(wait=True)
#             urllib.request.urlretrieve(link, full_name)
#             print(colored(img_name+' downloaded', 'green'))
#         except:
#             clear_output(wait=True)
#             print(colored('Link Missing', color='red'))
#     else:
#         clear_output(wait=True)
#         print(img_name,' has already been downloaded')
# end = time.time()
# print('Time taken: ', end-start)



""" Downloading the Testing data """

if not os.path.exists(test_dir):
    os.mkdir(test_dir)
start = time.time()
miss_link = "http://www.leanhealthcareexchange.com/wp-content/uploads/2014/02/LeanHealthcare_Sustainability-300x142.jpg"
miss_name = "missing.jpg"
for i in range(0, testcsv.shape[0]):
    link = testcsv.iloc[i]['Link_to_the_image']
    name = str(i)+'.jpg'
    miss_name = 'missing' + str(i) +'.jpg'
    full_name = os.path.join(test_dir, name)
    if not os.path.exists(full_name):
        try:
            clear_output(wait=True)
            urllib.request.urlretrieve(link, full_name)
            print(colored(name+' downloaded', 'green'))
        except:
            clear_output(wait=True)
            urllib.request.urlretrieve(miss_link, miss_name)
            print(colored('Link Missing', color='red'))
    else:
        clear_output(wait=True)
        print(name, ' has already been downloaded')
end = time.time()
print('Time taken: ', end-start)