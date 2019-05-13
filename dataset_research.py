# dataset_research.py
#
# Custom library containing list of classes, functions and global variables for use
#
# Author: Ranjeeta Bhattacharya


# Global variables in the dataset research module

song_descriptlist_details = []
artist_descriptlist_details = []


# The following class lists details about the artist. This serves as the base class. 

class Artist_Details(object):    

# Constructor method to initialize attributes relevant to artist

    def __init__(self,artist_familiarity,artist_hotness,artist_id,artist_latitude,
                    artist_location,artist_longitude,artist_name):
    
        self.artist_familiarity = artist_familiarity 
        self.artist_hotness = artist_hotness
        self.artist_id = artist_id 
        self.artist_latitude =  artist_latitude
        self.artist_location = artist_location
        self.artist_longitude = artist_longitude
        self.artist_name = artist_name
    
# Function body describing the entire artist dataset

    def artist_dataset_description(self):
        
        self.artist_familiarity = "Artist_Familiarity: Description of the familiarity of the artist. 0(Min) - 1(Max)" 
        self.artist_hotness = "Artist_Hotness: Hotness factor of the artist. Algorithmic estimation."
        self.artist_id = "Artist_ID: Unique identifier (Echo Nest ID)"
        self.artist_latitude = "Artist_Latitude: Latitude Details"
        self.artist_location = "Artist_Location: Location details of the artist"
        self.artist_longitude = "Artist_Longitude: Longitude details of the artist"
        self.artist_name = "Artist_Name: Name of the artist"
        
        artist_descriptlist_details.append(self.artist_familiarity)
        artist_descriptlist_details.append(self.artist_hotness)
        artist_descriptlist_details.append(self.artist_id)
        artist_descriptlist_details.append(self.artist_id)
        artist_descriptlist_details.append(self.artist_latitude)
        artist_descriptlist_details.append(self.artist_location)
        artist_descriptlist_details.append(self.artist_longitude)
        artist_descriptlist_details.append(self.artist_name)
        
        return artist_descriptlist_details
        
# The following class lists details about the song. This class inherits base class Artist.

class Song_Features(Artist_Details):
     
    def __init__(self,artist_familiarity,artist_hotness,artist_id,artist_latitude,
                 artist_location,artist_longitude,artist_name,duration,end_of_fade_in,key,
                 key_confidence,loudness,mode,mode_confidence,release,song_hotness,start_of_fade_out,
                 tempo,time_signature,time_signature_confidence,title,year):
        
        Artist_Details.__init__(self,artist_familiarity,artist_hotness,artist_id,artist_latitude,
                        artist_location,artist_longitude,artist_name)

        self.duration = duration
        self.end_of_fade_in = end_of_fade_in 
        self.key = key 
        self.key_confidence = key_confidence 
        self.loudness = loudness 
        self.mode = mode
        self.mode_confidence = mode_confidence
        self.release = release
        self.song_hotness = song_hotness 
        self.start_of_fade_out = start_of_fade_out 
        self.tempo = tempo 
        self.time_signature = time_signature 
        self.time_signature_confidence = time_signature_confidence
        self.title = title 
        self.year = year
    
# Function body describing all features of the song

    def feature_dataset_description(self):
        
        self.duration = "Duration: Duration of the song" 
        self.end_of_fade_in = "End_Of_Fade_In: Seconds at the beginning of the song"
        self.key = "Key: Key the song is in"
        self.key_confidence = "Key_Confidence: Confidence Measure"
        self.loudness = "Loudness: Overall loudness of the song is Decibel(dB)"
        self.mode = "Mode: Major or Minor mode (estimated by Echo Nest)"
        self.mode_confidence = "Mode_Confidence: Confidence Measure"
        self.release = "Release: Name of the Album"
        self.song_hotness = "Song_Hotness: Hotness factor of the song(algorithmic estimation)"
        self.start_of_fade_out = "Start_Of_Fade_Out: Fade out time of the song in seconds"
        self.tempo = "Tempo: Beats per minute"
        self.time_signature = "Time_Signature: Estimate number of beats per bar"
        self.time_signature_confidence = "Time_Signature_Confidence: Confidence Measure"
        self.title = "Title: Title of the song"
        self.year = "Year: Year of release"
        
        
        song_descriptlist_details.append(self.duration)
        song_descriptlist_details.append(self.end_of_fade_in)
        song_descriptlist_details.append(self.key)
        song_descriptlist_details.append(self.key_confidence)
        song_descriptlist_details.append(self.loudness)
        song_descriptlist_details.append(self.mode)
        song_descriptlist_details.append(self.mode_confidence)
        song_descriptlist_details.append(self.release)
        song_descriptlist_details.append(self.song_hotness)
        song_descriptlist_details.append(self.start_of_fade_out)
        song_descriptlist_details.append(self.tempo)
        song_descriptlist_details.append(self.time_signature)
        song_descriptlist_details.append(self.time_signature_confidence)
        song_descriptlist_details.append(self.title)
        song_descriptlist_details.append(self.year)
        
        return song_descriptlist_details
    
