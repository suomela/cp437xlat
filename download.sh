#!/bin/bash

set -e

rm -f cp437.txt unicode-license.txt
curl -o cp437.txt https://unicode.org/Public/MAPPINGS/VENDORS/MICSFT/PC/CP437.TXT
curl -o unicode-license.txt https://www.unicode.org/license.txt
