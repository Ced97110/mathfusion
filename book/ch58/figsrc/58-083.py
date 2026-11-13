import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 24, 26, 14, 'sujet', label='$v$ = (4, 7)')
rows = [(46, 'resultat', '× 1 : (4, 7)\ninchangé'), (26, 'fixe', '× 2 : (8, 14)'),
        (6, 'limite', '1 ⊛ $v$ : (0, 0)\nproduit inventé')]
for y, role, lab in rows:
    box(ax, 52, y, 34, 14, role, label=lab, size='s')
    arrow(ax, (28, 31), (52, y + 7), role if role != 'fixe' else 'fixe', lw=1.0)
text(ax, 15, 14, 'règle 4 : seul\nle scalaire 1\nne change rien', 'resultat', 's')
save(fig, '58-083')
