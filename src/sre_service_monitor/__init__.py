import argparse
import logging
import sys
from importlib.metadata import version


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="sre-service-monitor",
        description="Check the health of the HTTP, TCP, and systemd services.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('sre-service-monitor')}",
    )
    parser.add_argument(
        "-v,", "--verbose", action="store_true", help="Enable debug logging."
    )

    args =parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )
    logging.getLogger(__name__).info("Scaffold ready; checks not implemented yet.")
