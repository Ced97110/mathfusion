import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$\mathbb{Z}^n/N$  =  des horloges  +  des $\mathbb{Z}$', 'encre', 'm')
# partie finie : horloge à 3 positions
cx, cy, R = 24, 36, 11
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
for k in range(3):
    a = math.radians(90 - 120 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.0, 'sujet', label=str(k), size='s')
text(ax, cx, cy - 18, r'$\mathbb{Z}/3\mathbb{Z}$', 'sujet', 'm')
text(ax, cx, cy - 23.5, '3 restes : fini', 'sujet', 's')
# partie infinie
text(ax, 44, cy, '×', 'encre', 'xl')
line(ax, [(52, cy), (80, cy)], 'resultat', lw=1.6)
arrow(ax, (80, cy), (85, cy), 'resultat', lw=1.6)
arrow(ax, (52, cy), (47.5, cy), 'resultat', lw=1.6)
for xv in range(54, 80, 5): line(ax, [(xv, cy - 1.5), (xv, cy + 1.5)], 'resultat', lw=0.8)
text(ax, 68, cy - 6, r'$\mathbb{Z}$', 'resultat', 'm')
text(ax, 68, cy - 11, 'infini', 'resultat', 's')
text(ax, 44, 8, 'cas : N = multiples de (3 ; 0)', 'fixe', 's')
save(fig, '57-191')
