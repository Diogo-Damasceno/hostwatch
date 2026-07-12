from host_audit import core
import os, tempfile

def _mk(content):
    f = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    f.write(content.encode()); f.close()
    return f.name

def test_digest_stable():
    n = _mk("hello")
    assert core.digest(n) == core.digest(n)
    os.unlink(n)

def test_diff_changed():
    n = _mk("x")
    old = core.baseline([n])
    open(n, "w").write("y")   # altera o mesmo arquivo
    new = core.baseline([n])
    d = core.diff(old, new)
    assert d["changed"] == [n]
    os.unlink(n)

def test_diff_added_removed():
    a = _mk("x"); b = _mk("y")
    old = core.baseline([a]); new = core.baseline([b])
    d = core.diff(old, new)
    assert b in d["added"] and a in d["removed"]
    os.unlink(a); os.unlink(b)
