import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(56)
cx, cy, r = 25, 28, 15
box(ax, 2, 6, 46, 44, 'sujet', fill=False, dash=True)
disc(ax, cx, cy, r, 'fixe', fill=False)
q = [P(cx, cy, r, 90 * k) for k in range(4)]
poly(ax, q, 'sujet')
for p in q: disc(ax, p[0], p[1], 1.6, 'sujet')
text(ax, 8, 44, r'$U$', 'sujet', 'xl', weight='bold')
text(ax, 67, 40, r'$U$ : le groupe des' + '\nracines $n$-ièmes\nde l\'unité', 'sujet', 's')
text(ax, 67, 24, r'ici $n=4$ :' + '\n4 sommets', 'resultat', 's')
text(ax, 67, 12, 'notation de\nJacobson', 'fixe', 's')
save(fig, '66-026')
