import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, cw = 23, 14
bx = lambda k: x0 + k * cw
for i, d in enumerate('981'):
    box(ax, bx(i) + 0.5, 22, cw - 1, 12, 'sujet', label=d, size='l')
disc(ax, bx(3), 22, 1.1, 'fixe'); disc(ax, bx(1), 22, 1.1, 'resultat')
for k in (3, 2):
    arrow(ax, (bx(k) - 1, 38), (bx(k - 1) + 1, 38), 'varie', curve=0.6)
text(ax, 44, 48, '2 pas vers la gauche', 'varie', 'm')
text(ax, 44, 12, r'$9{,}81\times10^{2}$', 'resultat', 'l')
text(ax, 44, 4, r'à gauche : $e$ positif', 'fixe', 's')
save(fig, '14-076')
