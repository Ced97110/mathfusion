import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 27, 32, 17
def ang(h): return math.radians(90 - 30 * h)
def pt(h, r=R):
    a = ang(h); return (cx + r * math.cos(a), cy + r * math.sin(a))
disc(ax, cx, cy, R, 'fixe')
for h in range(12):
    if h not in (0, 5, 10, 3):
        x, y = pt(h); disc(ax, x, y, 0.6, 'fixe')
def arc(h0, h1, role):
    d = 3.1 / R
    a0 = ang(h0) - d; a1 = ang(h1) + d; n = 24
    pts = [(cx + R * math.cos(a0 + (a1 - a0) * k / n), cy + R * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
    line(ax, pts[:-3], role, lw=1.6)
    arrow(ax, pts[-4], pts[-1], role, lw=1.6)
for h0, h1 in ((0, 5), (5, 10), (10, 15)):
    arc(h0, h1, 'varie')
    x, y = pt((h0 + h1) / 2, R + 6)
    text(ax, x, y, '+ 5', 'varie', 's')
for h, role, lab in ((0, 'sujet', '0'), (5, 'varie', '5'), (10, 'varie', '10'), (3, 'resultat', '3')):
    x, y = pt(h); disc(ax, x, y, 2.8, role, label=lab, size='s')
text(ax, 27, 61, 'horloge à 12 heures', 'fixe', 's')
text(ax, 56, 44, 'addition répétée :', 'fixe', 's', ha='left')
text(ax, 56, 37, '3·5 = 5 + 5 + 5', 'sujet', 'm', ha='left')
text(ax, 56, 30, '= 15, soit 3 heures', 'resultat', 's', ha='left')
box(ax, 54, 12, 32, 10, 'resultat', label='seule valeur : 3 h', size='s')
save(fig, '57-092')
