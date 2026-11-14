import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, r = 24, 52, 14
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.7, zorder=1))
for h in range(12):
    a = math.radians(90 - 30 * h); p = (cx + r * math.cos(a), cy + r * math.sin(a))
    if h in (0, 4, 8):
        disc(ax, *p, 2.0, 'resultat' if h == 0 else 'sujet')
        q = (cx + (r + 5.2) * math.cos(a), cy + (r + 5.2) * math.sin(a))
        text(ax, q[0], q[1], ['0', '', '', '', '4 h', '', '', '', '8 h'][h] if h else '0', 'resultat' if h == 0 else 'sujet', 's')
    else:
        disc(ax, *p, 0.9, 'fixe')
text(ax, 24, 76, 'horloge : x = 4 h', 'sujet', 's', weight='bold')
text(ax, 68, 76, 'd × 4 h', 'varie', 's', weight='bold')
for y, t, role in [(63, '3 × 4 = 12 = 0', 'resultat'), (50, '6 × 4 = 24 = 0', 'resultat'), (37, '5 × 4 = 20 = 8', 'limite')]:
    box(ax, 50, y - 5, 36, 10, role, label=t, size='s')
text(ax, 68, 25.5, 'ne tue pas x', 'limite', 's')
f = numberline(ax, 8, 80, 14, 0, 12, labels=False, arrow_right=False)
for v in range(13):
    if v % 3 == 0:
        disc(ax, f(v), 14, 1.7, 'resultat'); text(ax, f(v), 8.5, str(v), 'resultat', 's')
text(ax, 44, 3, 'coefficients qui tuent x : multiples de 3', 'resultat', 's')
save(fig, '57-164')
