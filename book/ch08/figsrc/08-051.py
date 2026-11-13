import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
for x, a, b, r, t in [(22, '3,2', r'$\frac{32}{10}$', 'sujet', '1 décimale'), (66, '1,46', r'$\frac{146}{100}$', 'autre', '2 décimales')]:
    text(ax, x, 96, a, r, 'xl', weight='bold')
    box(ax, x - 12, 66, 24, 17, r, label=b, size='l')
    arrow(ax, (x, 91), (x, 84), 'fixe')
    text(ax, x, 61, t, r, 's')
text(ax, 44, 74.5, r'$\times$', 'encre', 'xl')
box(ax, 4, 34, 80, 16, 'varie', label=r'$\frac{32}{10}\times\frac{146}{100}=\frac{4\,672}{1\,000}$', size='l')
arrow(ax, (22, 57), (22, 51), 'varie'); arrow(ax, (66, 57), (66, 51), 'varie')
text(ax, 44, 26, r'$10\times100=1\,000$', 'encre', 'm')
for i, d in enumerate('1000'):
    box(ax, 24 + i * 11, 4, 10, 11, ('sujet' if i == 1 else 'autre') if d == '0' else 'fixe', label=d, size='l')
text(ax, 20, 9.5, '1 + 2', 'encre', 's', ha='right')
text(ax, 70, 9.5, '= 3 zéros', 'resultat', 's', ha='left')
save(fig, '08-051')
