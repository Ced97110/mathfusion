import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 22, 70, 'forme', 'fixe', 's'); text(ax, 68, 70, 'on y lit', 'fixe', 's')
rows = [(52, 'autre', 'pente-ordonnée', r'$y=mx+b$', 'la pente m, le nombre b'),
        (30, 'sujet', 'point-pente', r'$y-y_1=m(x-x_1)$', 'la pente m, un point'),
        (8, 'fixe', 'forme générale', None, 'rien directement')]
for y, role, name, f, lit in rows:
    box(ax, 2, y, 48, 16, role)
    text(ax, 26, y + 11.5, name, role, 's', weight='bold')
    if f: text(ax, 26, y + 5, f, role, 'm')
    arrow(ax, (51, y + 8), (55, y + 8), role)
    text(ax, 69, y + 8, lit, role, 's')
save(fig, '19-101')
