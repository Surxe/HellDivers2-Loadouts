# Write a file
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    
content = 'hi world'
write_file('test.txt', content)