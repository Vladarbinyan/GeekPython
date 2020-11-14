import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

current_dir = '.'
files = os.listdir(current_dir)

print(os.path.dirname('c:/windows/notepad.exe'))
print(os.path.split('c:/windows/notepad.exe'))
print(os.path.join(r'\etc\init', r'hop\mmm', 'bbb', '123.txt'))

# for x in files:
#     print(os.path.dirname(x))
# print(os.path.dirname(f'./{x}'))

# print(files)
