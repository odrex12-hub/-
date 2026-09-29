"""Stack model: AGD6.07.010 + Firefly ROC-RK3588S-PC (envelope). Frame: footprint MECH1 at board centre,
z = 0 on the top surface of AGD6.07.010. Firefly data (118 x 111.6 mm, 12 V DC 5.5x2.1) from public reviews,
connector set, hole positions and heights are ASSUMED (CHECK_DATASHEET Firefly)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "AGD6.3dshapes"))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import make3d as m
box, pin, text, write = m.box, m.pin, m.text, m.write

BOARD_T = 1.6
ST_AGD = 8.0          # standoffs base plate -> AGD6.07.010 (bottom parts <= 4.3 mm)
GAP = 25.0            # AGD6 top -> Firefly bottom (DC/DC 10.7 mm + mated JST/pin-header plugs <= 14 mm)
PLATE = 2.0
zp_top = -(BOARD_T + ST_AGD)                    # base plate top
FF_W, FF_L = 118.0, 111.6
zf = GAP                                         # Firefly PCB bottom
ALU, BLK, BRASS, GRN, GRY, WHT = (0.72, 0.74, 0.77), (0.08, 0.08, 0.09), (0.8, 0.65, 0.3), (0.05, 0.22, 0.12), (0.55, 0.55, 0.57), (0.93, 0.93, 0.93)

parts = [(box(-65, 65, -80, 80, zp_top - PLATE, zp_top), (0.35, 0.36, 0.38))]          # base plate 130 x 160
for x in (-25, 25):                                                                    # AGD6 holes 50 x 110
    for y in (-55, 55):
        parts += [(pin(x, y, 5.0, zp_top, -BOARD_T), BRASS), (pin(x, y, 5.5, 0, 2.0), GRY)]
hx, hy = FF_W / 2 - 3.5, FF_L / 2 - 3.5                                                # Firefly holes (ASSUMED)
for x in (-hx, hx):
    for y in (-hy, hy):
        parts += [(pin(x, y, 5.0, zp_top, zf), BRASS), (pin(x, y, 5.5, zf + BOARD_T, zf + BOARD_T + 2.0), GRY)]
zt = zf + BOARD_T
parts += [(box(-FF_W / 2, FF_W / 2, -FF_L / 2, FF_L / 2, zf, zt), GRN)]                # Firefly PCB
parts += [(box(-22, 22, -22, 22, zt, zt + 3.0), BLK)]                                  # heatsink base over RK3588S
parts += [(box(-22 + i * 4.4, -22 + i * 4.4 + 1.6, -22, 22, zt + 3.0, zt + 14.0), BLK) for i in range(10)]
# rear edge (y = -FF_L/2 in footprint coords = board "top" side): I/O connectors (ASSUMED set)
e = -FF_L / 2
io = [(-52, 9.0, 11.0, 14.0, BLK, "DC 12V"), (-38, 15.0, 6.0, 11.0, ALU, "HDMI"), (-20, 16.0, 13.5, 21.0, ALU, "LAN"),
      (0, 14.5, 15.6, 17.0, ALU, "USB3"), (17, 14.5, 15.6, 17.0, ALU, "USB3"), (33, 9.0, 3.3, 7.5, ALU, "USB-C")]
for x, w, h, d, col, lab in io:
    parts += [(box(x - w / 2, x + w / 2, e - 1.0, e - 1.0 + d, zt, zt + h), col)]
parts += [(box(30, 52, 5, 27, zt, zt + 1.2), BLK)]                                     # eMMC/LPDDR area
parts += [(text("Firefly ROC-RK3588S-PC", 4.0, 0, 34, zt, 0.08), WHT),
          (text("envelope model - CHECK_DATASHEET", 2.5, 0, 42, zt, 0.08), WHT),
          (text("12 V from AGD6 J202 (XT30 -> DC 5.5x2.1)", 2.5, -10, -30, zt, 0.08), WHT)]
write("AGD6_Firefly_stack_mech.step", parts)
print("stack height above base plate: %.1f mm" % (zt + 14.0 - zp_top))
