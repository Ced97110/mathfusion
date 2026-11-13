import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 22, 33, 14
text(ax, cx, 57, 'cadran à 6 heures', 'sujet', 's', weight='bold')
ang = lambda k: math.radians(90 - 60 * k)
for k in range(6):
    disc(ax, cx + R * math.cos(ang(k)), cy + R * math.sin(ang(k)), 3.3, 'fixe', label=str(k), size='s')
r2 = 7.5
for k in (0, 2, 4):
    a0 = 90 - 60 * k - 12; a1 = 90 - 60 * (k + 2) + 12
    ts = [a0 + (a1 - a0) * t / 20 for t in range(21)]
    pts = [(cx + r2 * math.cos(math.radians(a)), cy + r2 * math.sin(math.radians(a))) for a in ts]
    line(ax, pts[:-1], 'varie', lw=1.1)
    arrow(ax, pts[-2], pts[-1], 'varie', lw=1.1)
text(ax, cx, 12, '2 × 3 = 6, soit 0', 'resultat', 'm', weight='bold')
text(ax, cx, 6.5, 'deux facteurs non nuls', 'limite', 's')
line(ax, [(44, 8), (44, 56)], 'fixe', dash=True)
text(ax, 66, 57, 'matrices', 'sujet', 's', weight='bold')
box(ax, 48, 30, 14, 12, 'sujet', label='AB', size='l', weight='bold')
text(ax, 67, 36, '≠', 'limite', 'xl', weight='bold')
box(ax, 72, 30, 14, 12, 'autre', label='BA', size='l', weight='bold')
text(ax, 67, 22, "l'ordre compte", 'limite', 's')
save(fig, '51-008')
