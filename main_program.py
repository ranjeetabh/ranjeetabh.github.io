# main_program.py
#
# The main module for processing and analysing musical dataset
#
# Author: Ranjeeta Bhattacharya


# To suppress future warnings on console

import warnings

# Importing standard Libraries as required

import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import deque

# Setting stylemap for visualization plots

sns.set()

# Importing user defined/custom libraries

import dataset_research

# If executing the program in Jupyter notebook (Anaconda distribution), please unhash the next line

# %matplotlib inline

# Data structure queue implementation
# Declaring deque object to store sequential steps of execution of the program

queue = deque()

print("Main Program Execution Begins")
print("-----------------------------")
    
# Specifying names of input and output file handles for processing.

iFile = "MusicDataset_input.csv"

oFile = "MusicDataset_output.csv"

# Inserting the logical step completion details in queue

queue.append("1.Creating input and output file handles for processing")


# Opening the inputfile dataset, cleaning the records and writing to an output file

with open(iFile,"r",encoding="utf8") as infile, open(oFile,"w",errors="ignore") as outfile:

    print("Opening input and output files for processing")
    print("\n")
    
    r = csv.DictReader(infile)

    w = csv.DictWriter(outfile, delimiter=',', lineterminator='\n', fieldnames=r.fieldnames)
    
    w.writeheader()      # Writing the header to output file
    
    for row in r:                             

# Replacing the null values in each attribute with some default value as applicable

        if not row["artist_familiarity"].strip():
            row["artist_familiarity"] = 0
        
        if not row["artist_hotness"].strip():
            row["artist_hotness"] = 0
        
        if not row["artist_id"].strip():
            row["artist_id"] = "DMD"
        
        if not row["artist_latitude"].strip():
            row["artist_latitude"] = 0
        
        if not row["artist_location"].strip():
            row["artist_location"] = "Not Available"
        
        if not row["artist_longitude"].strip():
            row["artist_longitude"] = 0
        
        if not row["artist_name"].strip():
            row["artist_name"] = "Not Available"
        
        if not row["duration"].strip():
            row["duration"] = 0
        
        if not row["end_of_fade_in"].strip():
            row["end_of_fade_in"] = 0
        
        if not row["key"].strip():
            row["key"] = 0
        
        if not row["key_confidence"].strip():
            row["key_confidence"] = 0.0
        
        if not row["loudness"].strip():
            row["loudness"] = "-1"
        
        if not row["mode"].strip():
            row["mode"] = 0
        
        if not row["mode_confidence"].strip():
            row["mode_confidence"] = 0
        
        if not row["release"].strip():
            row["release"] = "Not Available"
        
        if not row["song_hotness"].strip():
            row["song_hotness"] = 0.0
        
        if not row["start_of_fade_out"].strip():
            row["start_of_fade_out"] = 0
        
        if not row["tempo"].strip():
            row["tempo"] = 0
        
        if not row["time_signature"].strip():
            row["time_signature"] = 0
        
        if not row["time_signature_confidence"].strip():
            row["time_signature_confidence"] = 0
        
        if not row["title"].strip():
            row["title"] = "Not Available"
        
        if not row["year"].strip():
            row["year"] = 0


# Writing cleaned data to output file       

        w.writerow(row)
        
        line_count = r.line_num
        
    print("Cleaned input data written to output file")
    print("\n")
    print("Input file has:",(line_count - 1),"records")

# Inserting the logical step completion details in queue

queue.append("2.Cleaned input file data and created output file for processing\n")

# Closing the input and outfile file handles post processing

infile.close()
outfile.close()


# Re-Opening the newly generated cleaned file for further investigation

