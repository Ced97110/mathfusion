import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(66)
XV = (r"$x$", "txt", "varie"); YV = (r"$y$", "txt", "varie")
text(ax, cx(0), 60, r"$a$", "sujet", "l"); text(ax, cx(3), 60, r"$b$", "sujet", "l")
arrow(ax, (cx(0), 57.5), (cx(0), 49.5), "sujet"); arrow(ax, (cx(3), 57.5), (cx(3), 49.5), "sujet")
row(38, [("2", "box", "sujet"), XV, P, ("3", "box", "sujet"), YV])
row(20, [("3", "box", "sujet"), XV, P, ("2", "box", "sujet"), YV])
text(ax, 22, 8, "coefficients : fixés", "sujet", "s")
text(ax, 66, 8, r"$x$, $y$ : varient", "varie", "s")
save(fig, "20-027")
