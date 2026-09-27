#!/bin/bash
# bounded least-squares allocator (CA_METHOD 3): baseline hover + physical failure of each motor at hover
CAMPAIGN=c3 source "$(dirname "$0")/common.sh"
for m in 0 1 2 3 4 5 6; do run sitl_bls $m PARAMS=CA_METHOD=3; done
finish
