"""CLI de host_audit."""
from __future__ import annotations
import sys
from host_audit.core import main as _core_main

def main(argv=None):
    return _core_main(argv if argv is not None else sys.argv[1:])

if __name__ == "__main__":
    raise SystemExit(main())
