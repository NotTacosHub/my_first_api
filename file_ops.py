from genericpath import exists
import os

def get_storage_dir():
    return R"C:\Users\smith\Bottega\hw10_1\storage"

def get_storage_file(file_name):
    return os.path.join(get_storage_dir(), file_name)

def file_exists(file_name):
    return exists(get_storage_file(file_name))

#create
def create_file(file_name):
    if not file_exists(file_name):
        return open(get_storage_file(file_name), "x")
    else:
        raise Exception("file already exists {}".format(file_name))

#read
def read_file(file_name):
    if file_exists(file_name):
       file=open(get_storage_file(file_name), "r")
       content = file.read()
       file.close()
       return content
    else:
        raise Exception("cannot read file, doesn't exist {}".format(file_name))

#update
def update_file(file_name, content):
    if file_exists(file_name):
        file=open(get_storage_file(file_name), "a")
        file.write(content)
        file.close()
    else:
        raise Exception("cannot update file, doesn't exist {}".format(file_name))

#delete
def delete_file(file_name):
    if file_exists(file_name):
        os.remove(get_storage_file(file_name))
    else:
        raise Exception("cannot delete file, doesn't exist {}".format(file_name))
