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

* 0.7
    -- Core Changes -- 
    - New Mode System released
    - ^- Mode System contains CSS & HTML mode
    - added switch statement | switches modes (HTML/CSS)
    - added corresponding mode command storage -> AlphaCLS (HTML) - BetaCLS (CSS)

'''

__author__ = 'Lotus'
__version__ = 0.7

import whitespace # Base Module - Excluded from Import-Check @ L6


try: # Import-Checking 
    import os
except ImportError as ImportErr: 
    whitespace.important_error_out(ImportErr)


# Multi Layer Storage
website_object_storage = []


class AlphaCLS: # Also for HTML Support
    def __init__(self):
        # Basis Commandline Editing Variables
        self.commandline_mode: str = 'html' 
        self.commandline_switch_count: int = 0
        
        # Basis HTML Attributes
        self.lang: str = ''
        self.charset: str = ''
        self.title: str = ''
        self.bg_color: str = 'white' # white == default
        self.default_statement: str = ''

        # Doc Configurations
        self.default_statement_config: bool = False
    
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

    def _force_exit(self): 
        self.commandline_mode = 'EXIT' 

    def cmd_switch(self):
        self.commandline_switch_count += 1
        if self.commandline_switch_count % 2 == 0: 
            self.commandline_mode = 'html'
        else: 
            self.commandline_mode = 'css'

    def cmd_clear(self): # Optional Alt. to cls
        os.system('cls')

    def cmd_cls(self): # Alternative to clear
        os.system('cls')

    def cmd_say(self, message: str): # Output
        print(f'... {message.replace("_", " ")}')

    # HTML Editing
    def cmd_lang(self, value: str): # Set Language
        self.lang = value
        print(f'Language set to: {self.lang}') # Method Response
    
    def cmd_char(self, value: str): # Set Charset
        self.charset = value
        print(f'Charset set to: {self.charset}') # Method Response

    def cmd_title(self, value: str): # Set Title
        self.title = value.replace('_', ' ')
        print(f'Title set to: {self.title}') # Method Response

    def cmd_bg(self, value: str): # Set Background Color
        self.bg_color = value.lower()
        print(f'Background Color set to: {self.bg_color}') # Method Response

    def cmd_out(self, value: str): # Set Default Statement
        self.default_statement_config = True
        self.default_statement = value.replace('_', ' ')
        print(f'Default Paragraph set to: {self.default_statement}')


A = AlphaCLS() # HTML Editing Instance Initialization

class BetaCLS: # CSS Entry Point
    def __init__(self, A): 
        self.A = A

    def cmd_switch(self):
        return self.A.cmd_switch()

    def cmd_help(self):
        print('CMD METHOD')
    
    def _force_exit(self): 
        self.A.commandline_mode = 'EXIT'


B = BetaCLS(A=A) # CSS Editing Instance Initialization

def commandline(mode: str, DockerCLS: object):
    while A.commandline_mode == mode:
        command = input(f'<{mode}> ').split()
        try: 
            if command[0].lower() in ['save', 'close', 'exit', 'quit']: 
                return DockerCLS._force_exit()
        except IndexError:
            pass
        try:
        
            base = command[0].lower()
            argument= command[1]
            getattr(DockerCLS, f'cmd_{base}')(argument)
        except AttributeError as attrerr: 
            whitespace.error_out(attrerr)
        except IndexError:
            try: 
                base_cmd = command[0]
                getattr(DockerCLS, f'cmd_{base_cmd}')()
            except AttributeError as attrerr:
                whitespace.error_out(attrerr)
            except TypeError:
                pass
            except IndexError: 
                pass


# HTML Commandline == Commandline Entry Point
class HTMLCMDL: # HTML Commandline and Commandset
    def __init__(self, A: object): 
        self.A = A # Alpha Instance

    def getl(self): 
        commandline(mode='html', DockerCLS=A)


class CSSCMDL: # CSS Commandline and Commandset
    def __init__(self, A: object, html: object): 
        self.A = A # Alpha Instance
        self.html = html

    def getl(self): 
        commandline(mode='css', DockerCLS=B)


html_commandline = HTMLCMDL(A)
css_commandline = CSSCMDL(A, html_commandline)

while 1:
    if A.commandline_mode == 'html': 
        getattr(html_commandline, 'getl')()
    elif A.commandline_mode == 'css':
        getattr(css_commandline, 'getl')()
    else:
        break


if A.default_statement_config: # Paragraph Default Checking
    public_str = f'''
<!DOCTYPE html>
<html lang="{A.lang}">

<head>
  <meta charset="{A.charset}">
  <title>{A.title}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="css/style.css" rel="stylesheet">
</head>

<body style="background-color:{A.bg_color}">

    <p>{A.default_statement}</p>
</body>

</html>
'''
else: 
    public_str = f'''
<!DOCTYPE html>
<html lang="{A.lang}">

<head>
  <meta charset="{A.charset}">
  <title>{A.title}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="css/style.css" rel="stylesheet">
</head>

<body style="background-color:{A.bg_color}">

</body>

</html>
'''

os.system('cls') # last console wipe
html_save_to_file = input('<save-to-file> ') # file that the generated HTML Code gets saved to

if save_to_file == '':
    save_to_file = 'HTML_DOC.html'
    css_save_to_file = 'HTML_DOC-STYLING.css'
else: 
    css_save_to_file = f'{html_save_to_file}-styling.css'

if save_to_file.lower() != 'force exit': 
    try:    # exit save, force save
        with open(save_to_file, 'w') as file:
            file.write(public_str)
    except FileNotFoundError as FNF:
        whitespace.error_out(FNF)
