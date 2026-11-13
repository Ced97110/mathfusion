import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
text(ax, 4, 87, r'$\sqrt{-12}$', 'sujet', 'l', ha='left')
box(ax, 2, 62, 44, 14, 'varie', label='1. sortir le signe' + '\n' + r'$-12=12\times(-1)$, $\sqrt{-1}=i$', size='s')
box(ax, 2, 40, 44, 16, 'autre', label='2. simplifier' + '\n' + r'$12=4\times 3$, $\sqrt{12}=2\sqrt{3}$', size='s')
box(ax, 2, 16, 44, 18, 'resultat', label='3. contrôler' + '\n' + r'$(2\sqrt{3}\,i)^2=4\times 3\times i^2$' + '\n' + r'$=-12$', size='s')
arrow(ax, (24, 62), (24, 57), 'varie', lw=1.0)
arrow(ax, (24, 40), (24, 35), 'varie', lw=1.0)
text(ax, 24, 8, r'$\sqrt{-12}=2\sqrt{3}\,i$', 'resultat', 'm')
# axe imaginaire
cx, cy, k = 66, 46, 8.0
arrow(ax, (cx - 14, cy), (cx + 16, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 36), (cx, cy + 38), 'fixe', lw=0.6)
t = 2 * math.sqrt(3)
disc(ax, cx, cy + t * k, 1.5, 'resultat'); disc(ax, cx, cy - t * k, 1.5, 'fixe')
line(ax, [(cx, cy), (cx, cy + t * k)], 'resultat', lw=1.6)
text(ax, cx + 3, cy + t * k, r'$2\sqrt{3}\,i$', 'resultat', 's', ha='left')
text(ax, cx + 3, cy - t * k, r'$-2\sqrt{3}\,i$', 'fixe', 's', ha='left')
text(ax, cx + 16, cy + 3, 'réel', 'fixe', 's', ha='right')
text(ax, cx + 6, cy + 40, r'$i$', 'fixe', 's')
text(ax, cx, 8, r'$2\sqrt{3}\approx 3{,}46$ sur l’axe de $i$', 'resultat', 's')
save(fig, '39-119')
