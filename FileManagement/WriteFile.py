import os
print(os.getcwd())
os.chdir('F:/')
print(os.getcwd())
try:
    data = open('test.txt', "r")
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = each_line.strip()
            if role == 'Man':
                print(line_spoken, file=man_file)
            elif role == 'Other Man':
                print(line_spoken, file=other_file)
except IOError as err:
    print("data file missing", str(err))
finally:
    if 'data' in locals() :
        data.close()
    if 'man_file' in locals() :
        man_file.close()
    if 'other_file' in locals() :
        other_file.close()
