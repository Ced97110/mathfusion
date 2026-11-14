import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def row(y, role, steps, end, lab):
    f = numberline(ax, 14, 54, y, 0, 2, 1, arrow_right=False, role='fixe')
    text(ax, 4, y + 17, lab, role, 's', ha='left')
    for (a, b, t) in steps:
        if b > a: c, ty = -0.6, y + 8
        elif b < a: c, ty = 1.0, y + 12
        else: c, ty = -1.6, y + 8
        arrow(ax, (f(a) - (2 if a == b else 0), y + 3), (f(b) + (2 if a == b else 0), y + 3), 'varie', curve=c)
        text(ax, (f(a) + f(b)) / 2 if a != b else f(a) - 7, ty, t, 'varie', 's')
    text(ax, 74, y, end, role, 's')
row(62, 'resultat', [(0, 1, '+1'), (1, 0, '−1')], r'retour à 0', 'ajouter 1, puis retirer 1')
row(26, 'limite', [(0, 0, '−1'), (0, 1, '+1')], r'arrive en 1', 'retirer 1, puis ajouter 1')
save(fig, '44-095')
