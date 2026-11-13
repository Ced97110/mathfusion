import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, s = 18, 8, 6.2
for k in range(-3, 4):
    a0, a1 = max(0, -k), min(5, 5 - k)
    if k != 2: line(ax, [(ox + a0 * s, oy + (a0 + k) * s), (ox + a1 * s, oy + (a1 + k) * s)], 'fixe')
line(ax, [(ox, oy + 2 * s), (ox + 3 * s, oy + 5 * s)], 'sujet', lw=1.8)
for a in range(6):
    for b in range(6):
        disc(ax, ox + a * s, oy + b * s, 0.55, 'sujet' if b - a == 2 else 'fixe')
for a, b, ha, dx in [(0, 2, 'right', -2), (1, 3, 'right', -2), (3, 5, 'left', 2)]:
    disc(ax, ox + a * s, oy + b * s, 1.4, 'sujet')
    text(ax, ox + a * s + dx, oy + b * s + 1.5, f'({a}, {b})', 'sujet', 's', ha=ha)
text(ax, 62, 50, 'une classe :', 'sujet', 's'); text(ax, 62, 46, 'une droite oblique', 'sujet', 's')
text(ax, 62, 24, 'autres classes', 'fixe', 's')
text(ax, ox - 3, oy - 4, r'$a$ : 0 à 5', 'fixe', 's', ha='left'); text(ax, ox + 22, oy - 4, r'$b$ : 0 à 5', 'fixe', 's', ha='left')
save(fig, '13-144')
