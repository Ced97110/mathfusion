import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R, RL = 44, 40, 16, 24
text(ax, 44, 74, 'ligne p6 : six rotations', 'sujet', 'l')
for k in range(6):
    a = math.radians(60 * k)
    line(ax, [(cx + 5.4*math.cos(a), cy + 5.4*math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], 'fixe')
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.2, 'varie')
    text(ax, cx + RL * math.cos(a), cy + RL * math.sin(a) * 0.92, f'{60*k}°', 'varie', 's')
disc(ax, cx, cy, 5.0, 'resultat', label=r'$C_6$', size='m')
text(ax, 44, 7, r'6 $\times$ 60° = 360°', 'encre', 'l')
save(fig, '74-162')
