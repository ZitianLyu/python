import shutil
import os 

path = './test.txt' 
with open(path, 'w+', encoding='utf-8', buffering=20) as f:
    f.write('helloworld') 
    f.write('helloworld') 
    
with open(path, 'w+', encoding='utf-8', buffering=1) as f: 
    f.write('helloworld \n') 
    f.write('helloworld \n') 
    f.write('helloworld \n') 
    
with open(path, 'wb+', buffering=0) as f: 
    f.write(b'helloworld') 
    f.write(b'helloworld') 

    f.close() 
    f1 = './test.txt' 
    f2 = './test/2' 
    shutil.move(f1, f2) 
    os.remove('./test/2/test.txt')