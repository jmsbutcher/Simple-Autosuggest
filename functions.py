
import numpy as np
import pandas as pd
import textdistance
import re
from collections import Counter
import os
import glob


def gather_text(directory, file_types) -> str:

    data = ""

    for root, _, files in os.walk(directory):
            
        for file_type in file_types:

            for filename in glob.glob(os.path.join(root, f'*.{file_type}')):

                with open(filename, 'r') as file:

                    data += (file.read() + "\n")

    return data



def get_suggestions(input, text_directory_path, file_types, num_suggestions):

    data = gather_text(text_directory_path, file_types)

    words = re.findall('[A-Za-z]\w+', data)

    word_freq_dict = Counter(words)

    probs = {}
    for word, freq in word_freq_dict.items():
        probs[word] = freq / len(words)

    input = input.lower()

    similarities = [1-(textdistance.Jaccard(qval=2)).distance(w, input) for w in word_freq_dict.keys()]
    df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
    df = df.rename(columns={"index":"input", 0: "Prob"})
    df["Similarity"] = similarities
    suggestions = df.sort_values(["Similarity", "Prob"], ascending=False).head(num_suggestions)

    return list(suggestions["input"].head(num_suggestions))



if __name__ == "__main__":
    print("Hello")
