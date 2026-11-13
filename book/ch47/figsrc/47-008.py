import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 32, 19
ax.add_patch(Circle((cx, cy), R + 4.5, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
roles = ['sujet', 'varie', 'autre']
for h in range(12):
    a = math.radians(90 - 30 * h); x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    disc(ax, x, y, 3.3, roles[h % 3], label=str(h), size='s')
text(ax, cx, cy, '12 heures', 'encre', 's')
text(ax, 68, 56, '3 lignes de 4', 'encre', 'm')
for r_ in range(3):
    for i in range(4):
        disc(ax, 56 + i * 8, 44 - r_ * 12, 3, roles[r_])
text(ax, 68, 6, r'$12 = 3 \times 4$', 'resultat', 'l')
save(fig, '47-008')
