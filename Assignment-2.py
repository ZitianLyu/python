import os 
import shutil 

str_bytes = '010101'.encode() 
with open('hello.bin', 'wb') as file: 
    file.write(str_bytes) 
    file.flush() 

test_dir = os.getcwd() + r'\test' 
if ~os.path.exists(test_dir): 
    os.makedirs(test_dir) 
shutil.move('hello.bin', test_dir) 

file_path = test_dir + r'\hello.bin' 
with open(file_path, 'rb') as file: 
    print(file.read(len(str_bytes)))  
    
os.remove(file_path)