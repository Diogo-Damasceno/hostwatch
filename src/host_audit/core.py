"""Monitor de integridade de arquivos por hash SHA-256."""
from __future__ import annotations
import hashlib, os

def digest(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(8192), b""):
            h.update(blk)
    return h.hexdigest()

def baseline(paths) -> dict:
    return {p: digest(p) for p in paths if os.path.isfile(p)}

def diff(old: dict, new: dict) -> dict:
    changed, added, removed = [], [], []
    for p, h in new.items():
        if p not in old:
            added.append(p)
        elif old[p] != h:
            changed.append(p)
    for p in old:
        if p not in new:
            removed.append(p)
    return {"changed": changed, "added": added, "removed": removed}

def main(argv=None):
    import sys
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) < 1:
        print("uso: host_audit <arquivo1> [arquivo2 ...]")
        return 2
    print(baseline(argv))
    return 0
