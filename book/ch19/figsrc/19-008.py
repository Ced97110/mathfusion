import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x0, role, a, b, f, v in [(2, 'resultat', 2, 5, r'$2\times2+1=5$', 'vrai'), (47, 'limite', 5, 2, r'$2\times5+1=11$', 'faux')]:
    text(ax, x0 + 19, 50, v, role, 'l', weight='bold')
    box(ax, x0, 33, 38, 12, role, label=f'({a}, {b})', size='l')
    text(ax, x0 + 9.5, 27, f'{a} cahiers', 'sujet', 's'); text(ax, x0 + 28.5, 27, f'{b} euros', 'varie', 's')
    text(ax, x0 + 19, 17, f, 'encre', 's')
text(ax, 66, 8, r'11 $\neq$ 2', 'limite', 'm')
text(ax, 21, 8, r'5 = 5', 'resultat', 'm')
save(fig, '19-008')
