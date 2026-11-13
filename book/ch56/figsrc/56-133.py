import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [(66, 'sujet', 'Départ', r'$I=(6,10)$ idéal non nul', r'on choisit $b=2$, de taille minimale'),
         (38, 'varie', 'Étape : diviser par $b$', r'$10=2\times 5+0$ et $6=2\times 3+0$', r'$r\in I$ et $\delta(r)<\delta(b)$'),
         (10, 'resultat', 'Arrivée', r'$r=0$ : tout $a$ de $I$ est $bq$', r'$I=(2)$')]
for y, role, head, l1, l2 in steps:
    box(ax, 4, y, 80, 20, role)
    text(ax, 8, y + 16, head, role, 's', ha='left', weight='bold')
    text(ax, 44, y + 9.5, l1, role, 'm')
    text(ax, 44, y + 3.8, l2, role, 's')
arrow(ax, (44, 66), (44, 58), 'fixe')
arrow(ax, (44, 38), (44, 30), 'fixe')
save(fig, '56-133')
