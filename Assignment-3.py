import os 
import shutil 

path = os.getcwd()

file = open(path + '\log.log','w') 
file.close()

test_dir = os.getcwd() + r'\test' 
if ~os.path.exists(test_dir): 
    os.makedirs(test_dir) 
shutil.move('log.log', test_dir) 

with open(test_dir + '\log.log','a') as f:
    f.write('log File.') 
    f.close() 

file_path = test_dir + r'\log.log' 
with open(file_path, 'rb') as file: 
    print(file.readline()) 

os.remove(test_dir + '\log.log')