import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, lab, cap in [(50, r'$\sqrt{5}$', 'ne rien changer'), (30, r'$-\sqrt{5}$', r'$\sqrt{5}$ devient $-\sqrt{5}$')]:
    disc(ax, 10, y, 5, 'sujet', label=r'$\sqrt{5}$', size='s')
    arrow(ax, (16, y), (34, y), 'varie')
    text(ax, 25, y + 4.5, cap, 'varie', 's')
    disc(ax, 40, y, 5, 'sujet' if y == 50 else 'autre', label=lab, size='s')
    line(ax, [(46, y), (58, 40)], 'resultat', lw=0.7)
box(ax, 58, 28, 28, 24, 'resultat', label=r'$\mathrm{Gal}(E/F)$' + '\n2 éléments', size='s')
box(ax, 4, 8, 50, 10, 'fixe', label='fractions : elles ne bougent pas', size='s')
save(fig, '64-058')
