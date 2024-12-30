CP437 translation table
=======================

Files in this repository:

- `cp437.txt`: translation table for mapping CP437 to Unicode.
- `cp437.rs`: Rust file that contains a table for mapping CP437 bytes to Unicode characters.
- `download.sh`: shell script that downloads `cp437.txt` from <https://unicode.org/>.
- `convert.py`: Python script that converts `cp437.txt` to `cp437.rs`.

You can simply copy `cp437.rs` and use it for your own purposes, but if you want to re-generate it, run:

    uv run convert.py
