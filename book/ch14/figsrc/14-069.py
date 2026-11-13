import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
digits = ['0', '0', '0', '0', '5', '9']
x0, cw = 11, 11
bx = lambda k: x0 + k * cw
for i, d in enumerate(digits):
    box(ax, bx(i) + 0.5, 26, cw - 1, 12, 'sujet' if d in '59' else 'fixe', label=d, size='l')
disc(ax, bx(1), 26, 1.1, 'fixe'); disc(ax, bx(5), 26, 1.1, 'resultat')
for k in range(1, 5):
    arrow(ax, (bx(k) + 1, 42), (bx(k + 1) - 1, 42), 'varie', curve=-0.6)
text(ax, 44, 52, '4 rangs vers la droite', 'varie', 'm')
text(ax, 44, 15, r'$0{,}00059=5{,}9\times10^{-4}$', 'resultat', 'l')
text(ax, 44, 7, 'vers la droite : e négatif', 'fixe', 's')
save(fig, '14-069')
