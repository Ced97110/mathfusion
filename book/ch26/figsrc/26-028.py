import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for x0, h, c1, c2 in ((2, "A = 30°", "cos 60° = 0,5", "sin 30° = 0,5"), (46, "A = 20°", "cos 70° ≈ 0,3420", "sin 20° ≈ 0,3420")):
    box(ax, x0, 52, 40, 10, "varie", label=h, size="m")
    box(ax, x0, 34, 40, 10, "sujet", label=c1, size="s")
    box(ax, x0, 18, 40, 10, "autre", label=c2, size="s")
    arrow(ax, (x0 + 20, 52), (x0 + 20, 44.5), "fixe")
    text(ax, x0 + 20, 31, "=", "resultat", "l", weight="bold")
box(ax, 2, 2, 84, 10, "resultat", label="cos(90° − A) = sin A", size="m")
save(fig, "26-028")
