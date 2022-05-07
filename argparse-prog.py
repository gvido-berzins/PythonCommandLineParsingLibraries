import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List

SCRIPT_DIR = Path(__file__).parent
CWD = Path().cwd()
SUPPORTED_EXTS = [".pcap", ".pcapng"]


def search_path(path: Path, exts: List[str]) -> List[Path]:
    paths: List[Path] = []
    for path in path.glob("*"):
        if path.is_file() and path.suffix in exts:
            paths.append(path)
    return paths


def find_pcaps(path_strs: str, exts: List[str] = SUPPORTED_EXTS) -> List[Path]:
    pcaps: List[Path] = []
    path_list: List[str] = []
    if not isinstance(path_strs, list):
        path_list.append(path_strs)
    else:
        path_list.extend(path_strs)

    for path_str in path_list:
        path = Path(path_str)
        if not path.exists():
            continue
        if path.is_dir():
            paths = search_path(path, exts)
            pcaps.extend(paths)
        if path.suffix in exts:
            pcaps.append(path)
    return pcaps


def parse_args(argv: List[str]):
    parser = ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="+",
        type=find_pcaps,
        help=(
            "Paths to network traces, can be either filenames or a directory containing "
            "pcap files, defaults to the current working directory"
        ),
    )
    parser.add_argument(
        "--no-file", action="store_true", help="Whether to extract results into a file"
    )
    parser.add_argument(
        "-o",
        "--outdir",
        type=Path,
        help="Output directory to extract into, defaults to current working directory",
        default=CWD,
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    pcaps = [p for paths in args.paths for p in paths]
    return run(pcaps, args.no_file, args.outdir)


def run(pcaps: List[Path], no_file: bool = False, outdir: Path = CWD) -> int:
    """Start probing pcap files and returning results"""
    file_attrs = []
    print(pcaps)
    for pcap in pcaps:
        stat = pcap.stat()
        attrs = f"{pcap}: size={stat.st_size}, ctime={stat.st_ctime}"
        print(attrs)
        file_attrs.append(attrs)

    if not no_file:
        text = "\n".join(file_attrs + ["\n"])
        outdir.mkdir(parents=True, exist_ok=True)
        outdir.joinpath("results.txt").write_text(text)
    return 0


if __name__ == "__main__":
    SystemExit(main(sys.argv[1:]))
