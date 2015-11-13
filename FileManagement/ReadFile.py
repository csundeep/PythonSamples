import os
print(os.getcwd())
os.chdir('F:/')
print(os.getcwd())
try:
    data = open('test.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
except IOError:
    print("data file missing")
finally:
    data.close()
