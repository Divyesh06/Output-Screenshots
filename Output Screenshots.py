import urllib
import requests
import os

splitter = "#Take Screenshot"

print("""
    This Script will automatically take screenshots of your Code Outputs

    You can also divide your File into multiple parts and take Screenshots of Individual Parts by adding the Comment (#Take Screenshot) to indicate new separation

    For more help on this, check out README.md at https://github.com/Divyesh06/Output-Screenshots

"""
)

python_file = input('Enter the location of your Python File: ')

_input = input
_print = print
output_string = ""


def url_encode(string):
    a = urllib.parse.quote(string)
    a = a.replace("%0A", "%250A")
    return a


def input(prompt):
    value = _input(prompt)
    full_prompt = prompt+value
    global output_string
    output_string += full_prompt+'\n'
    return value


def print(*args, sep=" ", end="\n"):
    global output_string
    args = (str(arg) for arg in args)
    statement = str(sep).join(args)+str(end)
    output_string += statement
    _print(statement)


with open(python_file) as f:
    content = f.read()
_print(f"""
=====================================
\nRunning {python_file} Now\n
=====================================
""")
code_blocks = content.split(splitter)
for index, i in enumerate(code_blocks):
    exec(i, globals(), locals())
    output_string = output_string.strip()
    result = requests.get(
        f'https://carbonnowsh.herokuapp.com/?code={url_encode(output_string)}&windowTheme=boxy&paddingHorizontal=0px&paddingVertical=0px&backgroundColor={url_encode("#151718")}&exportSize=4x&windowControls=false')
    file_name = f'Screenshot{index+1}.png'
    with open(file_name, 'wb') as f:
        f.write(result.content)
    output_string = ""
    _print(f"Screenshot saved at ", os.path.join(os.getcwd(), file_name))
_print(f"""

    Completed Running {python_file}

    If this script helped you save some time, don't forget to Star it on Github

""")
