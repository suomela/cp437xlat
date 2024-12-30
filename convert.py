from contextlib import redirect_stdout


def myrepr(c):
    if c in ["'", "\\"]:
        return f"'\\{c}'"
    elif c.isprintable():
        return f"'{c}'"
    else:
        return f"'\\u{{{ord(c):04X}}}'"


def main():
    xlat = []
    with open("cp437.txt") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("#") or line == "\x1a":
                continue
            cp437, unicode, comment = line.split("\t")
            assert comment.startswith("#")
            cp437 = int(cp437, base=0)
            unicode = chr(int(unicode, base=0))
            assert cp437 == len(xlat)
            xlat.append(unicode)

    print("/// CP437 translation table.")
    print("///")
    print("/// Generated from:")
    print(
        "/// - source: <https://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/PC/CP437.TXT>"
    )
    print("/// - license: <https://www.unicode.org/license.txt>")
    print("pub const CP437: [char; 256] = [")
    start = "   "
    buf = None
    for r in map(myrepr, xlat):
        add = " " + r + ","
        if buf is None:
            buf = start
        if len(buf + add) >= 100:
            print(buf)
            buf = start
        buf = buf + add
    if buf is not None:
        print(buf)
    print("];")


if __name__ == "__main__":
    with open("cp437.rs", "w") as f:
        with redirect_stdout(f):
            main()
