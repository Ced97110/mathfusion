import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
f = numberline(ax, 8, 60, 20, 1, 8, labels=False, arrow_right=False)
for v in range(1, 9):
    text(ax, f(v), 15, str(v), 'fixe', 's')
for v in (1, 2, 4, 8): disc(ax, f(v), 20, 2.2, 'resultat')
disc(ax, f(3), 20, 2.2, 'limite')
line(ax, [(61, 20), (72, 20)], 'limite', dash=True)
disc(ax, 78, 20, 3, 'limite', label='π', size='s')
text(ax, 78, 12, 'degré infini', 'limite', 's')
text(ax, f(3), 29, '∛2 : degré 3', 'limite', 's')
text(ax, 40, 40, 'degrés permis : 1, 2, 4, 8…', 'resultat', 's')
save(fig, '61-158')
