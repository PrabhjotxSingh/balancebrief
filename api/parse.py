import os 
path = "api/sources/"
os.chdir(path) 
  
def read_text_file(file_path): 
    text_file = open(file_path, "r")
    return text_file
  
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if file.endswith(".txt"): 
        file_path = f"{file}"

        # call read text file function
        text_file = read_text_file(file_path)
        ret = []
        for x in range(3):
            temp = text_file.readline().replace("\n", '')
            ret.append(temp)
        text_file.readline()
        print(ret)
        text =  text_file.read().rstrip()


