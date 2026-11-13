import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cols = [('A B C', 'fixe', 'e'), ('C A B', 'sujet', 'r'), ('B C A', 'sujet', 'r2'), ('A C B', 'varie', 'sA'), ('C B A', 'varie', 'sB'), ('B A C', 'varie', 'sC')]
xs = [10 + 13.6 * i for i in range(6)]
cy, R = 52, 5.5
V = {'A': (0, R), 'B': (-R * math.cos(math.radians(30)), -R / 2), 'C': (R * math.cos(math.radians(30)), -R / 2)}
text(ax, 44, 82, r'$S_3$ : rangements de A, B, C', 'encre', 's')
text(ax, 44, 33.5, r'$D_3$ : gestes sur le triangle', 'encre', 's')
for x, (s, role, kind) in zip(xs, cols):
    text(ax, x, 72, s, role, 's')
    arrow(ax, (x, 69.2), (x, 61.2), 'resultat', lw=0.8, both=True)
    poly(ax, [(x + V[k][0], cy + V[k][1]) for k in 'ABC'], 'fixe' if kind != 'e' else 'fixe')
    if kind in ('r', 'r2'):
        a0 = math.radians(90); sweep = math.radians(120 if kind == 'r' else 240)
        pts = [(x + 2.6 * math.cos(a0 + sweep * t / 24), cy + 2.6 * math.sin(a0 + sweep * t / 24)) for t in range(25)]
        line(ax, pts[:-1], 'sujet', lw=1.0); arrow(ax, pts[-2], pts[-1], 'sujet', lw=1.0)
    if kind in ('sA', 'sB', 'sC'):
        v = V[kind[1]]; d = (-v[0] / R, -v[1] / R)
        line(ax, [(x + v[0] - d[0], cy + v[1] - d[1]), (x + v[0] + d[0] * (1.5 * R + 1), cy + v[1] + d[1] * (1.5 * R + 1))], 'varie', lw=1.0, dash=True)
brace(ax, xs[0] - 5, xs[0] + 5, 28, 'fixe', '1 identité')
brace(ax, xs[1] - 5, xs[2] + 5, 28, 'sujet', '2 rotations')
brace(ax, xs[3] - 5, xs[5] + 5, 28, 'varie', '3 réflexions')
text(ax, 44, 12, r'$1 + 2 + 3 = 6$', 'resultat', 'm', weight='bold')
save(fig, '50-082')
