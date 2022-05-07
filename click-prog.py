from pathlib import Path
from typing import List

import click

SCRIPT_DIR = Path(__file__).parent
CWD = Path().cwd()
SUPPORTED_EXTS = [".pcap", ".pcapng"]


def search_path(path: Path, exts: List[str]) -> List[Path]:
    paths: List[Path] = []
    for path in path.glob("*"):
        if path.is_file() and path.suffix in exts:
            paths.append(path)
    return paths


def find_pcaps(path_list: List[Path], exts: List[str] = SUPPORTED_EXTS) -> List[Path]:
    pcaps: List[Path] = []
    for path in path_list:
        if path.is_dir():
            paths = search_path(path, exts)
            pcaps.extend(paths)
        if path.suffix in exts:
            pcaps.append(path)
    return pcaps


def path_callback(ctx, param, value):
    return find_pcaps(value)


@click.command()
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(exists=True, resolve_path=True, path_type=Path),
    callback=path_callback,
)
@click.option(
    "--no-file",
    is_flag=True,
    default=False,
    help="Whether to extract results into a file",
)
@click.option(
    "--outdir",
    default=CWD,
    help="Output directory to extract into, defaults to current working directory",
    type=click.Path(exists=True, resolve_path=True, path_type=Path),
)
def cli(paths, no_file, outdir):
    """Program for extracting data from pcap files"""
    # pcaps = find_pcaps(paths)
    run(paths, no_file, outdir)


def run(pcaps: List[Path], no_file: bool = False, outdir: Path = CWD) -> int:
    """Start probing pcap files and returning results"""
    file_attrs = []
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
    SystemExit(cli())
