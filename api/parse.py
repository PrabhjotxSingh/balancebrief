import os
import cohere
import numpy as np

from cohere.responses.classify import Example

client = cohere.Client('lqJD3VjaVUpo4tgxxzg2RFIuu6p3jXmmezQc0tXD')

os.chdir("api/sources/") 
  
def read_text_file(file_path): 
    text_file = open(file_path, "r")
    return text_file
meta_data = []
text = []
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".txt"): 
        file_path = f"{file}"

        # call read text file function
        text_file = read_text_file(file_path)
        temp = []
        for x in range(4):
            temp += [text_file.readline().replace("\n", '')]
        meta_data.append(temp)
        text_file.readline()
        text +=  [text_file.read().rstrip().replace("\n", ' ')]
#Encode your documents with input type 'search_document'



