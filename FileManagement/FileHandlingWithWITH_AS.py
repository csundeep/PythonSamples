import os
print(os.getcwd())
os.chdir('F:/')
print(os.getcwd())
try:
    with open('test.txt', "r") as data,open('man_data.txt', 'w') as man_file,open('other_data.txt', 'w') as other_file:  # eliminates the use of finally block
        for each_line in data:
            if not each_line.find(':') == -1:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = each_line.strip()
                if role == 'Man':
                    print(line_spoken, file=man_file)
                elif role == 'Other Man':
                    print(line_spoken, file=other_file)
                print(line_spoken)
except IOError as err:
    print("data file missing", str(err))
