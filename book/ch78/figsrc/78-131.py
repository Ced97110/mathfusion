import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 3, 62, 38, 10, 'sujet', label=r'$x=(1,1,1,1)$')
box(ax, 47, 62, 38, 10, 'autre', label=r'$y=(2,1,1,1)$')
rows = [(r'$z_1=x_1y_1-x_2y_2-x_3y_3-x_4y_4$', '−1', 'varie'),
        (r'$z_2=x_1y_2+x_2y_1+x_3y_4-x_4y_3$', '3', 'fixe'),
        (r'$z_3=x_1y_3-x_2y_4+x_3y_1+x_4y_2$', '3', 'fixe'),
        (r'$z_4=x_1y_4+x_2y_3-x_3y_2+x_4y_1$', '3', 'fixe')]
for i, (f, v, role) in enumerate(rows):
    y = 46 - i * 13
    box(ax, 3, y, 60, 9, role, label=f, size='s', fill=(i == 0))
    text(ax, 67, y + 4.5, '=', 'encre', 'm')
    box(ax, 71, y, 14, 9, 'resultat', label=v)
save(fig, '78-131')
