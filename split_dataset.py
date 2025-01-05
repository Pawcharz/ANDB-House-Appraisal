import pandas as pd
from sklearn.model_selection import train_test_split

dataset_path = './dataset.csv'
dataset = pd.read_csv(dataset_path)

TEST_PERC = 0.2
VAL_PERC = 0.1

#split the data into train and test set
train, test = train_test_split(dataset, test_size=TEST_PERC, random_state=0)
test, val = train_test_split(test, test_size=VAL_PERC / (VAL_PERC + TEST_PERC), random_state=0)

#save the data
train.to_csv('dataset_train.csv',index=False)
val.to_csv('dataset_val.csv',index=False)
test.to_csv('dataset_test.csv',index=False)

print("Dataset Split Successfully")