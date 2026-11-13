import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 44, 37, 21
for k in range(12):
    a = math.radians(30 * k)
    role = 'varie' if k % 3 == 0 else ('limite' if k == 1 else 'fixe')
    disc(ax, cx + R * math.sin(a), cy + R * math.cos(a), 4, role, label=str(k), size='s')
text(ax, cx, cy, r'$3 \times v \equiv 1\ ?$', 'encre', 'm')
text(ax, 44, 5, '3 × v : seulement 0, 3, 6, 9', 'varie', 'm')
save(fig, '44-151')
