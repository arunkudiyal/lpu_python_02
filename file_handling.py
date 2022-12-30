# Wanted to access the file (demo.txt) and read the content
# open(file_path, mode_of_operation)
fileRef = open('./demo.txt', 'r')
print( fileRef.read() )