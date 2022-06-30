import configparser
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("editorconfig", type=str, help="editor configuration file path")
ap.add_argument("output", type=str, help="output csv file path")
args = ap.parse_args()

configs = configparser.ConfigParser()
configs.read(args.editorconfig, encoding="utf8")
with open(args.output, 'w') as f:
    for section in configs.keys():
        for key, value in configs.items(section):
            f.write(f"{section},{key},{value}\n")