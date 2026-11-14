import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cw, x0 = 7.2, 30
def row(y, s, roles):
    for i, c in enumerate(s):
        box(ax, x0 + i * cw, y, cw, 6.5, roles[i], label=c, r=0.5)
a, b = '1110000', '1101001'
s = ''.join(str((int(p) + int(q)) % 2) for p, q in zip(a, b))
assert s == '0011001'
box(ax, 2, 56, 84, 11, 'sujet', label=r'$m = 1001$ : les 1 désignent les colonnes 1 et 4', size='s')
arrow(ax, (44, 55.5), (44, 49.5), 'varie')
row(42, a, ['fixe'] * 7)
row(32, b, ['fixe'] * 7)
box(ax, x0 - 0.6, 30.8, 2 * cw + 1.2, 19.4, 'varie', fill=False, lw=0.9, r=0.5)
text(ax, 2, 45, 'colonne 1', 'fixe', 's', ha='left')
text(ax, 2, 35, 'colonne 4', 'fixe', 's', ha='left')
text(ax, 25, 35, '+', 'encre', 'l')
line(ax, [(x0 - 2, 29), (x0 + 7 * cw + 2, 29)], 'encre', lw=1.0)
row(20, s, ['resultat'] * 7)
text(ax, 2, 23, 'somme', 'resultat', 's', ha='left')
text(ax, 44, 11, '1 + 1 = 0 aux positions 1 et 2', 'varie', 's')
text(ax, 44, 4, 'somme = mot envoyé de $m$', 'resultat', 's')
save(fig, '68-135')
