import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(66)
cx, cy, r = 31, 34, 19
disc(ax, cx, cy, r, 'fixe', fill=False)
for k in range(6):
    p = P(cx, cy, r, 60 * k)
    disc(ax, p[0], p[1], 1.8 if k == 1 else 1.3, 'sujet' if k == 1 else 'fixe')
    q = P(cx, cy, r + 6.5, 60 * k)
    lab = '1' if k == 0 else (r'$\zeta_6$' if k == 1 else r'$\zeta_6^{%d}$' % k)
    text(ax, q[0] + (1 if k == 0 else 0), q[1], lab, 'sujet' if k == 1 else 'fixe', 's')
line(ax, [P(cx, cy, 8, 2 * i) for i in range(31)], 'varie')
q = P(cx, cy, 12.5, 30); text(ax, q[0], q[1], '60°', 'varie', 's')
text(ax, 72, 52, r'$\zeta_n$', 'sujet', 'xl', weight='bold')
text(ax, 72, 41, r'$\zeta$ : un sommet', 'sujet', 's')
text(ax, 72, 30, r'$n$ : nombre de' + '\nparts égales', 'varie', 's')
text(ax, 72, 18, r'$n=6$ : 60°' + '\nentre sommets', 'fixe', 's')
save(fig, '66-021')
