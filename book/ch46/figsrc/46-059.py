import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

X0, CW = 22, 5.4
def row(ax, y, members, role, hi=(4,)):
    for h in range(12):
        x = X0 + h * CW
        if h in members: box(ax, x, y, CW - 0.5, 5.5, "sujet" if h in hi else role, r=0.6)
        else: box(ax, x, y, CW - 0.5, 5.5, "fixe", fill=False, lw=0.4, r=0.6)
def header(ax, y):
    for h in range(0, 12, 2): text(ax, X0 + h * CW + (CW - 0.5) / 2, y, str(h), "fixe", "s")
def rlabel(ax, y, s, role): text(ax, X0 - 2, y + 2.75, s, role, "s", ha="right")

fig, ax = canvas(56)
header(ax, 52)
row(ax, 42, {0, 2, 4, 6, 8, 10}, 'sujet', hi=()); rlabel(ax, 42, '{0, 2, …, 10}', 'sujet')
row(ax, 32, {0, 3, 6, 9}, 'autre', hi=()); rlabel(ax, 32, '{0, 3, 6, 9}', 'autre')
for h in (0, 6):
    x = X0 + h * CW + (CW - 0.5) / 2
    line(ax, [(x, 32), (x, 24)], 'resultat', dash=True)
row(ax, 18, {0, 6}, 'resultat', hi=()); rlabel(ax, 18, 'dans les deux', 'resultat')
a = (X0 + 6 * CW + 2.2, 17); b = (X0 + 0 * CW + 2.2, 17)
arrow(ax, a, b, 'varie', curve=-0.5)
text(ax, 44, 4, '6 + 6 = 12, soit 0 : dans la partie', 'varie', 's')
save(fig, '46-059')
