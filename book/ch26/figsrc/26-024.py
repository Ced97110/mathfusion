import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, "CAH – SOH – TOA", "encre", "l", weight="bold")
rows = (("C = cosinus", "A = adjacent", "H = hypoténuse"),
        ("S = sinus", "O = opposé", "H = hypoténuse"),
        ("T = tangente", "O = opposé", "A = adjacent"))
for i, row in enumerate(rows):
    y = 38 - i * 15
    for j, (lab, role) in enumerate(zip(row, ("sujet", "varie", "fixe"))):
        box(ax, 2 + j * 30, y, 26 if j < 2 else 26, 11, role, label=lab, size="s")
    text(ax, 29, y + 5.5, "÷", "encre", "m") if False else None
save(fig, "26-024")
