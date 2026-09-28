# АГД6.07.010 — соединения, которые осталось развести вручную

Сформировано из `drc_report.txt` (rev 0.3). Координаты — мм от левого верхнего угла платы 100 × 150 мм.
Все остальные соединения разведены; DRC — 0 электрических ошибок, сверка со схемой — 0 расхождений.

**Итого 42 соединений:** земля — 19, силовые — 13, сигналы — 4, питание логики — 3, Ethernet — 3.

Почему не развела автоматика: на этих участках нужно раздвинуть или переложить уже проложенные дорожки
(push-and-shove / rip-up). Freerouting (2 прохода) и собственный трассировщик по сетке 0.1 мм (5 раундов) упираются в эти же соединения.

## Как доразвести в KiCad 10 (оценка 1.5–3 ч)
1. Редактор плат → Установки → Интерактивный трассировщик: режим **Shove** (раздвигать).
2. Для каждой строки: щёлкнуть на площадке «Откуда», клавиша **X**, провести к «Куда». Клавиша **V** — переход слоя.
3. **Силовые** (VIN_*, SNS, +12V, V12_*, VIN_AI*, AI_SNS, V12AI_RAW, V12_AI): только внешние слои F.Cu/B.Cu, ширина по классу
   (HV_14S 1.0 мм, PWR_AI 1.5 мм, PWR_12V 0.8 мм) или участок полигона; переход слоя — ≥ 2 отверстия 0.8/0.4 мм на каждые 2 A.
4. **Земля:** короткий отвод от площадки и переходное отверстие 0.6/0.3 мм на слой In1 (сплошная земля).
5. **Ethernet:** пары TXP/TXN вести рядом, 0.2/0.2 мм.
6. После — B (перезалить полигоны) и Инспектор → DRC: цель 0 неразведённых и 0 ошибок.

