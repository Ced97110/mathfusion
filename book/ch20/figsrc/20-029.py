import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(64)
text(ax, 6, 60, r"$<$ : strictement plus petit", "sujet", "s", ha="left")
text(ax, 6, 54, r"$>$ : strictement plus grand", "autre", "s", ha="left")
for y0, expr, role, lab in ((34, r"$3 < 7$", "resultat", "vrai"), (20, r"$7 > 3$", "resultat", "vrai : même fait"), (4, r"$5 < 5$", "limite", "faux : 5 égale 5")):
    box(ax, 6, y0, 28, 11, role, label=expr, size="l")
    text(ax, 40, y0 + 5.5, lab, role, "s", ha="left")
save(fig, "20-029")
