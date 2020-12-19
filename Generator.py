''' HTML Generator ''' 

''' Change Log: 

* 0.5 (First-Release) 
    -- Beta Release -- 
    -- Base Core    -- 
    - added out statement   | Sets HTML Doc Default Paragraph
    - added lang statement  | Sets HTML Doc Language
    - added char statement  | Sets HTML Doc Charset
    - added title statement | Sets HTML Doc Title
    - added cls statement   | Clears CMDL # Optional Alternative
    - added clear statement | Clears CMDL # Alternative
    - added say statement   | Commandline Output

* 0.6 
    -- Minor Bug Fix -- 
    - fixed background color bug
    
    -- Base Core Addition -- 
    - added help statement  | Displays help screen 
'''

__author__ = 'Lotus'
__version__ = 0.6

import whitespace # Base Module - Excluded from Import-Check @ L6


try: # Import-Checking 
    import os
    import datetime
except ImportError as ImportErr: 
    whitespace.important_error_out(ImportErr)


# Basis HTML Attributes
lang: str = ''
charset: str = ''
title: str = ''
bg_color: str = 'white' # white == default
default_statement: str = ''

# Global Configurations
default_statement_config: bool = False

class Alpha: 
    # Commandline Editing
    def cmd_help(self): # displays help screen 
        print('''Commands: 
    title [title_str]
        changes the title in the HTML Doc

    char [charset]
        changes the charset in the HTML Doc

    lang [language]
        changes the language in the HTML Doc

    out [paragraph]
        adds a default paragraph to the body part in the HTML Doc

    bg [background-color]
        adds a default background color to the body part in the HTML Doc

    say [output-text]
        outputs text in the commandline interface

    cls
        clears console screen - Optional alt. to "clear"

    clear
        cleans console screen - alternative to "cls"''')              

    def cmd_clear(self): # Optional Alt. to cls
        os.system('cls')

    def cmd_cls(self): # Alternative to clear
        os.system('cls')

    def cmd_say(self, message: str): # Output
        print(f'... {message.replace("_", " ")}')

    # HTML Editing
    def cmd_lang(self, value: str): # Set Language
        global lang
        lang = value
        print(f'Language set to: {lang}') # Method Response
    
    def cmd_char(self, value: str): # Set Charset
        global charset
        charset = value
        print(f'Charset set to: {charset}') # Method Response

    def cmd_title(self, value: str): # Set Title
        global title
        title = value.replace('_', ' ')
        print(f'Title set to: {title}') # Method Response

    def cmd_bg(self, value: str): # Set Background Color
        global bg_color
        bg_color = value.lower()
        print(f'Background Color set to: {bg_color}') # Method Response

    def cmd_out(self, value: str): # Set Default Statement
        global default_statement
        global default_statement_config
        default_statement_config = True
        default_statement = value.replace('_', ' ')
        print(f'Default Paragraph set to: {default_statement}')


A = Alpha()

class CMDL: # Commandline
    def __init__(self, A): 
        self.A = A # Alpha Instance

    def getl(self): # Main Commandline Method
        while 1: # Main Input Loop
            command = input('<cmd> ').split()
            try:
                if command[0] in ['save', 'close', 'exit', 'quit']:  
                    break
                base_cmd = command[0].lower()
                arg = command[1]
                getattr(self.A, f'cmd_{base_cmd}')(arg)
            except AttributeError:
                whitespace.error_out('Command Not Found')
            except IndexError:
                try: 
                    base_cmd = command[0]
                    getattr(self.A, f'cmd_{base_cmd}')()
                except AttributeError:
                    whitespace.error_out('Command Not Found')
                except TypeError: 
                    pass
                except IndexError: 
                    pass


CMDL = CMDL(A) # Commandline Initialization
CMDL.getl()    # Method Initialization

if default_statement_config: # Paragraph Default Checking
    public_str = f'''
<!DOCTYPE html>
<html lang="{lang}">

<head>
  <meta charset="{charset}">
  <title>{title}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="css/style.css" rel="stylesheet">
</head>

<body style="background-color:{bg_color}">

    <p>{default_statement}</p>
</body>

</html>
'''
else: 
    public_str = f'''
<!DOCTYPE html>
<html lang="{lang}">

<head>
  <meta charset="{charset}">
  <title>{title}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="css/style.css" rel="stylesheet">
</head>

<body style="background-color:{bg_color}">

</body>

</html>
'''

os.system('cls') # last console wipe
save_to_file = input('<save-to-file> ') # file that the generated HTML Code gets saved to

if save_to_file == '':
    save_to_file = 'HTML_DOC.html'

if save_to_file.lower() != 'force exit': 
    try:    # exit save, force save
        with open(save_to_file, 'w') as file:
            file.write(public_str)
    except FileNotFoundError as FNF:
        whitespace.error_out(FNF)
