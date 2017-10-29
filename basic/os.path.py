$ pwd
/Users/jangsanghoon/Desktop/python_code

$ python dr.py
__file__  # ./dr.py
os.path.dirname(__file__)  # .
os.path.realpath(__file__) # /Users/jangsanghoon/Desktop/python_code/dr.py
os.path.realpath( os.path.dirname(__file__) ) # /Users/jangsanghoon/Desktop/python_code

os.getcwd() # /Users/jangsanghoon/Desktop/python_code

os.path.basename( os.path.realpath(__file__) ) # dr.py
