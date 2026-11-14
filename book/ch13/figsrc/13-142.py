import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 66, 'positifs', 'fixe', 'm'); text(ax, 66, 66, 'négatifs', 'sujet', 'm')
for x, a, b, c, r in [(22, '3 + 5', '5 + 3', '8', 'fixe'), (66, r'$3+(-5)$', r'$(-5)+3$', r'$-2$', 'sujet')]:
    box(ax, x - 16, 48, 32, 10, r, label=a)
    arrow(ax, (x, 47), (x, 38), 'varie', both=True)
    text(ax, x + 2, 42.5, 'échange', 'varie', 's', ha='left')
    box(ax, x - 16, 27, 32, 10, r, label=b)
    arrow(ax, (x, 26), (x, 19), 'resultat')
    box(ax, x - 8, 8, 16, 10, 'resultat', label=c)
text(ax, 44, 3, "l'ordre ne change rien", 'resultat', 's')
save(fig, '13-142')
