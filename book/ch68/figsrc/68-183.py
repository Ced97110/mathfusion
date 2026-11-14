import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(90)
w = '1100101'
d = w[-1] + w[:-1]
g, xg = '1101000', '0011010'
assert d == '1110010'
assert ''.join(str((int(u) + int(v)) % 2) for u, v in zip(g, xg)) == d
text(ax, 2, 82, 'mot', 'sujet', 's', ha='left')
x1, p = brow(fig, ax, 58, 82, w, roles=['sujet'] * 6 + ['varie'])
text(ax, 2, 66, 'décalé d’un cran', 'resultat', 's', ha='left')
x2, _ = brow(fig, ax, 58, 66, d, roles=['varie'] + ['resultat'] * 6)
arrow(ax, (x1[6], 78.5), (x2[0], 70.5), 'varie', curve=-0.15)
text(ax, 44, 55, r'décalé = $g$ + $x^2 \times g$', 'encre', 'm')
both = [i for i in range(7) if g[i] == '1' and xg[i] == '1']
text(ax, 2, 45, r'$g$', 'fixe', 's', ha='left')
brow(fig, ax, 58, 45, g, roles=['varie' if i in both else 'fixe' for i in range(7)])
text(ax, 2, 33, r'$+\ x^2 \times g$', 'fixe', 's', ha='left')
brow(fig, ax, 58, 33, xg, roles=['varie' if i in both else 'fixe' for i in range(7)])
line(ax, [(2, 26), (86, 26)], 'fixe')
text(ax, 2, 19, '= décalé', 'resultat', 's', ha='left')
brow(fig, ax, 58, 19, d, roles=['varie' if i in both else 'resultat' for i in range(7)])
text(ax, 44, 7, 'multiple de g : dans le code', 'resultat', 'm')
save(fig, '68-183')
