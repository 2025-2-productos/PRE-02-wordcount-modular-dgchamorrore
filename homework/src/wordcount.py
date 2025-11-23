import os

files_in_input_dir=os.listdir('data/input/')
files_in_input_dir

# count the frequency of the words in the files in the input directory
counter={}
for filename in files_in_input_dir:
    with open('data/input/'+filename) as f:
        for l in f:
            for w in l.split( ):
                w = w.lower().strip(",.!?")
                counter[w] = counter.get(w, 0) + 1