| № | Цепь | Откуда | Координаты | Куда | Координаты |
|---|---|---|---|---|---|
| 1 | `+12V` | Pad 8 of U205 on F.Cu | (27.2; 93.2) | Pad 1 of R217 on B.Cu | (27.8; 90.2) |
| 2 | `+3V3` | Pad 1 of U701 on F.Cu | (91.6; 130.6) | Track on F.Cu, length 0.5020 mm | (94.9; 130.2) |
| 3 | `+3V3` | Pad 3 of U703 on F.Cu | (18.8; 97.3) | Track on B.Cu, length 2.5470 mm | (21.2; 95.2) |
| 4 | `+5V` | Track on In2.Cu, length 4.6101 mm | (58.7; 15.9) | Pad 14 of U201 on F.Cu | (57.3; 18.6) |
| 5 | `/ADC_PRESS` | Track on F.Cu, length 11.4980 mm | (21.4; 40.9) | Pad 2 of R413 on F.Cu | (50.4; 18.4) |
| 6 | `/ETHERNET/E1_TXN` | PTH pad 2 of J1007 | (2.7; 26.2) | Track on In2.Cu, length 0.4000 mm | (2.0; 27.0) |
| 7 | `/ETHERNET/E3_TXN` | Pad 2 of J1003 on F.Cu | (6.0; 133.1) | PTH pad 10 of J1007 | (12.9; 26.2) |
| 8 | `/ETHERNET/E3_TXP` | PTH pad 9 of J1007 | (12.9; 28.8) | Track on B.Cu, length 0.4243 mm | (12.0; 29.5) |
| 9 | `/LOAD_SWITCHES_12V/V12_MON` | Pad 7 of U804 on F.Cu | (19.7; 93.7) | Pad 2 of R805 on B.Cu | (17.4; 90.4) |
| 10 | `/POWER_CONVERSION/AI_SNS` | Zone 'PWR_POWER_CONVERSION_AI_SNS_0' on F.Cu, priority 18 | (81.5; 52.7) | Zone 'PWR_POWER_CONVERSION_AI_SNS_1' on B.Cu, priority 18 | (64.2; 65.3) |
| 11 | `/POWER_CONVERSION/V12AI_RAW` | Track on B.Cu, length 1.3421 mm | (81.1; 56.5) | Pad 2 of U203 on F.Cu | (83.7; 57.1) |
| 12 | `/POWER_CONVERSION/V12_AI` | Pad 8 of U204 on F.Cu | (34.7; 93.2) | Track on F.Cu, length 12.4800 mm | (55.4; 94.5) |
| 13 | `/POWER_CONVERSION/V12_AI` | Pad 9 of U203 on F.Cu | (83.7; 52.9) | Track on F.Cu, length 2.1850 mm | (64.8; 72.6) |
| 14 | `/POWER_CONVERSION/V12_ALERT_N` | Pad 2 of R218 on B.Cu | (23.9; 92.9) | Pad 3 of U205 on F.Cu | (22.9; 93.2) |
| 15 | `/POWER_CONVERSION/VIN_AI` | Track on F.Cu, length 1.6040 mm | (66.8; 79.6) | Track on F.Cu, length 0.1416 mm | (67.9; 32.2) |
| 16 | `/POWER_INPUT_14S/GATE_DRV` | Pad 10 of U101 on F.Cu | (52.6; 20.7) | Pad 1 of R101 on B.Cu | (68.4; 22.9) |
| 17 | `/POWER_INPUT_14S/INA1_N` | Track on In2.Cu, length 3.8720 mm | (32.9; 45.9) | Pad 9 of U102 on F.Cu | (33.7; 48.7) |
| 18 | `/POWER_INPUT_14S/SNS` | Zone 'PWR_POWER_INPUT_14S_SNS_1' on F.Cu, priority 17 | (47.8; 18.1) | Zone 'PWR_POWER_INPUT_14S_SNS' on B.Cu, priority 17 | (85.3; 11.3) |
| 19 | `/POWER_INPUT_14S/UV` | Pad 3 of U101 on F.Cu | (48.4; 21.7) | Track on B.Cu, length 0.8077 mm | (38.7; 19.6) |
| 20 | `/POWER_INPUT_14S/VIN_F` | Pad 2 of U101 on F.Cu | (48.4; 21.2) | Track on B.Cu, length 2.6807 mm | (51.2; 16.9) |
| 21 | `/POWER_INPUT_14S/VIN_PGOOD` | Pad 8 of U101 on F.Cu | (52.6; 21.7) | Track on B.Cu, length 2.3531 mm | (53.0; 24.7) |
| 22 | `/VIN_PROT` | Pad 8 of U102 on F.Cu | (33.7; 49.2) | Track on B.Cu, length 4.5096 mm | (37.4; 45.9) |
| 23 | `/VIN_PROT` | Track on B.Cu, length 12.1643 mm | (46.5; 18.4) | Pad 9 of U101 on F.Cu | (52.6; 21.2) |
| 24 | `GND` | Pad 2 of R852 on F.Cu | (40.4; 111.9) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 25 | `GND` | Pad 2 of U202 on F.Cu | (61.4; 20.1) | Track on B.Cu, length 0.3341 mm | (60.9; 20.4) |
| 26 | `GND` | Pad 4 of U702 on F.Cu | (22.7; 97.8) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 27 | `GND` | Pad 7 of U204 on F.Cu | (34.7; 93.7) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 28 | `GND` | Track on B.Cu, length 0.6293 mm | (32.6; 39.8) | Pad 2 of C106 on F.Cu | (34.4; 44.9) |
| 29 | `GND` | Track on B.Cu, length 1.1993 mm | (30.4; 49.9) | Pad 7 of U102 on F.Cu | (33.7; 49.7) |
| 30 | `GND` | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 31 | `GND` | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 32 | `GND` | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 33 | `GND` | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 34 | `GND` | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 35 | `GND` | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 36 | `GND` | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
| 37 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 2 of C103 on F.Cu | (22.3; 84.9) |
| 38 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 4 of J412 on F.Cu | (94.0; 108.3) |
| 39 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Pad 7 of U205 on F.Cu | (27.2; 93.7) |
| 40 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_BOTTOM' on B.Cu, priority 0 | (0.3; 0.3) |
| 41 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_PLANE' on In1.Cu, priority 0 | (0.3; 0.3) |
| 42 | `GND` | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) | Zone 'GND_TOP' on F.Cu, priority 0 | (0.3; 0.3) |
