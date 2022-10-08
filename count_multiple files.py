#a script to count number of words in multiple text files
 

from encodings.utf_8 import encode

#create a funtion
def count_words (filename):
    try:
        with open(filename, encoding= 'utf-8') as file: 
            content = file.read()         
    except FileNotFoundError:
        print(f'the file by name {filename} does not exit')

    else:    
     #split content of file 
        split_content = content.split()
        #count the number of words contained in file
        count_words = len(split_content)
        print(f'the number of words contained in the {filename} file is {count_words}')
filename = 'text.txt'
file1 = 'user_info.txt'
file2 = 'python.txt'
count_words(filename)
count_words(file2)
count_words(file1)