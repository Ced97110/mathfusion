import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 80, r'polynômes qui annulent $\sqrt{2}$', 'encre', 'm')
rows = [(60, r'$x^2-2$', 2, 'sujet'), (40, r'$x^3-2x$', 3, 'fixe'), (20, r'$x^4-4$', 4, 'fixe')]
for y, p, d, role in rows:
    box(ax, 2, y, 30, 12, role, label=p)
    box(ax, 38, y + 2, 11 * d, 8, role, label=f'degré {d}')
text(ax, 74, 66, 'minimal', 'sujet', 'm')
text(ax, 44, 8, 'choix : le plus petit degré', 'sujet', 's')
save(fig, '54-188')
