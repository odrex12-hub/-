#!/bin/bash
# empty tank 20 kg: what rescues it — low ESC idle and/or lower yaw weight (own allocator), stock with low idle
CAMPAIGN=c6 source "$(dirname "$0")/common.sh"
# idle 5 % omega = 22 rad/s; hover throttle for 20 kg with that idle: (w_hover − 22)/(443.5 − 22)
LOW="SIM_GZ_EC_MIN1=22,SIM_GZ_EC_MIN2=22,SIM_GZ_EC_MIN3=22,SIM_GZ_EC_MIN4=22,SIM_GZ_EC_MIN5=22,SIM_GZ_EC_MIN6=22,MPC_THR_HOVER=0.40"
inst gen20
for m in 1 2 3 4 5 6; do
  run c6_lowidle_bls_hover $m PARAMS=CA_METHOD=3,$LOW
  run c6_lowidle_bls_auto $m AUTOLAND=1 PARAMS=CA_METHOD=3,COM_ACT_FAIL_ACT=2,$LOW
  run c6_lowidle_stock_auto $m AUTOLAND=1 PARAMS=CA_METHOD=2,COM_ACT_FAIL_ACT=2,$LOW
  run c6_wy01_bls_auto $m AUTOLAND=1 PARAMS=CA_METHOD=3,COM_ACT_FAIL_ACT=2,CA_BLS_W_YAW=0.1
done
inst gen
finish
