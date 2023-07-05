import argparse
import glob
import os

import torch

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model_name_or_path", type=str)

    parser.add_argument("--train_data", type=str)
    parser.add_argument("--eval_data", type=str)

    parser.add_argument("--do_train", action="store_true")
    parser.add_argument("--do_eval", action="store_true")
    parser.add_argument("--do_test", action="store_true")

    args = parser.parse_args()

    if args.do_train:
        pass

    if args.do_eval:
        pass

    if args.do_test:
        pass

    return None

if __name__ == "__main__":
    main()