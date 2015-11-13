import os
print(os.getcwd())
os.chdir('F:/')
print(os.getcwd())
try:
    data = open('test.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass
except IOError as err:
    print("data file missing",str(err))
finally:
    if 'data' in locals() :
        data.close()
