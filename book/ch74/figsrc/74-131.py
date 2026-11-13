import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R = 44, 41, 21
labs = [r'$I$', r'$M$', r'$M^2$', r'$M^3=-I$', r'$M^4$', r'$M^5$']
pos = [(cx + R*math.cos(math.radians(60*k)), cy + R*math.sin(math.radians(60*k))) for k in range(6)]
for k in range(6):
    p, q = pos[k], pos[(k+1) % 6]
    d = math.hypot(q[0]-p[0], q[1]-p[1]); e = 3.4
    a = (p[0]+(q[0]-p[0])*e/d, p[1]+(q[1]-p[1])*e/d); b = (q[0]-(q[0]-p[0])*e/d, q[1]-(q[1]-p[1])*e/d)
    arrow(ax, a, b, 'varie')
for k, (x, y) in enumerate(pos):
    role = 'resultat' if k == 0 else ('limite' if k == 3 else 'sujet')
    disc(ax, x, y, 3.0, role)
    dx = 1 if k in (0, 1, 5) else (-1 if k in (2, 3, 4) else 0)
    ox = x + math.cos(math.radians(60*k))*(4+ (6 if k==3 else 0) if k in (0,3) else 4) 
    text(ax, ox + (0 if k in (0,3) else math.cos(math.radians(60*k))*4), y + math.sin(math.radians(60*k))*4.5, labs[k], role, 's')
arrow(ax, pos[0], pos[3], 'limite', curve=0.0, both=True, lw=0.6)
text(ax, cx, cy-4.5, 'demi-tour', 'limite', 's')
text(ax, cx, cy+3, r'$\times 3$', 'limite', 's')
text(ax, 44, 5, r'$M^6=I$ : ordre 6', 'resultat', 'm')
text(ax, 44, 75, 'une rotation de 60° à chaque pas', 'varie', 's')
save(fig, '74-131')
