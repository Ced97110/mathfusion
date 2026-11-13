import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
digits = list('29') + ['0'] * 6
x0, cw = 6, 9.5
bx = lambda k: x0 + k * cw
for i, d in enumerate(digits):
    box(ax, bx(i) + 0.5, 22, cw - 1, 12, 'sujet' if i < 2 else 'fixe', label=d, size='l')
disc(ax, bx(1), 22, 1.1, 'fixe'); disc(ax, bx(8), 22, 1.1, 'resultat')
for k in range(1, 8):
    arrow(ax, (bx(k) + 1, 38), (bx(k + 1) - 1, 38), 'varie', curve=-0.6)
text(ax, 44, 48, '7 rangs vers la droite', 'varie', 'm')
text(ax, 44, 13, r'$2{,}9\times10^{7}=29\,000\,000$', 'encre', 'm')
text(ax, 44, 5, r'$e=7$ : l’ordre de grandeur', 'resultat', 'm')
save(fig, '14-073')
