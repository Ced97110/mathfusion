import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cx(i): return 7 + i * 12.5
def row(y, items):
    for i, (t, k, r) in enumerate(items):
        if k == "box": box(ax, cx(i) - 5, y, 10, 10, r, label=t, size="l")
        else: text(ax, cx(i), y + 5, t, r, "l")
X = (r"$x$", "txt", "encre"); Y = (r"$y$", "txt", "encre"); P = ("+", "txt", "encre")
fig, ax = canvas(66)
text(ax, 44, 62, "le cas chiffré", "fixe", "s")
row(44, [("1", "txt", "varie"), X, P, ("2", "box", "sujet"), Y, (r"$>$", "box", "fixe"), ("5", "box", "sujet")])
box(ax, cx(0) - 5, 44, 10, 10, "varie", fill=False, dash=True)
row(14, [(r"$a$", "box", "sujet"), X, P, (r"$b$", "box", "sujet"), Y, (r"$>$", "box", "fixe"), (r"$c$", "box", "sujet")])
text(ax, 44, 6, "la forme", "fixe", "s")
for i in (0, 3, 6):
    arrow(ax, (cx(i), 43), (cx(i), 25.5), "varie")
line(ax, [(cx(5), 43), (cx(5), 25.5)], "fixe", dash=True)
text(ax, cx(0) + 1.5, 38, "1 : non écrit", "varie", "s", ha="left")
text(ax, cx(5) - 1.5, 32, "même signe", "fixe", "s", ha="right")
save(fig, "20-024")
