import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(64)
SX, SY = 10, 4
def graph(ox, oy, f, role, title, foot, labels):
    line(ax, [(ox, oy), (ox + 3 * SX + 4, oy)], "fixe"); line(ax, [(ox, oy), (ox, oy + 9 * SY + 3)], "fixe")
    pts = [(ox + i * SX, oy + f(i) * SY) for i in range(4)]
    xs = [ox + t / 20 * 3 * SX for t in range(21)]
    line(ax, [(x, oy + f((x - ox) / SX) * SY) for x in xs], role, lw=1.3)
    for i in range(3):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        line(ax, [(x0, y0), (x1, y0), (x1, y1)], "varie", lw=0.8, dash=True)
        if labels: text(ax, x1 + 1.5, (y0 + y1) / 2, labels[i], "varie", "s", ha="left")
    for (x, y) in pts: disc(ax, x, y, 1.0, role)
    text(ax, ox + 15, 57, title, role, "m"); text(ax, ox + 15, 3, foot, "varie", "s")
graph(5, 10, lambda t: 3 * t, "sujet", "droite", "accroissement constant", None)
graph(49, 10, lambda t: t * t, "autre", "courbe", "accroissement qui change", ["+1", "+3", "+5"])
save(fig, "20-032")
