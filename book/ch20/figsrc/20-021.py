import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(66)
text(ax, 44, 62, "boulangerie", "fixe", "s")
row(44, [("2", "box", "sujet"), X, P, ("3", "box", "sujet"), Y, (r"$\leq$", "box", "fixe"), ("12", "box", "sujet")])
brace(ax, cx(0) - 5, cx(4) + 5, 43, "sujet", label="un nombre fixé par inconnue")
text(ax, 44, 26, "le second dépasse le premier plus 1", "fixe", "s")
row(7, [(r"$-1$", "box", "sujet"), X, P, ("1", "box", "sujet"), Y, (r"$>$", "box", "fixe"), ("1", "box", "sujet")])
save(fig, "20-021")
