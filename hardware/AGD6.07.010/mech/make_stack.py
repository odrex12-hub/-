"""Stack model: AGD6.07.010 + Firefly ROC-RK3588S-PC (envelope). Frame: centre of AGD6.07.010, z = 0 on its top surface.
Firefly board 90 x 60 mm, 12 V DC 5.5x2.1, 12 V 3-pin fan header (public reviews); hole pattern, connector set and
heights are ASSUMED (CHECK_DATASHEET Firefly). Firefly sits on an adapter plate carried by the four AGD6 standoffs."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "AGD6.3dshapes"))
import make3d as m
box, pin, text, write = m.box, m.pin, m.text, m.write
m.OUT = HERE + "/"

BOARD_T = 1.6
ST_LOW = 8.0          # bay floor -> AGD6 bottom (bottom parts <= 4.3 mm)
GAP = 30.0            # AGD6 top -> adapter plate bottom (DC/DC 10.7 mm, vertical plugs on pin headers <= 14 mm + wire bend)
PLATE_T = 2.0         # adapter plate (FR4 / Al)
ST_FF = 5.0           # adapter plate -> Firefly bottom
FF_X, FF_Y = 60.0, 90.0                       # Firefly 90 x 60 mm, long side along the AGD6 long side
HX, HY = FF_X / 2 - 3.5, FF_Y / 2 - 3.5       # Firefly holes 3.5 mm from corners (ASSUMED)
ALU, BLK, BRASS, GRN, GRY, WHT, FLOOR = (0.72, 0.74, 0.77), (0.08, 0.08, 0.09), (0.8, 0.65, 0.3), (0.05, 0.22, 0.12), \
    (0.55, 0.55, 0.57), (0.93, 0.93, 0.93), (0.35, 0.36, 0.38)

zfl = -(BOARD_T + ST_LOW)
parts = [(box(-60, 60, -85, 85, zfl - 2.0, zfl), FLOOR)]                               # bay floor (context)
zpl = GAP
for x in (-25, 25):                                                                    # AGD6 holes 50 x 110
    for y in (-55, 55):
        parts += [(pin(x, y, 5.0, zfl, -BOARD_T), BRASS), (pin(x, y, 5.0, 0, zpl), BRASS),
                  (pin(x, y, 5.5, zpl + PLATE_T, zpl + PLATE_T + 2.0), GRY)]
PL = (0.55, 0.6, 0.65)                                                                 # adapter plate 64 x 120 with a notch
parts += [(box(-15, 32, -60, 60, zpl, zpl + PLATE_T), PL), (box(-32, -15, -32, 60, zpl, zpl + PLATE_T), PL),  # over J1007/J309/J310
          (box(-32, -15, -60, -50, zpl, zpl + PLATE_T), PL)]
zf = zpl + PLATE_T + ST_FF
OY = 10.0                                     # Firefly shifted +10 mm away from the header block
for x in (-HX, HX):
    for y in (-HY, HY):
        parts += [(pin(x, y + OY, 5.0, zpl + PLATE_T, zf), BRASS), (pin(x, y + OY, 5.5, zf + BOARD_T, zf + BOARD_T + 2.0), GRY)]
zt = zf + BOARD_T
parts += [(box(-FF_X / 2, FF_X / 2, -FF_Y / 2 + OY, FF_Y / 2 + OY, zf, zt), GRN)]               # Firefly PCB
parts += [(box(-20, 20, -12 + OY, 28 + OY, zt, zt + 2.5), BLK)]                                  # heatsink base 40 x 40
parts += [(box(-20 + i * 4.3, -20 + i * 4.3 + 1.4, -12 + OY, 28 + OY, zt + 2.5, zt + 10.0), BLK) for i in range(10)]
parts += [(box(-20, 20, -12 + OY, 28 + OY, zt + 10.0, zt + 20.0), (0.15, 0.15, 0.17))]          # 40 x 40 x 10 fan, 12 V
parts += [(text("FAN 12V", 3.0, 0, 8 + OY, zt + 20.0, 0.08), WHT)]
e = -FF_Y / 2 + OY                                                                          # I/O edge faces the AGD6 XT30 edge
io = [(-21, 9.0, 11.0, 14.0, BLK), (-7, 16.0, 13.5, 21.0, ALU), (10, 14.5, 7.0, 17.0, ALU), (23, 9.0, 3.3, 7.5, ALU)]
for x, w, h, d, col in io:                                                             # DC jack, LAN, USB3, USB-C (ASSUMED)
    parts += [(box(x - w / 2, x + w / 2, e - 1.0, e - 1.0 + d, zt, zt + h), col)]
parts += [(text("Firefly ROC-RK3588S-PC 90x60", 2.6, 0, 36 + OY, zt, 0.08), WHT),
          (text("envelope - CHECK_DATASHEET", 2.0, 0, 41 + OY, zt, 0.08), WHT)]
write("AGD6_Firefly_stack_mech.step", parts)
print("top of fan above AGD6 top: %.1f mm; above bay floor: %.1f mm" % (zt + 20.0, zt + 20.0 - zfl))
