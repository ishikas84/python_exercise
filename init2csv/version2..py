import configparser
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("editorconfig", type=str, help="editor configuration file path")
ap.add_argument("output", type=str, help="output csv file path")
ap.add_argument("--collapsed", action="store_true", help="collapse")
args = ap.parse_args()

configs = configparser.ConfigParser()
configs.read(args.editorconfig, encoding="utf8")
with open(args.output, 'w') as f:
    if args.collapsed:
        keys = []
        for section in configs.keys():
            keys.extend(key for key, _ in configs.items(section))
        keys = list(set(keys))
        keys = ["header"] + keys
        head = ",".join(keys)
        f.write(f"{head}\n")
        for section in configs.keys():
            values = [section]
            if len(configs.items(section)) > 0:
                for key, value in configs.items(section):
                    values.append(value)
                f.write("{}\n".format(",".join(values)))            
    else:
        for section in configs.keys():
            for key, value in configs.items(section):
                f.write(f"{section},{key},{value}\n")
