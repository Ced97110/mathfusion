import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert (2 + 3, 2 * 3) == (5, 6)
fig, ax = canvas(70)
disc(ax, 10, 58, 4.4, 'sujet', label='2', size='m')
text(ax, 20, 58, '+', 'fixe', 'l')
disc(ax, 30, 58, 4.4, 'sujet', label='3', size='m')
arrow(ax, (36, 58), (50, 58), 'varie', lw=1.0)
box(ax, 52, 52, 34, 12, 'sujet', label=r'$a_1=2+3=5$', size='s', weight='bold')
text(ax, 44, 70, 'racines 2 et 3', 'fixe', 's') if False else None
text(ax, 44, 44, r'$(x-2)(x-3)$ développé :', 'fixe', 's')
labs = ['$x^2$', '−5x', '+ 6']
for k, (w, l) in enumerate(zip([20, 24, 20], labs)):
    x = [6, 30, 58][k]
    box(ax, x, 22, w if k != 2 else 20, 14, 'varie' if k == 1 else 'fixe', label=l, size='m', weight='bold' if k == 1 else 'normal')
arrow(ax, (68, 52), (44, 37.5), 'sujet', lw=0.0) if False else None
text(ax, 42, 15, r'coefficient de $x$ : $-a_1=-5$', 'varie', 's')
text(ax, 44, 7, 'a₁ sans signe : la somme 5', 'sujet', 's')
save(fig, '65-046')
