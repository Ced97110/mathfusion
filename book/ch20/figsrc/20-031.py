import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(62)
rows = [(44, r"$2x + 3y \leq 12$", "sujet", "linéaire", "resultat"),
        (24, r"$x^2 + y \leq 4$", "autre", "x au carré : exposant", "autre"),
        (4, r"$xy > 1$", "autre", "x fois y : produit", "autre")]
for y0, expr, role, lab, lr in rows:
    box(ax, 3, y0, 36, 14, role, label=expr, size="l")
    text(ax, 45, y0 + 7, lab, lr, "s", ha="left")
save(fig, "20-031")
