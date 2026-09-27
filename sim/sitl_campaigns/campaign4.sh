#!/bin/bash
# BLS allocator variants: low idle (5 % omega ≈ 0.25 % Fmax), higher yaw weight
CAMPAIGN=c4 source "$(dirname "$0")/common.sh"
LOW="SIM_GZ_EC_MIN1=22,SIM_GZ_EC_MIN2=22,SIM_GZ_EC_MIN3=22,SIM_GZ_EC_MIN4=22,SIM_GZ_EC_MIN5=22,SIM_GZ_EC_MIN6=22,MPC_THR_HOVER=0.51"
for m in 1 2 3 4 5 6; do run sitl_blsidle $m PARAMS=CA_METHOD=3,$LOW; done
for m in 1 6; do run sitl_blswy1 $m PARAMS=CA_METHOD=3,CA_BLS_W_YAW=1.0; done
for m in 1 2 3 4 5 6; do run sitl_blsland $m LAND=1 PARAMS=CA_METHOD=3; done
finish
