import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$Y=\{2,3,4,6\}$', 'varie', 'm')
for xc, n, role, t in [(15, 8, 'limite', '3 ne divise\npas 8'), (44, 12, 'resultat', 'multiple de\n2, 3, 4 et 6'), (73, 24, 'resultat', 'multiple de\n2, 3, 4 et 6')]:
    box(ax, xc - 10, 36, 20, 12, role, label=str(n), size='l', lw=1.8 if n == 12 else 0.8)
    text(ax, xc, 28, t, role, 's')
arrow(ax, (44, 21), (44, 14), 'resultat')
text(ax, 44, 8, r'$\sup Y=12=\mathrm{PPCM}(2,3,4,6)$', 'resultat', 'm')
save(fig, '79-195')
