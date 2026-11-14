import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(66)
text(ax, 44, 62, "boulangerie : mêmes nombres", "fixe", "s")
row(40, [("2", "box", "sujet"), X, P, ("3", "box", "sujet"), Y, (r"$\leq$", "box", "fixe"), ("12", "box", "sujet")])
row(12, [("2", "box", "sujet"), X, P, ("3", "box", "sujet"), Y, (r"$\geq$", "box", "varie"), ("12", "box", "sujet")])
text(ax, cx(5), 56, "au plus", "fixe", "s")
text(ax, cx(5), 8, "au moins", "varie", "s")
arrow(ax, (cx(5), 39), (cx(5), 23.5), "varie")
text(ax, cx(5) - 1.5, 31.5, "sens inversé", "varie", "s", ha="right")
save(fig, "20-025")
