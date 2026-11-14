import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 14, 60, r'$z$', 'sujet', 'l', weight='bold'); text(ax, 52, 60, r'$a^2+b^2$', 'varie', 'l', weight='bold')
rows = [(r'$3+4i$', r'$9+16$', '25', 'resultat'), (r'$1+i$', r'$1+1$', '2', 'resultat'),
        (r'$i$', r'$0+1$', '1', 'resultat'), (r'$0$', r'$0+0$', '0', 'fixe')]
for k, (z, s, r, ro) in enumerate(rows):
    y = 44 - k * 13
    box(ax, 2, y, 26, 10, 'sujet', label=z)
    arrow(ax, (29, y + 5), (37, y + 5), 'fixe')
    box(ax, 38, y, 28, 10, 'varie', label=s)
    arrow(ax, (67, y + 5), (72, y + 5), 'fixe')
    box(ax, 73, y, 13, 10, ro, label=r, weight='bold')
save(fig, '75-145')
