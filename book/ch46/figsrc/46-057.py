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
header(ax, 51)
row(ax, 41, {4}, 'sujet'); rlabel(ax, 41, 'X = {4}', 'sujet')
row(ax, 31, {0, 4, 8}, 'autre'); rlabel(ax, 31, '{0, 4, 8}', 'autre')
row(ax, 21, {0, 2, 4, 6, 8, 10}, 'autre'); rlabel(ax, 21, '{0, 2, …, 10}', 'autre')
row(ax, 11, set(range(12)), 'autre'); rlabel(ax, 11, 'horloge entière', 'autre')
text(ax, 44, 4, 'lequel est le plus petit ?', 'varie', 'm', weight='bold')
text(ax, 3, 36.5, '', 'fixe', 's')
save(fig, '46-057')
