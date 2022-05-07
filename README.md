Repository with my command-line parsing utility example snippets
and a few examples of the same program implemented with different tools.

## Example code

Simple CLI program which accepts one or more paths and prints out
attributes for all paths that end with ".pcap" or ".pcapng" and outputs the 
results to a file.

Accepted Inputs:

- valid path, which could be a directory or a file, doesn't need to exist
- invalid path, ignored
  
Options:

- Result file output directory
- Flag to switch result file output off

## Resources for learning about CLI tool stuff

- [click documetation](https://click.palletsprojects.com/en/8.1.x/)
- [click examples](https://github.com/pallets/click/blob/main/examples)
- [Real Python Article](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
- [CLI guidelines](https://clig.dev/)
