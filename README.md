# Assignment 2 - Analysis of Twitter Data
## Mongodb setup (skip if data is allready in the Database)
1. Make a folder called data
1. Insert the `training.1600000.processed.noemoticon.csv` file into the data folder
1. Give the dataset a header line by running `sed -i '1s;^;polarity,id,date,query,user,text\n;' training.1600000.processed.noemoticon.csv`
1. Start up a docker mongodb with `bash ./MGDB`
1. Insert the data into the docker database by running `bash ./MGDB_insert_data`

## Run the program
1. `python3 main.py`