import pandas as pd
import matplotlib.pyplot as plt

myntra = pd.read_csv("myntra_train_dataset.csv")

print(myntra.head())



myntra_im_class = myntra[["Link_to_the_image","Sub_category"]]

print(myntra_im_class.head())

print(myntra['Sub_category'].value_counts())

print(myntra.describe())