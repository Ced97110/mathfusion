import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(52)
text(ax, 2, 47, 'f : score de chaque élève', 'sujet', 's', ha='left')
for i, v in enumerate(['5', '7', '2']):
    x = 8 + 26 * i
    box(ax, x, 31, 20, 10, 'sujet', label=v, size='l')
    arrow(ax, (x + 10, 31), (x + 10, 22), 'varie', both=True)
    box(ax, x, 12, 20, 10, 'resultat', label=v, size='l')
text(ax, 2, 5.5, 'g : somme partielle', 'resultat', 's', ha='left')
text(ax, 86, 5.5, r"$\mu(x,x)=1$ : rien à défaire", 'encre', 's', ha='right')
save(fig, '80-416')
