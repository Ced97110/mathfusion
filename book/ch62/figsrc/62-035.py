import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 2, 18, 84, 46, 'sujet')
text(ax, 44, 59, r'$F[x]$ avec $F=\mathbb{Q}$', 'sujet', 'l')
for i, l in enumerate([r'$x^2-2$', r'$3x+\frac{1}{2}$', r'$7$']):
    box(ax, 5 + i * 27.5, 24, 24, 17, 'encre', label=l)
arrow(ax, (44, 23), (44, 14), 'varie')
text(ax, 44, 9, r'$f\in F[x]$', 'resultat', 'l')
text(ax, 44, 2.5, r'$f$ : coefficients dans $F$', 'fixe', 's')
save(fig, '62-035')
