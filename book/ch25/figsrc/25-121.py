import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(52)
A = (6, 12); P = (50, 12); u = 44
line(ax, [A, (P[0] + 4, 12)], 'fixe')
line(ax, [P, (P[0], 12 + 0.1763 * u)], 'varie', lw=1.8)
for t, lab, y in [(10, 'tan 10° ≈ 0,1763', 25), (5, 'tan 5° ≈ 0,0875', 18.5), (1, 'tan 1° ≈ 0,0175', 12)]:
    h = math.tan(math.radians(t)) * u
    line(ax, [A, (P[0], 12 + h)], 'sujet', lw=1.2)
    text(ax, 56, y, lab, 'sujet', 's', ha='left')
text(ax, 28, 7, 'adjacent 1', 'fixe', 's')
text(ax, 62, 33, 'opposé', 'varie', 's')
box(ax, 8, 36, 60, 9, 'resultat', label='0° : segment, tan 0° = 0/1 = 0', size='s')
save(fig, '25-121')
