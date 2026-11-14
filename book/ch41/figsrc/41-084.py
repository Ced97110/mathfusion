import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = [('écrire', 'sujet', r'$\langle1-4,\ 3-2\rangle=\langle-3,1\rangle$'),
        ('carrer, ajouter', 'sujet', r'$(-3)^2+1^2=9+1=10$'),
        ('développer', 'varie', r'$(1-4)^2=1-8+16=9$' + '\n' + r'$(3-2)^2=9-12+4=1$'),
        ('regrouper', 'resultat', r'$10+20-2\times10=10$')]
y = 72
for i, (lab, role, expr) in enumerate(rows):
    h = 18 if i == 2 else 12
    y -= h
    box(ax, 28, y, 58, h, role, label=expr, size='s')
    text(ax, 16, y + h / 2, lab, role, 's')
    text(ax, 2.5, y + h / 2, str(i + 1), role, 's')
    if i < 3:
        arrow(ax, (57, y), (57, y - 5), 'fixe')
    y -= 5
save(fig, '41-084')
