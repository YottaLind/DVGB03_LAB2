#!/usr/bin/env python3

from ui import TerminalUI

import os
import sys
import logging
import argparse


log = logging.getLogger(__name__)


def main(args):
    try:
        logging.basicConfig(
            format="[%(levelname)s] %(message)s",
            level=logging.__dict__[args.log_level.upper()],
        )
    except KeyError:
        log.critical("invalid log level: {}".format(args.log_level))
        return 1

    try:
        return TerminalUI("bst" if args.mode == "bst" else "avl").run()
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass


def get_args():
    parser = argparse.ArgumentParser("Terminal-based UI for BST/AVL trees")
    parser.add_argument("--log-level", "-l", type=str, default="info",
                        help="Minimum verbosity for logging.  Available in ascending order: "
                        "debug, info, warning, error, crirical.",
                        )
    parser.add_argument("--mode", "-m", type=str, default="bst",
                        help="Tree mode.  Available options: bst, avl.",
                        )
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main(get_args()))
