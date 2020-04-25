import subprocess

# Gets the clipboard content
def read_from_clipboard():
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

# Creates variable
clipContent = read_from_clipboard()

replacedContent = clipContent.replace(" ", "%20")

print(replacedContent)
