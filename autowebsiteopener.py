import subprocess
import webbrowser

# Get the user's command
file_commands = input('Enter a command to open a software:')
websites_commands=input('Enter the website you want to open:')
# Map the command to the software path
software_paths = {
    'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    'notepad': 'C:\\Windows\\system32\\notepad.exe',
    'calculator': 'C:\\Windows\\system32\\calc.exe'
}
website_paths={
    'instagram':'https://www.instagram.com/',
    'suiit':'https://suiit.ac.in/'
}
if websites_commands in website_paths:
    webbrowser.open_new_tab(websites_commands);
else:
    print("This may not be a website");

# Check if the command is valid
if file_commands in software_paths:
    # Open the software using the subprocess module
    subprocess.Popen(software_paths[file_commands])
else:
    print('Invalid command')
