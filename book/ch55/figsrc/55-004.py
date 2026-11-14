import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 83, r'$\mathbb{R}$ : une infinité d’essais', 'sujet', 's')
line(ax, [(4, 73), (84, 73)], 'fixe')
for i in range(26):
    disc(ax, 6 + i * 3.0, 73, 1.1, 'sujet')
text(ax, 24, 63, 'horloge à 3 positions', 'autre', 's')
cx, cy, R = 24, 38, 15
disc(ax, cx, cy, R, 'fixe', fill=False)
for k, ang in enumerate((90, -30, 210)):
    disc(ax, cx + R * math.cos(math.radians(ang)), cy + R * math.sin(math.radians(ang)), 4.2, 'autre', label=str(k))
text(ax, 66, 46, '3 essais seulement', 'autre', 's')
box(ax, 46, 12, 40, 16, 'fixe', label='mêmes valeurs' + r' $\Rightarrow$' + '\nmêmes coefficients ?', size='s', dash=True)
save(fig, '55-004')
