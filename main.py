import pandas as pd

file = 'AFCO Lijst.txt'

def extract_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if "=" in line]
    data_extracted = [line.split('=', 1) for line in filtered_lines]
    return pd.DataFrame(data_extracted, columns=['Abbreviation', 'Meaning'])

if __name__ == "__main__":
    data = extract_data(file)
    print("Done")

