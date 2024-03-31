# James Butcher
# 3/23/24
# 
# Generated with ChatGPT-3.5 from prompt:
#  "write a python function that creates a single text file consisting of all
#   the contents of specific types of files within all the subdirectories of a
#   specified directory"

import os
import glob


def combine_files(directory, file_types, output_file):

    with open(output_file, 'w') as outfile:

        for root, _, files in os.walk(directory):
            
            for file_type in file_types:

                for file in glob.glob(os.path.join(root, f'*.{file_type}')):

                    with open(file, 'r') as infile:
                        
                        outfile.write(f'=== {file} ===\n')
                        outfile.write(infile.read())
                        outfile.write('\n')


if __name__ == "__main__":

    # Prompt user to enter the path to the training directory
    training_path = input("Enter full path to the directory you want to train on:")

    file_types = ["h", "cpp", "py"]
    output_file = "training_text.txt"

    combine_files(training_path, file_types, output_file)


