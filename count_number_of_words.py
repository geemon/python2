#a program to count the number of words in text file
file_name = 'text.txt5'
try:
    with open (file_name) as file:
        rd_content = file.read()
        #to spilt the words in the text file
        split_rd = rd_content.split()
        #to fine the number of words in the file
        num_of_words = len(split_rd)
    print(f'The number of words contained in {file_name} file is {num_of_words} words')    

except FileNotFoundError:
    print(f'the file {file_name} does not exit')

