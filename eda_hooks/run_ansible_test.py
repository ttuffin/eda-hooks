from __future__ import annotations

import argparse
import subprocess

from typing import Sequence


def _run_ansible_test(command: str):
    args = ["ansible-test", command, "--venv"]
    result = subprocess.run(args)
    return result.returncode


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "test_type",
        nargs="?",
        help="The type of test to run. Default: sanity",
        choices=["sanity", "units"],
        default="sanity",
    )
    args = parser.parse_args(argv)

    retv = _run_ansible_test(args.test_type)
    return retv


if __name__ == "__main__":
    raise SystemExit(main())
