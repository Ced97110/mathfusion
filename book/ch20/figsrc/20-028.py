import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(62)
box(ax, 34, 42, 20, 14, "sujet", label=r"$c$", size="xl")
text(ax, 62, 49, "nombre de droite", "sujet", "s", ha="left")
for x0, v, lab, sx in ((6, "12", "boulangerie", 38), (50, "20", "autre problème", 50)):
    arrow(ax, (sx, 42), (x0 + 16, 29.5), "varie")
    box(ax, x0, 18, 32, 11, "varie", label=f"{v} euros")
    text(ax, x0 + 16, 12, lab, "varie", "s")
save(fig, "20-028")
