import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(50)
f = numberline(ax, 6, 80, 22, 1, 80, step=1, labels=False, arrow_right=False, tick=0.0)
for v in (1, 24, 80):
    disc(ax, f(v), 22, 1.8, 'sujet' if v != 80 else 'resultat')
    text(ax, f(v), 15, 'ch. ' + str(v), 'sujet' if v != 80 else 'resultat', 'm')
arrow(ax, (f(80) - 2, 25), (f(24) + 2, 25), 'varie', curve=0.3)
text(ax, f(52), 42, r'$x-y=0$ et $x-y=-1$ : $0=1$', 'varie', 'm')
text(ax, f(52), 36, 'question restée sans réponse', 'varie', 's')
text(ax, f(80) + 3, 8, 'dernier chapitre', 'resultat', 's', ha='right')
save(fig, '80-465')
