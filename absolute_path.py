#script to read from a file using absolute path
my_file_path = 'C:\\Users\\#G.E.E\\Documents\\nan\\text.txt'
with open(my_file_path) as file_object:
    rd_me = file_object.read()
print(rd_me)