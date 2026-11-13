import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 80, 'N engendré par', 'fixe', 'm', weight='bold')
text(ax, 65, 80, 'partie finie du quotient', 'fixe', 'm', weight='bold')
rows = [(66, '(2 ; 0)', 'resultat', 'ℤ/2ℤ : horloge à 2'),
        (52, '(3 ; 0)', 'resultat', 'ℤ/3ℤ : horloge à 3'),
        (38, '(2 ; 1)', 'fixe', 'aucune horloge')]
for cy, gen, role, res in rows:
    box(ax, 6, cy - 4.5, 32, 9, 'sujet', label=gen)
    arrow(ax, (38.5, cy), (45.5, cy), 'fixe')
    box(ax, 46, cy - 4.5, 40, 9, role, label=res)
text(ax, 44, 27, 'que lire dans le couple ?', 'varie', 'm', weight='bold')
box(ax, 6, 8, 38, 12, 'varie', dash=True, label='quelle règle ?')
box(ax, 48, 8, 38, 12, 'autre', dash=True, label='avec deux couples ?')
save(fig, '57-228')
