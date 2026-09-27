#!/bin/bash
# tilt 10 (installed): emergency landing after failure; then tilt 0: hover + landing; then reinstall tilt 10
CAMPAIGN=c2 source "$(dirname "$0")/common.sh"
for m in 1 2 3 4 5 6; do run sitl_land_t10 $m LAND=1; done
inst gen0
for m in 1 2 3 4 5 6; do run sitl_kill_t0 $m; done
for m in 1 2 3 4 5 6; do run sitl_land_t0 $m LAND=1; done
inst gen
finish
