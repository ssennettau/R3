import argparse
import logging

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description = "Analyzes an audio file to return the key points of a dictation",
        usage = "%(prog)s [OPTIONS] [INPUT]"
    )
    parser.add_argument(
        "--version", 
        action = "version",
        version = f"{parser.prog} v0.0.3"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action = "store_const",
        dest = "loglevel",
        const = logging.INFO,
        default = logging.WARNING
    )
    parser.add_argument(
        "-d",
        "--debug",
        action = "store_const",
        dest = "loglevel",
        const = logging.DEBUG,
    )
    parser.add_argument(
        "-o",
        "--output-format",
        action = "store",
        choices = ["json", "text"],
        type = str,
        default = "json",
        help = "Output format",
    )
    parser.add_argument(
        "input",
        action = "store",
        nargs = "*",
        help = "Audio file(s) to be analyzed"
    )

    return parser