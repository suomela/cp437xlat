CP437 translation table for Rust
================================

Files in this repository:

- `cp437.txt`: translation table for mapping CP437 to Unicode, provided by <https://unicode.org/>.
- `cp437.rs`: Rust source code that contains a table for mapping CP437 bytes to Unicode characters.
- `download.sh`: shell script that downloads `cp437.txt` and the license terms `unicode-license.txt`.
- `convert.py`: Python script that converts `cp437.txt` to `cp437.rs`.

An example
----------

To translate a CP437-encoded file into a Unicode string, you can use something along these lines:
```rust
let mut file = File::open(path)?;
let mut bytes = Vec::new();
file.read_to_end(&mut bytes)?;
let mut string = String::new();
for b in bytes {
    string.push(cp437::CP437[b as usize]);
}
```

Building
--------

You can simply copy `cp437.rs` and use it for your own purposes, but if you want to re-generate it, run:
```bash
uv run convert.py
```

License
-------

The translation table `cp437.txt` is Copyright © 1991-2024 Unicode, Inc., please see <https://www.unicode.org/license.txt> or the file `unicode-license.txt` in this repository for the license terms.

Everything else you can freely use under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
