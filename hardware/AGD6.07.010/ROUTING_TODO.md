# АГД6.07.010 — соединения, которые осталось развести вручную

Сформировано из `drc_report.txt`. Координаты — мм от левого верхнего угла платы (100 × 150 мм).
Рекомендуемый порядок в KiCad 10: Редактор плат → «Трассировать» (X) с интерактивным раздвиганием (Shove).
Силовые цепи (VIN_*, SNS, +12V, V12_*, VIN_AI*, AI_SNS, V12AI_RAW, V12_AI) — только на внешних слоях, ширина по классу цепи
или участок полигона; переход между слоями — не менее 2 переходных отверстий 0.8/0.4 мм на каждые 2 A (`calculations.md` §2).

| № | Цепь | Откуда | Координаты | Куда | Координаты |
|---|---|---|---|---|---|
| 1 | `+12V` | Pad 8 of U205 on F.Cu | (27.2; 93.2) | Track on B.Cu, length 0.1810 mm | (27.8; 90.2) |
| 2 | `+12V` | Track on B.Cu, length 1.2578 mm | (90.9; 38.6) | Track on F.Cu, length 0.9179 mm | (63.3; 17.4) |
| 3 | `+12V` | Zone 'PWR_+12V_0' on B.Cu, priority 10 | (93.6; 44.1) | Zone 'PWR_+12V_4' on F.Cu, priority 10 | (64.8; 63.7) |
| 4 | `+12V` | Zone 'PWR_+12V_0' on F.Cu, priority 10 | (73.0; 132.7) | Zone 'PWR_+12V_3' on B.Cu, priority 10 | (96.4; 105.0) |
| 5 | `+12V` | Zone 'PWR_+12V_10' on B.Cu, priority 10 | (36.0; 18.9) | Zone 'PWR_+12V_11' on F.Cu, priority 10 | (52.4; 17.8) |
| 6 | `+12V` | Zone 'PWR_+12V_12' on F.Cu, priority 10 | (58.3; 16.7) | Zone 'PWR_+12V_11' on F.Cu, priority 10 | (52.4; 17.8) |
| 7 | `+12V` | Zone 'PWR_+12V_4' on F.Cu, priority 10 | (64.8; 63.7) | Zone 'PWR_+12V_8' on F.Cu, priority 10 | (72.9; 63.1) |
| 8 | `+12V` | Zone 'PWR_+12V_6' on B.Cu, priority 10 | (59.4; 19.8) | Zone 'PWR_+12V_4' on F.Cu, priority 10 | (64.8; 63.7) |
| 9 | `+12V` | Zone 'PWR_+12V_6' on B.Cu, priority 10 | (59.4; 19.8) | Zone 'PWR_+12V_9' on B.Cu, priority 10 | (91.4; 34.4) |
| 10 | `+12V` | Zone 'PWR_+12V_7' on F.Cu, priority 10 | (18.6; 90.8) | Pad 8 of U205 on F.Cu | (27.2; 93.2) |
| 11 | `+3V3` | Pad 1 of U701 on F.Cu | (91.6; 130.6) | Track on F.Cu, length 0.5020 mm | (94.9; 130.2) |
| 12 | `+3V3` | Pad 3 of U703 on F.Cu | (18.8; 97.3) | Track on B.Cu, length 2.5470 mm | (21.2; 95.2) |
| 13 | `+5V` | Track on In2.Cu, length 4.6101 mm | (58.7; 15.9) | Pad 14 of U201 on F.Cu | (57.3; 18.6) |
| 14 | `/ADC_PRESS` | Track on F.Cu, length 11.4980 mm | (21.4; 40.9) | Pad 2 of R413 on F.Cu | (50.4; 18.4) |
| 15 | `/ETHERNET/E1_TXN` | PTH pad 2 of J1007 | (2.7; 26.2) | Pad 2 of J1001 on F.Cu | (6.0; 112.1) |
| 16 | `/ETHERNET/E1_TXP` | PTH pad 1 of J1007 | (2.7; 28.8) | Pad 1 of J1001 on F.Cu | (6.0; 110.8) |
| 17 | `/ETHERNET/E3_TXN` | Pad 2 of J1003 on F.Cu | (6.0; 133.1) | PTH pad 10 of J1007 | (12.9; 26.2) |
| 18 | `/ETHERNET/E3_TXP` | Pad 1 of J1003 on F.Cu | (6.0; 131.8) | PTH pad 9 of J1007 | (12.9; 28.8) |
| 19 | `/I2C_SCL` | Pad 2 of U703 on F.Cu | (17.4; 97.3) | Track on F.Cu, length 3.7356 mm | (20.1; 96.0) |
| 20 | `/I2C_SDA` | Track on F.Cu, length 0.6880 mm | (19.7; 92.7) | Pad 1 of U703 on F.Cu | (17.4; 96.5) |
| 21 | `/LOAD_SWITCHES_12V/OUT1` | Zone 'PWR_LOAD_SWITCHES_12V_OUT1_1' on F.Cu, priority 15 | (20.3; 132.3) | Zone 'PWR_LOAD_SWITCHES_12V_OUT1_0' on F.Cu, priority 15 | (19.5; 140.4) |
| 22 | `/LOAD_SWITCHES_12V/V12_FAN` | Zone 'PWR_LOAD_SWITCHES_12V_V12_FAN_0' on B.Cu, priority 25 | (38.4; 132.0) | Zone 'PWR_LOAD_SWITCHES_12V_V12_FAN_1' on B.Cu, priority 25 | (32.3; 127.3) |
| 23 | `/LOAD_SWITCHES_12V/V12_MON` | Pad 7 of U804 on F.Cu | (19.7; 93.7) | Pad 2 of R805 on B.Cu | (17.4; 90.4) |
| 24 | `/POWER_CONVERSION/AI_SNS` | Zone 'PWR_POWER_CONVERSION_AI_SNS_0' on B.Cu, priority 18 | (82.5; 55.8) | Zone 'PWR_POWER_CONVERSION_AI_SNS_1' on B.Cu, priority 18 | (64.2; 65.3) |
| 25 | `/POWER_CONVERSION/V12AI_RAW` | Track on B.Cu, length 1.3421 mm | (81.1; 56.5) | Pad 2 of U203 on F.Cu | (83.7; 57.1) |
| 26 | `/POWER_CONVERSION/V12_AI` | Pad 8 of U204 on F.Cu | (34.7; 93.2) | Track on F.Cu, length 12.4800 mm | (55.4; 94.5) |
| 27 | `/POWER_CONVERSION/V12_AI` | Pad 9 of U203 on F.Cu | (83.7; 52.9) | Track on F.Cu, length 2.1850 mm | (64.8; 72.6) |
| 28 | `/POWER_CONVERSION/V12_ALERT_N` | Track on B.Cu, length 1.3880 mm | (23.9; 91.5) | Pad 1 of TP208 on F.Cu | (25.7; 97.2) |
| 29 | `/POWER_CONVERSION/V12_ALERT_N` | Track on B.Cu, length 1.3880 mm | (23.9; 91.5) | Pad 3 of U205 on F.Cu | (22.9; 93.2) |
| 30 | `/POWER_CONVERSION/V12_RAW` | Zone 'PWR_POWER_CONVERSION_V12_RAW_0' on B.Cu, priority 19 | (68.2; 68.1) | Zone 'PWR_POWER_CONVERSION_V12_RAW_1' on B.Cu, priority 19 | (84.5; 19.0) |
| 31 | `/POWER_CONVERSION/VIN_AI` | Track on F.Cu, length 1.6040 mm | (66.8; 79.6) | Track on F.Cu, length 0.1416 mm | (67.9; 32.2) |
| 32 | `/POWER_CONVERSION/VIN_AI_F` | Track on B.Cu, length 2.1800 mm | (48.7; 78.9) | Track on F.Cu, length 3.3020 mm | (77.3; 83.4) |
| 33 | `/POWER_CONVERSION/VIN_AI_F` | Zone 'PWR_POWER_CONVERSION_VIN_AI_F_1' on B.Cu, priority 21 | (17.8; 55.0) | Zone 'PWR_POWER_CONVERSION_VIN_AI_F_1' on F.Cu, priority 21 | (55.6; 71.1) |
| 34 | `/POWER_INPUT_14S/GATE_DRV` | Pad 10 of U101 on F.Cu | (52.6; 20.7) | Pad 1 of R101 on B.Cu | (68.4; 22.9) |
| 35 | `/POWER_INPUT_14S/INA1_N` | Track on In2.Cu, length 3.8720 mm | (32.9; 45.9) | Pad 9 of U102 on F.Cu | (33.7; 48.7) |
| 36 | `/POWER_INPUT_14S/SNS` | Zone 'PWR_POWER_INPUT_14S_SNS_1' on F.Cu, priority 17 | (47.8; 18.1) | Zone 'PWR_POWER_INPUT_14S_SNS' on B.Cu, priority 17 | (85.3; 11.3) |
| 37 | `/POWER_INPUT_14S/UV` | Pad 3 of U101 on F.Cu | (48.4; 21.7) | Track on B.Cu, length 0.8077 mm | (38.7; 19.6) |
| 38 | `/POWER_INPUT_14S/VIN_F` | Track on B.Cu, length 2.6807 mm | (51.2; 16.9) | Pad 2 of U101 on F.Cu | (48.4; 21.2) |
| 39 | `/POWER_INPUT_14S/VIN_F` | Zone 'PWR_POWER_INPUT_14S_VIN_F_1' on F.Cu, priority 13 | (23.4; 10.8) | Zone 'PWR_POWER_INPUT_14S_VIN_F_0' on F.Cu, priority 13 | (30.1; 10.8) |
| 40 | `/POWER_INPUT_14S/VIN_F` | Zone 'PWR_POWER_INPUT_14S_VIN_F_2' on F.Cu, priority 13 | (78.6; 10.9) | Zone 'PWR_POWER_INPUT_14S_VIN_F_0' on F.Cu, priority 13 | (30.1; 10.8) |
| 41 | `/POWER_INPUT_14S/VIN_PGOOD` | Pad 8 of U101 on F.Cu | (52.6; 21.7) | Track on B.Cu, length 2.6412 mm | (54.7; 23.0) |
| 42 | `/POWER_INPUT_14S/VIN_RAW` | Zone 'PWR_POWER_INPUT_14S_VIN_RAW_0' on B.Cu, priority 31 | (55.4; 12.0) | Zone 'PWR_POWER_INPUT_14S_VIN_RAW_1' on F.Cu, priority 31 | (18.1; 10.8) |
| 43 | `/VIN_PROT` | Track on B.Cu, length 4.5096 mm | (37.4; 45.9) | Pad 8 of U102 on F.Cu | (33.7; 49.2) |
| 44 | `/VIN_PROT` | Track on F.Cu, length 0.4681 mm | (46.2; 18.1) | Pad 9 of U101 on F.Cu | (52.6; 21.2) |
| 45 | `/VIN_PROT` | Zone 'PWR_VIN_PROT_1' on F.Cu, priority 11 | (48.9; 23.0) | Zone 'PWR_VIN_PROT_0' on F.Cu, priority 11 | (54.8; 20.3) |
| 46 | `/VIN_PROT` | Zone 'PWR_VIN_PROT_2' on F.Cu, priority 11 | (70.5; 10.8) | Pad 9 of U101 on F.Cu | (52.6; 21.2) |
| 47 | `GND` | Pad 1 of D813 on B.Cu | (21.3; 93.2) | Pad 7 of U205 on F.Cu | (27.2; 93.7) |
| 48 | `GND` | Pad 2 of R852 on F.Cu | (40.4; 111.9) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 49 | `GND` | Pad 2 of U202 on F.Cu | (61.4; 20.1) | Track on B.Cu, length 0.3341 mm | (60.9; 20.4) |
| 50 | `GND` | Pad 3 of U804 on F.Cu | (15.4; 93.2) | Track on B.Cu, length 0.1421 mm | (16.3; 92.7) |
| 51 | `GND` | Track on B.Cu, length 0.6293 mm | (32.6; 39.8) | Pad 2 of C106 on F.Cu | (34.4; 44.9) |
| 52 | `GND` | Track on B.Cu, length 1.1993 mm | (30.4; 49.9) | Pad 7 of U102 on F.Cu | (33.7; 49.7) |
| 53 | `GND` | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 54 | `GND` | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 55 | `GND` | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 56 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 2 of C103 on F.Cu | (22.3; 84.9) |
| 57 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 4 of J412 on F.Cu | (94.0; 108.3) |
| 58 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 4 of U702 on F.Cu | (22.7; 97.8) |
| 59 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 7 of U204 on F.Cu | (34.7; 93.7) |
| 60 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 7 of U205 on F.Cu | (27.2; 93.7) |
| 61 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) |
| 62 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) |
| 63 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) |
| 64 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) |
| 65 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) |
| 66 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |

Всего: 66 соединений.
