from posixpath import split


def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file("pets.txt")
new_content = split(file_content)





