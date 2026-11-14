import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 71, 'Écrit : trois termes', 'limite', 's')
terms = [(4, r'$3x^2$', 'varie'), (32, r'$5x$', 'sujet'), (60, r'$-3x^2$', 'varie')]
for x, t, r in terms:
    box(ax, x, 52, 24, 13, r, label=t, size='l')
arrow(ax, (16, 51), (30, 48.5), 'varie')
arrow(ax, (72, 51), (58, 48.5), 'varie')
text(ax, 44, 61.5, '', 'varie', 's')
text(ax, 44, 45, r'$3 - 3 = 0$ : ils s’annulent', 'varie', 's')
arrow(ax, (44, 42), (44, 33), 'resultat')
box(ax, 26, 18, 36, 13, 'resultat', label=r'$5x$', size='l')
text(ax, 44, 12, 'regroupé : degré 1', 'resultat', 'm')
text(ax, 44, 4, r'pour $x=10$ : 50 des deux côtés', 'fixe', 's')
save(fig, '15-131')
