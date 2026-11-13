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
row(ax, 42, {0, 4, 8}, 'autre'); rlabel(ax, 42, '{0, 4, 8}', 'autre')
row(ax, 32, {0, 2, 4, 6, 8, 10}, 'autre'); rlabel(ax, 32, '{0, 2, …, 10}', 'autre')
row(ax, 22, set(range(12)), 'autre'); rlabel(ax, 22, 'horloge entière', 'autre')
for h in (0, 4, 8):
    x = X0 + h * CW + (CW - 0.5) / 2
    line(ax, [(x, 22), (x, 14)], 'resultat', dash=True)
row(ax, 8, {0, 4, 8}, 'resultat', hi=()); rlabel(ax, 8, 'dans les trois', 'resultat')
text(ax, 44, 2.4, '', 'fixe', 's')
save(fig, '46-058')
