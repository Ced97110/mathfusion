import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
box(ax, 2, 14, 22, 26, 'sujet', label=r'$\alpha$', size='xl'); text(ax, 13, 9, 'angle principal', 'sujet', 's')
text(ax, 37.5, 45, 'hauteur', 'fixe', 's'); text(ax, 56.5, 45, r'$\alpha$', 'sujet', 'm'); text(ax, 75.5, 45, r'$180°-\alpha$', 'resultat', 's')
rows = [(28, '0,5', '30°', '150°'), (14, '0,4', '23,58°', '156,42°')]
for y, h, a, b in rows:
    box(ax, 29, y, 17, 11, 'fixe', label=h); box(ax, 48, y, 17, 11, 'sujet', label=a); box(ax, 67, y, 17, 11, 'resultat', label=b)
save(fig, '32-031')
