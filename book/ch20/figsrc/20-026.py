import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(58)
text(ax, 14, 52, "boulangerie", "fixe", "s")
text(ax, 44, 52, "inconnues", "sujet", "s")
text(ax, 74, 52, "exemple", "fixe", "s")
for y0, sym, a, b in ((30, r"$x$", "pains", "premier nombre"), (8, r"$y$", "gâteaux", "second nombre")):
    box(ax, 36, y0, 16, 12, "sujet", label=sym, size="xl")
    box(ax, 2, y0, 26, 12, "varie", label=a)
    box(ax, 60, y0, 26, 12, "varie", label=b)
    arrow(ax, (35.5, y0 + 6), (28.5, y0 + 6), "varie")
    arrow(ax, (52.5, y0 + 6), (59.5, y0 + 6), "varie")
save(fig, "20-026")
