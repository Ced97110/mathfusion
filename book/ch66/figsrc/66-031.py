import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 30, 33, 17
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
angs = [0, 60, 120, 180, 240, 300]
pts = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in angs]
line(ax, pts + [pts[0]], 'fixe', lw=0.6)
for a, (x, y) in zip(angs, pts):
    prim = a in (60, 300)
    disc(ax, x, y, 2.2, 'sujet' if prim else 'fixe')
    lx = cx + (R + 5.5) * math.cos(math.radians(a)); ly = cy + (R + 4.5) * math.sin(math.radians(a))
    text(ax, lx, ly, f'{a}°', 'sujet' if prim else 'fixe', 's')
box(ax, 58, 38, 28, 16, 'fixe', label='4 déjà vus')
text(ax, 72, 35, 'pour 2 ou 3 côtés', 'fixe', 's')
box(ax, 58, 12, 28, 16, 'sujet', label='2 primitifs')
text(ax, 72, 9, r'$\Phi_6$ : ces deux-là', 'sujet', 's')
save(fig, '66-031')
