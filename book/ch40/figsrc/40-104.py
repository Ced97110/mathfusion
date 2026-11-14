import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
box(ax, 14, 86, 60, 10, 'sujet', label=r'$r=4\cos\theta+2\sin\theta$', size='m')
steps = [('1. multiplier par r', r'$r^2=4r\cos\theta+2r\sin\theta$', 'sujet'),
         ('2. remplacer', r'$x^2+y^2=4x+2y$', 'sujet'),
         ('3. regrouper', r'$x^2-4x+y^2-2y=0$', 'sujet'),
         ('4. compléter les carrés', r'$(x-2)^2+(y-1)^2=5$', 'sujet'),
         ('5. lire', 'centre (2 ; 1), rayon √5', 'resultat')]
xc = 61
arrow(ax, (44, 86), (xc, 81), 'varie')
for i, (name, eq, role) in enumerate(steps):
    y = 70 - 15 * i
    box(ax, 2, y, 32, 11, 'varie', label=name, size='s')
    box(ax, 38, y, 48, 11, role, label=eq, size='s')
    if i < 4:
        arrow(ax, (xc, y), (xc, y - 4), 'varie')
save(fig, '40-104')
