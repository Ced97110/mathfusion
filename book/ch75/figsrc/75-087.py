import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx, cy = 44, 52
for ang in (0, 60, 120):
    a = math.radians(ang); line(ax, [(cx - 30 * math.cos(a), cy - 30 * math.sin(a) * 0.55), (cx + 30 * math.cos(a), cy + 30 * math.sin(a) * 0.55)], 'fixe', lw=0.7)
    d = (math.cos(a), math.sin(a) * 0.55)
    arrow(ax, (cx, cy), (cx + 11 * d[0], cy + 11 * d[1]), 'sujet', lw=1.2)
    arrow(ax, (cx, cy), (cx + 22 * d[0], cy + 22 * d[1]), 'varie', lw=1.2) if False else None
    arrow(ax, (cx + 11 * d[0], cy + 11 * d[1]), (cx + 22 * d[0], cy + 22 * d[1]), 'varie', lw=1.2)
text(ax, 44, 72, r'$\gamma$ garde chaque droite : $\gamma=a$', 'encre', 'm')
text(ax, cx + 5.5, cy - 3.5, r'$u$', 'sujet', 'm'); text(ax, cx + 17, cy - 3.5, r'$\gamma u$', 'varie', 'm')
f = numberline(ax, 12, 66, 16, -2, 2, arrow_right=True)
for v, role in ((-1, 'resultat'), (1, 'resultat'), (2, 'limite')):
    disc(ax, f(v), 16, 1.8, role)
text(ax, f(-1), 26, r'$a^2=1$', 'resultat', 's'); text(ax, f(1), 26, r'$a^2=1$', 'resultat', 's')
text(ax, f(2), 26, r'$a^2=4$', 'limite', 's')
text(ax, 44, 6, r'$a^2=1$ donc $a=1$ ou $a=-1$', 'encre', 'm')
save(fig, '75-087')
