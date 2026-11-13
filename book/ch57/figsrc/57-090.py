import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 26, 36, 17
pt = lambda h, r=R: (cx + r * math.sin(math.radians(30 * h)), cy + r * math.cos(math.radians(30 * h)))
for h in range(12):
    px, py = pt(h)
    role = 'resultat' if h == 3 else ('sujet' if h in (0, 5, 10) else 'fixe')
    disc(ax, px, py, 1.9 if role != 'fixe' else 1.1, role)
for a, b in [(0, 5), (5, 10), (10, 3)]:
    (px, py), (qx, qy) = pt(a), pt(b)
    d = math.hypot(qx - px, qy - py); ux, uy = (qx - px) / d, (qy - py) / d
    arrow(ax, (px + ux * 2.4, py + uy * 2.4), (qx - ux * 2.4, qy - uy * 2.4), 'varie')
for h in range(12):
    role = 'resultat' if h == 3 else ('sujet' if h in (0, 5, 10) else 'fixe')
    lx, ly = pt(h, R + 4.8)
    text(ax, lx, ly, str(h or 12), role, 's')
text(ax, 55, 36, '3 × 5 h\n= 5 + 5 + 5\n= 15 h = 3 h', 'varie', 'm', ha='left')
text(ax, 44, 4, r'$nx=x+x+\cdots+x$', 'sujet', 'm')
save(fig, '57-090')
