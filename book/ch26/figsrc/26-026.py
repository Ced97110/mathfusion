import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, O, r, d0, d1, role, lw=1.2):
    line(ax, [(O[0] + r * math.cos(math.radians(d0 + (d1 - d0) * i / 30)), O[1] + r * math.sin(math.radians(d0 + (d1 - d0) * i / 30))) for i in range(31)], role, lw=lw)
fig, ax = canvas(62)
O = (14, 8)
arrow(ax, O, (O[0] + 56, O[1]), "fixe", lw=0.9)
arrow(ax, O, (O[0], O[1] + 46), "fixe", lw=0.9)
arrow(ax, O, (O[0] + 46 * math.cos(math.radians(40)), O[1] + 46 * math.sin(math.radians(40))), "fixe", lw=0.9)
arc(ax, O, 14, 0, 40, "sujet", 1.6); arc(ax, O, 22, 40, 90, "autre", 1.6); arc(ax, O, 36, 0, 90, "fixe", 0.9)
text(ax, O[0] + 18 * math.cos(math.radians(14)), O[1] + 18 * math.sin(math.radians(14)), "40°", "sujet", "s")
text(ax, O[0] + 27 * math.cos(math.radians(68)), O[1] + 27 * math.sin(math.radians(68)), "50°", "autre", "s")
text(ax, O[0] + 41 * math.cos(math.radians(50)), O[1] + 41 * math.sin(math.radians(50)) - 3, "90°", "fixe", "s")
text(ax, 62, 54, "40° + 50° = 90°", "resultat", "m")
save(fig, "26-026")
