import argparse
import sys
from pathlib import Path
from typing import NoReturn


def main():
    args = make_parser().parse_args()

    working_directory = args.dir
    dry_run = not args.execute

    for dirs_and_files in Path.iterdir(working_directory):
        print(dirs_and_files)

    if dry_run:
        abort_and_print_message("DRY_RUN: Stopping the script")


def expanded_path(path: str) -> Path:
    return Path(path).expanduser()


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("dir", type=expanded_path, help="Directory to check")
    parser.add_argument(
        "--execute", action="store_true", help="Actually delete duplicate files."
    )

    return parser


def abort_and_print_message(message: str) -> NoReturn:
    print(message)
    sys.exit(1)


if __name__ == "__main__":
    main()
