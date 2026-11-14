import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'règle : $\deg(fg)=\deg f+\deg g$', 'sujet', 'm')
rows = [(52, 'fixe', r'$f=2x$, $g=3$, $fg=6x$', r'degrés $1+0=1$' + '\n' + 'somme = degré du produit'),
        (32, 'sujet', r'$fg=0$', r'somme $=-\infty$ (degré de 0)' + '\n' + 'l’un des deux est nul'),
        (12, 'sujet', r'$fg=1$', r'somme $=0$ : degrés $0+0$' + '\n' + 'les deux sont constants')]
for y, role, left, right in rows:
    box(ax, 3, y - 6, 34, 12, role, label=left, size='s')
    arrow(ax, (38.5, y), (44, y), 'varie')
    text(ax, 46, y, right, 'resultat', 's', ha='left')
save(fig, '54-139')
