import argparse
import sys
from pathlib import Path
from typing import NoReturn


def main():
    args = make_parser().parse_args()
    working_directory = args.dir

    if not working_directory.exists():
        abort_and_print_message(f"Directory {working_directory} does not exist.")
    if not  working_directory.is_dir():
        abort_and_print_message(f"{working_directory} is not a directory.")

    dry_run = not args.execute

    dirs_and_files = collect_file_paths(working_directory)

    for item in dirs_and_files:
        print(item)

    if dry_run:
        abort_and_print_message("DRY_RUN: No changes made.", error = False)


def collect_file_paths(working_directory: str) -> list[Path]:
    dirs_and_files = []
    for dir_or_file in Path.iterdir(working_directory):
        if dir_or_file.is_dir():
            dirs_and_files.extend(collect_file_paths(Path(str(dir_or_file) + "/")))
        else:
            dirs_and_files.append(Path(dir_or_file))
    return dirs_and_files  


def expanded_path(path: str) -> Path:
    return Path(path).expanduser()


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("dir", type=expanded_path, help="Directory to scan.")
    parser.add_argument(
        "--execute", action="store_true", help="Actually delete duplicate files."
    )

    return parser


def abort_and_print_message(message: str, error: bool = True) -> NoReturn:
    print(f"{"Error:" if error else ""} {message} Aborting...")
    sys.exit(1)


if __name__ == "__main__":
    main()
