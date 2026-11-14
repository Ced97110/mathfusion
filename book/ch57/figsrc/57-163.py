import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 20, 75, 'coefficients  R', 'fixe', 's', weight='bold')
text(ax, 64, 75, 'module  Rx,  x = (2 ; 1)', 'sujet', 's', weight='bold')
rows = [(62, 'a = 3', r'$(6\,;\,3)$', 'sujet'), (47, 'b = 2', r'$(4\,;\,2)$', 'sujet'),
        (30, '3 + 2 = 5', r'$(6\,;\,3)+(4\,;\,2)=(10\,;\,5)$', 'resultat'), (12, '7', r'$(14\,;\,7)$', 'resultat')]
for y, l, r, role in rows:
    box(ax, 3, y - 5, 28, 10, 'varie' if role == 'sujet' else 'resultat', label=l, size='s')
    box(ax, 40, y - 5, 45, 10, role, label=r, size='s')
    arrow(ax, (31.5, y), (39.5, y), 'varie', lw=1.1)
text(ax, 35.5, 69, r'$\mu_x$', 'varie', 's')
line(ax, [(3, 21), (85, 21)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 4, 'tout multiple de x est atteint', 'resultat', 's')
save(fig, '57-163')
