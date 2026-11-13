import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 5.6; ox, oy = 6, 22
P = lambda x, y: (ox + x * s, oy + y * s)
ker = [(0, 0), (2, 1), (4, 2), (6, 3)]
line(ax, [P(0, 0), P(6.6, 3.3)], 'sujet', lw=0.9, dash=True)
for x in range(8):
    for y in range(4):
        if (x, y) not in ker: disc(ax, *P(x, y), 0.8, 'fixe')
for (x, y) in ker: disc(ax, *P(x, y), 1.4, 'sujet')
disc(ax, *P(6, 3), 1.9, 'resultat', fill=False, lw=1.2)
arrow(ax, (P(2, 1)[0] - 1, P(2, 1)[1] + 2), (P(6, 3)[0] - 1.5, P(6, 3)[1] + 2.5), 'varie', lw=1.1, curve=0.3)
text(ax, 32, 46, r'$\times 3$', 'varie', 'm')
text(ax, P(2, 1)[0], P(2, 1)[1] - 4, r'$(2\,;\,1)$', 'sujet', 's')
text(ax, P(4, 2)[0], P(4, 2)[1] - 4, r'$(4\,;\,2)$', 'sujet', 's')
text(ax, P(6, 3)[0] + 1, P(6, 3)[1] + 6.5, r'$(6\,;\,3)$', 'resultat', 's')
text(ax, 22, 60, 'départ : couples', 'encre', 'm', weight='bold')
box(ax, 4, 3, 80, 10, 'resultat', label=r'$\eta(6\,;\,3) = 6 - 6 = 0$ : dans le noyau', size='s')
text(ax, 66, 57, '3 × (2 ; 1) = (6 ; 3)', 'varie', 's')
text(ax, 66, 52.5, '(2 ; 1) + (4 ; 2) = (6 ; 3)', 'sujet', 's')
save(fig, '57-153')
