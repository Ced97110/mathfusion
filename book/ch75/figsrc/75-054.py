import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for k, (a, b) in enumerate([(r'$x$', r'$\eta x$'), (r'$y$', r'$\eta y$')]):
    y = 40 - k * 12
    disc(ax, 14, y, 4.5, 'sujet', label=a)
    disc(ax, 74, y, 5.5, 'varie', label=b)
    arrow(ax, (19, y), (68, y), 'varie')
    text(ax, 44, y + 3.5, r'$\eta$', 'varie', 's')
text(ax, 44, 57, r'$\eta$ : linéaire et bijective', 'varie', 's', weight='bold')
text(ax, 14, 49, 'flèches', 'sujet', 's')
text(ax, 74, 49, 'images', 'varie', 's')
line(ax, [(2, 21), (86, 21)], 'fixe', dash=True)
box(ax, 14, 4, 60, 9, 'fixe', fill=False, dash=True, label=r'$B(\eta x,\eta y)=B(x,y)$')
text(ax, 44, 16.5, r'condition, vraie pour certains $\eta$', 'fixe', 's')
save(fig, '75-054')
