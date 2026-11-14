import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(42, 'degré 2', [('racine carrée', 'sujet')]),
        (24, 'degré 3', [('racine carrée', 'sujet'), ('racine cubique', 'varie')])]
for y, name, chips in rows:
    text(ax, 2, y + 5, name, 'encre', 'm', ha='left', weight='bold')
    for i, (lab, role) in enumerate(chips):
        x = 32 + i * 28
        box(ax, x, y, 25, 10, role, label=lab, size='s')
        if i > 0: arrow(ax, (x - 2.8, y + 5), (x - 0.4, y + 5), 'fixe')
text(ax, 2, 20, 'Cardan, XVIe siècle', 'fixe', 's', ha='left')
text(ax, 44, 8, r'$\sqrt[3]{8}=2$, car 2 × 2 × 2 = 8', 'varie', 's')
text(ax, 44, 54, 'formules par racines', 'fixe', 's')
save(fig, '64-003')
