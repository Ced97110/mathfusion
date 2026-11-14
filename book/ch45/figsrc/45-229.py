import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
items = [('départ', 'sujet', r'on suppose $\eta:\mathbb{Z}/4\to$ rectangle'),
         ('calcul', 'fixe', r'$\eta(2)=\eta(1+1)=\eta(1)^2$'),
         ('étape clé', 'varie', r'$\eta(1)^2=e$ (carré = neutre)'),
         ('arrivée', 'limite', r'$\eta(2)=e=\eta(0)$, mais $2\neq0$')]
ys = [70, 52, 34, 16]
for (lab, role, eq), y in zip(items, ys):
    text(ax, 2, y + 6, lab, role, 's', ha='left', weight='bold')
    box(ax, 2, y - 3, 84, 8, role, label=eq, size='m', lw=1.6 if role == 'varie' else 0.8)
for y in ys[:-1]:
    arrow(ax, (44, y - 3), (44, y - 9), 'fixe')
text(ax, 44, 4, 'contradiction avec l’injectivité', 'limite', 'm', weight='bold')
save(fig, '45-229')
