''' Whitespace is a python kit module ''' 

__author__ = 'Lotus'
__verison__ = 0.1

# Error Output
def error_out(error_msg: str):
    print(f' * [ERROR] - {error_msg}')

def prior_error_out(error_msg: str):
    print(f' ** [ERROR] - {error_msg}')

def important_error_out(error_msg: str): 
    print(f' *** [ERROR] - {error_msg}')

try: 
    import pyfiglet
except ImportError as ImportErr: 
    print(f'Error while trying to import external lib in file: whitespace.py [{ImportErr}]')

def ascii_out(raw_string: str): 
    print(pyfiglet.figlet_format(raw_string, "standard"))
