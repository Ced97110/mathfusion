import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R = 27, 28, 19
pos = {}
for n in range(12):
    a = math.radians(90 - 30 * n)
    pos[n] = (cx + R * math.cos(a), cy + R * math.sin(a))
role = {n: 'sujet' for n in range(12)}
role[1] = 'autre'; role[3] = 'varie'
for n in range(12):
    disc(ax, pos[n][0], pos[n][1], 3.3, role[n], label=str(n), size='s')
text(ax, 66, 46, 'M : groupe de 12 heures', 'sujet', 's')
text(ax, 66, 38, 'D = ℤ agit : n × 1', 'varie', 's')
text(ax, 66, 30, 'un seul générateur : 1', 'autre', 's')
text(ax, 66, 22, 'il suffit : type fini', 'resultat', 's')
a, b = pos[1], pos[3]
d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
arrow(ax, (a[0]+u[0]*3.6, a[1]+u[1]*3.6), (b[0]-u[0]*3.6, b[1]-u[1]*3.6), 'varie', curve=-0.25)
text(ax, 36, 34, '× 3', 'varie', 's')
save(fig, '60-032')
