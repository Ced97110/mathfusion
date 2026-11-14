import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(74)
box(ax, 3, 56, 34, 11, "sujet", label="plus petit que 12")
text(ax, 44, 61.5, "ou", "encre", "m")
box(ax, 51, 56, 34, 11, "varie", label="égal à 12")
arrow(ax, (44, 55), (44, 45.5), "varie")
box(ax, 28, 33, 32, 11, "resultat", label=r"$\leq$ 12", size="l")
box(ax, 6, 4, 34, 11, "resultat", label=r"$5 \leq 5$ vrai")
box(ax, 48, 4, 34, 11, "limite", label=r"$5 < 5$ faux")
arrow(ax, (44, 32), (23, 16.5), "fixe")
save(fig, "20-030")
