import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
rows = [(58, 'fixe', r'$\frac{x}{3}+1$', 'expression : pas de =', 'voisine'),
        (32, 'autre', r'$2x+1=7$', 'équation : rien en bas', 'voisine'),
        (6, 'sujet', r'$\frac{4}{x-1}=\frac{2}{x+6}$', 'x en bas, avec =', '')]
for y, role, expr, lab, _ in rows:
    box(ax, 3, y, 46, 16, role, True, expr)
    text(ax, 52, y + 8, lab, role, 's', ha='left')
save(fig, '21-085')
