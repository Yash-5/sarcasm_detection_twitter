import csv

"""
Given the filename of Affective rating scores, it returns a dictionary of valence ratings of words
For each word there is a tuple of size 2, valence ratings of old people using the word and young people using the word respectively

The data is available at http://crr.ugent.be/archives/1003
"""
def build_valence(filename="./Ratings_Warriner_et_al.csv"):
    valence_file_iter = csv.reader(open(filename, "r"), delimiter=",")
    valence_file = [x for x in valence_file_iter]
    # We want V.Mean.Y and V.Mean.O which are at indices 29 and 32, the word is at index 1
    # Remove the header
    valence_file = valence_file[1:]
    valence_rating = {}
    for entry in valence_file:
        valence_rating[entry[1]] = (float(entry[29]), float(entry[32]))
    return valence_rating
