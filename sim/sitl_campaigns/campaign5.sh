#!/bin/bash
# T-12 / T-12b matrix: automatic landing by COM_ACT_FAIL_ACT, stock (CA_METHOD 2) vs own allocator (CA_METHOD 3);
# side wind force 15 N; failure during a 5 m/s transit; maneuvers without failure; empty tank 20 kg.
CAMPAIGN=c5 source "$(dirname "$0")/common.sh"
S="CA_METHOD=2,COM_ACT_FAIL_ACT=2"
B="CA_METHOD=3,COM_ACT_FAIL_ACT=2"
run c5_man_stock 0 MANEUVER=1 PARAMS=CA_METHOD=2
run c5_man_bls 0 MANEUVER=1 PARAMS=CA_METHOD=3
run c5_wind_bls 0 WIND_N=15 PARAMS=CA_METHOD=3
for m in 1 2 3 4 5 6; do
  run c5_auto_stock $m AUTOLAND=1 PARAMS=$S
  run c5_auto_bls $m AUTOLAND=1 PARAMS=$B
  run c5_wind_stock $m AUTOLAND=1 WIND_N=15 PARAMS=$S
  run c5_wind_bls $m AUTOLAND=1 WIND_N=15 PARAMS=$B
  run c5_transit_stock $m AUTOLAND=1 MANEUVER=1 FAIL_DELAY=3 PARAMS=$S
  run c5_transit_bls $m AUTOLAND=1 MANEUVER=1 FAIL_DELAY=3 PARAMS=$B
done
inst gen20
for m in 1 2 3 4 5 6; do
  run c5_e20_auto_stock $m AUTOLAND=1 PARAMS=$S
  run c5_e20_auto_bls $m AUTOLAND=1 PARAMS=$B
  run c5_e20_hover_bls $m PARAMS=CA_METHOD=3
done
run c5_e20_man_bls 0 MANEUVER=1 PARAMS=CA_METHOD=3
inst gen
finish
