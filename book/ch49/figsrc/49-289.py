import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
c = (24, 36); R = 13
ang = [225, 315, 45, 135]
P = [(c[0] + R * math.cos(math.radians(a)), c[1] + R * math.sin(math.radians(a))) for a in ang]
poly(ax, P, 'fixe')
for i in range(4):
    j = (i + 1) % 4
    a, b = P[i], P[j]
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    arrow(ax, (a[0] + u[0]*4.5 - u[1]*0, a[1] + u[1]*4.5), (b[0] - u[0]*4.5, b[1] - u[1]*4.5), 'varie', curve=0.0)
for i, p in enumerate(P):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=str(i + 1))
text(ax, 24, 11, 'une orbite : 4 sommets', 'sujet', 's')
rows = [('rotations', '4', 'fixe'), ('stabilisateur', '1 (neutre)', 'fixe'), ('orbite', r'$4 \div 1 = 4$', 'resultat')]
for k, (a, b, r) in enumerate(rows):
    y = 58 - k * 17
    text(ax, 46, y + 4, a, 'encre', 's', ha='left')
    box(ax, 46, y - 7, 38, 8, r, label=b, size='m')
text(ax, 65, 7, r'$|S|$ = 4, multiple de 4', 'resultat', 's')
save(fig, '49-289')
