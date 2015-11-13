import os
import pickle
os.chdir('F:/')
new_man = []
try:
    with open('man_data.txt', 'rb') as man_file,open('other_data.txt', 'rb') as other_file:  # eliminates the use of finally block
        new_man = pickle.load(man_file)
        for man in new_man:
            print(man)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
