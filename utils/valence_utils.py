import csv

def build_valence(filename):
    valence_file_iter = csv.reader(open(filename, "r"), delimiter=",")
    valence_file = [x for x in valence_file_iter]
    # We want V.Mean.Y and V.Mean.O which are at indices 29 and 32, the word is at index 1
    # Remove the header
    valence_file = valence_file[1:]
    valence_rating = {}
    for entry in valence_file:
        valence_rating[entry[1]] = (float(entry[29]), float(entry[32]))
    return valence_rating