import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def matrix(cx, cy, vals, role):
    for k, v in enumerate(vals):
        text(ax, cx + (-4.5 if k % 2 == 0 else 4.5), cy + (3.8 if k < 2 else -3.8), v, role, 'l')
    for s in (-1, 1):
        x = cx + s * 11
        line(ax, [(x - s * 2, cy + 9), (x, cy + 9), (x, cy - 9), (x - s * 2, cy - 9)], role, lw=1.0)
matrix(20, 46, ['2', '0', '0', '3'], 'sujet')
matrix(68, 46, ['2', '0', '1', '3'], 'autre')
arrow(ax, (34, 42), (54, 42), 'resultat', both=True)
text(ax, 44, 51, 'même\ntransformation', 'resultat', 's')
arrow(ax, (10, 14), (30, 14), 'sujet'); arrow(ax, (20, 6), (20, 26), 'sujet')
arrow(ax, (58, 14), (78, 14), 'autre'); arrow(ax, (64, 6), (72, 26), 'autre')
text(ax, 20, 31, 'repère 1', 'sujet', 's'); text(ax, 68, 31, 'repère 2', 'autre', 's')
save(fig, '60-013')
