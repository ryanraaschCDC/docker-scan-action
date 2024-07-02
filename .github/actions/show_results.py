import argparse
import json
import pandas as pd

def print_results(path):
    pd.set_option('display.max_rows', None)
    with open(path, "r") as file:
        d = json.load(file)
    results = []
    for vul in d["matches"]:
        results.append({
            'NAME': vul['artifact']['name'],
            'INSTALLED': vul['artifact']['version'],
            'TYPE': vul['artifact']['type'],
            'VULNERABILITY': vul['vulnerability']['id'],
            'SEVERITY': vul['vulnerability']['severity']
        }
        )
    df = pd.DataFrame(results)
    df['SEVERITY'] = pd.Categorical(df['SEVERITY'], ['Critical','High', 'Medium', 'Low', 'Negligible', 'Unknown'])
    print(df.sort_values(["SEVERITY", "NAME", "VULNERABILITY"]).to_string(index=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    args = parser.parse_args()

    print_results(args.file)