import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# (5, 4) ∈ Z^(2) : chaque morceau du signe relié à son sens
parts = [(14, '(5, 4)', 'xl', 'sujet', 'un couple', 60),
         (32, '∈', 'xl', 'encre', 'appartient à', 60),
         (49, r'$\mathbb{Z}$', 'xl', 'autre', 'entiers', 60),
         (59.5, '(2)', 'l', 'varie', '2 cases', 63)]
for x, sym, sz, role, lab, y in parts:
    text(ax, x, y, sym, role, sz, weight='bold' if role != 'encre' else 'normal')
    arrow(ax, (x, y - 4.5), (x, 46), role if role != 'encre' else 'fixe', lw=0.8)
    text(ax, x, 41.5, lab, role, 's')
# deux tailles de listes
text(ax, 2, 22, r'$\mathbb{Z}^{(2)}$', 'varie', 'm', ha='left')
box(ax, 22, 18.5, 7, 7, 'sujet', r=0.5); box(ax, 30, 18.5, 7, 7, 'sujet', r=0.5)
text(ax, 2, 9, r'$\mathbb{Z}^{(3)}$', 'varie', 'm', ha='left')
box(ax, 22, 5.5, 7, 7, 'sujet', r=0.5); box(ax, 30, 5.5, 7, 7, 'sujet', r=0.5); box(ax, 38, 5.5, 7, 7, 'sujet', r=0.5)
text(ax, 52, 22, '2 cases', 'varie', 's', ha='left')
text(ax, 52, 9, '3 cases', 'varie', 's', ha='left')
save(fig, '58-006')
