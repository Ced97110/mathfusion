import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
f = lambda v: 14 + v * 2.2
box(ax, 4, 84, 80, 10, 'sujet', label=r'Départ : $p = 5$ irréductible, (5) maximal', size='s')
arrow(ax, (44, 84), (44, 77), 'fixe')
box(ax, 4, 67, 80, 10, 'varie', label='chapitre 52 : maximal ⇒ premier', size='s')
arrow(ax, (44, 67), (44, 60), 'fixe')
box(ax, 4, 50, 80, 10, 'resultat', label=r'$ab \in (5) \Rightarrow a \in (5)$ ou $b \in (5)$', size='s')
y = 24
text(ax, 2, y, '(5)', 'autre', 's', ha='left')
for v in range(0, 31, 5):
    disc(ax, f(v), y, 1.1, 'resultat' if v == 10 else 'varie' if v == 30 else 'autre')
disc(ax, f(3), y, 1.1, 'limite', fill=False)
text(ax, f(3), y - 6, r'$a = 3 \notin (5)$', 'limite', 's')
text(ax, f(10), y + 6, r'$b = 10 \in (5)$', 'resultat', 's')
text(ax, f(30) - 6, y - 6, r'$ab = 30 \in (5)$', 'varie', 's')
save(fig, '56-116')
