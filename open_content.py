import csv
import pprint
import os

#function to read tsv file and convert it to a dictionary
def csv_to_dict(filename):

    #Relative pathing the file
    dirname = os.path.dirname(__file__)
    media_path = dirname + filename
    csv_object = csv.DictReader(open(media_path, 'r'), delimiter=',')

    dict_list = []

    for line in csv_object:
        dict_list.append(line)

    return dict_list

#pprint.pprint(csv_to_dict(r'/data.csv'))