import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 19, 34, 12
ax.add_patch(Circle((cx, cy), R, fill=False, ec=COL['sujet'], lw=0.6, zorder=1))
for k in range(6):
    a = math.radians(90 - 60 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.6, 'sujet')
text(ax, cx, cy, 'ℤ/6ℤ', 'sujet', 'm', weight='bold')
text(ax, cx, 14, 'horloge à 6 positions', 'sujet', 's')
text(ax, 50, 58, 'anneau choisi', 'varie', 's')
text(ax, 73, 58, 'ℤ/6ℤ est un module ?', 'encre', 's')
rows = [(40, 'ℤ', 'resultat', 'oui ✓'), (26, 'ℤ/6ℤ', 'resultat', 'oui ✓'), (12, 'ℚ', 'limite', 'non ✗')]
for y, ring, role, verdict in rows:
    box(ax, 42, y, 16, 10, 'varie', label=ring)
    arrow(ax, (58.8, y + 5), (66.2, y + 5), 'fixe')
    box(ax, 67, y, 18, 10, role, label=verdict, size='m', weight='bold')
save(fig, '57-212')
