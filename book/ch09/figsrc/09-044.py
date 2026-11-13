import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(44, 'sujet', r'$\frac{3}{4}$', 'rapport : un nombre', 'ni vrai ni faux'),
        (24, 'resultat', r'$\frac{3}{4} = \frac{6}{8}$', 'proportion vraie', '0,75 et 0,75'),
        (4, 'limite', r'$\frac{3}{4} = \frac{6}{9}$', 'proportion fausse', '0,75 et 0,67')]
for y, role, f, a, b in rows:
    box(ax, 3, y, 38, 15, role, label=f, size='xl')
    text(ax, 46, y + 10, a, role, 's', ha='left', weight='bold')
    text(ax, 46, y + 4.5, b, 'fixe', 's', ha='left')
save(fig, '09-044')
