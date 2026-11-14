import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 4, 56, 80, 9, 'sujet', label=r'$M(S)$ : les 4 transformations de 2 numéros')
rows = [('resultat', 'parenthèses sans effet', 'exigé'), ('resultat', 'un élément neutre', 'exigé'),
        ('limite', r'$\alpha\circ\beta\neq\beta\circ\alpha$', 'non exigé')]
for i, (role, t, tag) in enumerate(rows):
    y = 40 - i * 14
    box(ax, 4, y, 46, 9, role, label=t, size='s')
    text(ax, 54, y + 4.5, tag, role, 's', ha='left')
    arrow(ax, (10, 56), (10, y + 9), role) if False else None
line(ax, [(2, 56), (2, 6)], 'fixe', lw=0.8) if False else None
save(fig, '44-065')
