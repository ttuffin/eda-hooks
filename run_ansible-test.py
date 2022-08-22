from __future__ import annotations

import argparse
import subprocess

from typing import Sequence


def _run_ansible_test(command: str):
    args = ["ansible-test", command, "--venv"]
    result = subprocess.run(args, stdout=subprocess.DEVNULL)
    return result.returncode


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "test_type",
        nargs="?",
        help="The type of test to run; sanity or units. Default: sanity",
        default="sanity",
    )
    args = parser.parse_args(argv)

    retv = _run_ansible_test(args.test_type)
    return retv


if __name__ == "__main__":
    raise SystemExit(main())
