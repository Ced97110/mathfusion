import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, r = 34, 10, 18
t = [i*math.pi/60 for i in range(61)]
line(ax, [(cx + r*math.cos(a), cy + r*math.sin(a)) for a in t], 'sujet', lw=1.2)
line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe')
line(ax, [(cx, cy), (cx, cy + r)], 'sujet', lw=1.2)
disc(ax, cx, cy + r, 1.1, 'sujet'); disc(ax, cx - r, cy, 1.1, 'sujet')
text(ax, cx, cy + r + 4, r'sin 90° = 1', 'sujet', 'm')
text(ax, cx + 9, cy + 4, r'90° + 90°', 'varie', 'm')
text(ax, cx - r + 3, 4.5, r'sin 180° = 0', 'sujet', 'm')
line(ax, [(cx, cy + r), (70, cy + r)], 'fixe', dash=True)
line(ax, [(70, cy), (70, cy + 2*r)], 'limite', lw=2.2)
text(ax, 70, cy + 2*r + 4, r'1 + 1 = 2', 'limite', 'm')
disc(ax, 70, cy, 1.4, 'resultat')
text(ax, 70, 4.5, 'vrai : 0', 'resultat', 'm')
save(fig, '34-004')
