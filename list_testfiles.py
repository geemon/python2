#a pyhton script to loop through a list of files and count the number of files in each file

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
filename = ['text.txt', 'user_info.txt', 'python.txt', 'write_to_python.txt', 'bullet.txt']
for fname in filename:
    count_words(fname)

