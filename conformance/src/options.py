"""
Command-line options for the test tool.
"""

import argparse
from dataclasses import dataclass


@dataclass
class _Options:
    report_only: bool | None
    skip_timing: bool
    type_checker: list[str] | None


def parse_options(argv: list[str]) -> _Options:
    parser = argparse.ArgumentParser()
    reporting_group = parser.add_argument_group("reporting")
    reporting_group.add_argument(
        "--report-only",
        action="store_true",
        help="regenerates the test suite report from past results",
    )
    reporting_group.add_argument(
        "--skip-timing",
        action="store_true",
        help="do not update timing information in the output files",
    )
    selection_group = parser.add_argument_group("selection")
    selection_group.add_argument(
        "--type-checker",
        action="append",
        help="run only the specified type checker (can be used multiple times)",
    )
    ret = _Options(**vars(parser.parse_args(argv)))
    return ret
