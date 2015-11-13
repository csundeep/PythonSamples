import os
import pickle
os.chdir('F:/')
try:
    with open('test.txt', "rb") as data,open('man_data.txt', 'wb') as man_file,open('other_data.txt', 'wb') as other_file:  # eliminates the use of finally block
        for each_line in data:
            if not each_line.decode("utf-8").find(':') == -1:
                (role, line_spoken) = each_line.decode("utf-8").split(':', 1)
                if role == 'Man':
                    pickle.dump(line_spoken, file=man_file)
                elif role == 'Other Man':
                    pickle.dump(line_spoken, file=other_file)
                print(role,' : ',line_spoken)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