with open ("MusicDataset_output.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0      # Initializing counter to read file


    for row in csv_reader:
        if line_count == 0:      # Exclude the header
            
            line_count += 1
        else:                    # Creating and initializing object of Song_Features class with requisite attributes
            
            song_features = dataset_research.Song_Features(row[0],row[1],row[2],row[3],row[4],row[5],
                                                           row[6],row[7],row[8],row[9],row[10],row[11],
                                                           row[12],row[13],row[14],row[15],row[16],row[17],
                                                           row[18],row[19],row[20],row[21]) 


# Invoking method to display detailed list of attributes associated with an artist 

desc_artist = song_features.artist_dataset_description()
print("\n")
print("| ARTIST DETAILS |")
print("| -------------- |")

# Iterating through the list and displaying the same on screen

for item in desc_artist:
    print(item,"\n")


# Invoking method to display detailed list of attributes associated with a song

desc_song = song_features.feature_dataset_description()
print("\n")
print("| SONG FEATURE DETAILS |")
print("| -------------------- |")

for item in desc_song:
    print(item,"\n")


# Closing the file handle post processing

csv_file.close()


# Reading the contents of input file in Pandas dataframe for data exploration and visualization

print("Reading input file in pandas dataframe")
print("--------------------------------------")

df = pd.read_csv("MusicDataset_output.csv",encoding="ISO-8859-1")

# Displaying information regarding the input file after reading in a dataframe

print("Displaying dataset information using pandas dataframe")
print("-----------------------------------------------------")
df.info()
print("\n")


# Exploratory Data analysis section

# Using Pandas dataframe methods to generate some descriptive statistics of the dataset

print("Descriptive Statistics of dataset")
print("---------------------------------\n")
print("Field :: artist_familiarity ")
print("Count ::",df['artist_familiarity'].count())
print("Mean  ::",df['artist_familiarity'].mean())
print("Std   ::",df['artist_familiarity'].std())
print("Min   ::",df['artist_familiarity'].min())
print("Max   ::",df['artist_familiarity'].max())
print("\n")


print("Field :: artist_hotness ")
print("Count ::",df['artist_hotness'].count())
print("Mean  ::",df['artist_hotness'].mean())
print("Std   ::",df['artist_hotness'].std())
print("Min   ::",df['artist_hotness'].min())
print("Max   ::",df['artist_hotness'].max())
print("\n")


print("Field :: duration ")
print("Count ::",df['duration'].count())
print("Mean  ::",df['duration'].mean())
print("Std   ::",df['duration'].std())
print("Min   ::",df['duration'].min())
print("Max   ::",df['duration'].max())
print("\n")


print("Field :: loudness ")
print("Count ::",df['loudness'].count())
print("Mean  ::",df['loudness'].mean())
print("Std   ::",df['loudness'].std())
print("Min   ::",df['loudness'].min())
print("Max   ::",df['loudness'].max())
print("\n")


print("Field :: tempo ")
print("Count ::",df['tempo'].count())
print("Mean  ::",df['tempo'].mean())
print("Std   ::",df['tempo'].std())
print("Min   ::",df['tempo'].min())
print("Max   ::",df['tempo'].max())
print("\n")


# Inserting the logical step completion details in queue

queue.append("3.Generated descriptive statistics about dataset")

# Finding correlation between some features of the dataset

print("Correlations between internal features")
print("--------------------------------------")
print("\n")
print(df[['artist_familiarity','song_hotness']].corr())
print("\n")
print(df[['artist_longitude','song_hotness']].corr())
print("\n")
print(df[['loudness','song_hotness']].corr())
print("\n")
print(df[['artist_hotness','song_hotness']].corr())
print("\n")
print(df[['artist_familiarity','artist_hotness']].corr())
print("\n")


# Correlation coefficients analysis

print("Positive correlation exhibited between pairs 'artist_familiarity,song_hotness', 'loudness,song_hotness', 'artist_hotness,song_hotness', 'artist_familiarity,artist_hotness'")
print("\n")
print("Negative correlation exhibited between pairs 'artist_longitude,song_hotness'")
print("\n")

# Inserting the logical step completion details in queue

queue.append("4.Exploratory Data Analysis completed")

# Plotting and visualization section

print("Beginning plotting and visualization section")
print("--------------------------------------------")

df[['artist_familiarity','artist_hotness','song_hotness']].plot.hist()


df.plot.scatter(x='artist_familiarity',y='artist_hotness',color='red',s=50,figsize=(12,3))


sns.jointplot(x='artist_hotness',y='loudness',color='green',data=df,kind='reg')


# Inserting the logical step completion details in queue

queue.append("5.Plotting and visualization done")

# Printing the contents of deque

print("\n")
print("Major logical execution steps of the program in sequential order. Printing contents of FIFO queue")
print("--------------------------------------------------------------------------------------------------")
print("\n")
print(queue)
print("\n")

# Displaying the graphs on screen

warnings.simplefilter(action='ignore', category=FutureWarning)   
warnings.filterwarnings("ignore")


print("Displaying generated graphs on screen")
plt.show()












