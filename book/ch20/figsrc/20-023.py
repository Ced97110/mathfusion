import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(80)
le = (r"$\leq$", "box", "fixe")
row(60, [(r"$a$", "box", "sujet"), X, P, (r"$b$", "box", "sujet"), Y, le, (r"$c$", "box", "sujet")])
text(ax, 44, 74, "même structure, autres nombres", "fixe", "s")
row(34, [("2", "box", "sujet"), X, P, ("3", "box", "sujet"), Y, le, ("12", "box", "sujet")])
row(8, [("5", "box", "sujet"), X, P, ("1", "box", "sujet"), Y, le, ("7", "box", "sujet")])
text(ax, 44, 55, "lettres", "fixe", "s") if False else None
for i in (0, 3, 6):
    arrow(ax, (cx(i), 59), (cx(i), 46.5), "varie")
line(ax, [(cx(5), 59), (cx(5), 46.5)], "fixe", dash=True)
text(ax, cx(5) - 1.5, 52, "≤ reste", "fixe", "s", ha="right")
for i in (0, 3, 6):
    arrow(ax, (cx(i), 33), (cx(i), 19.5), "varie")
line(ax, [(cx(5), 33), (cx(5), 19.5)], "fixe", dash=True)
save(fig, "20-023")
