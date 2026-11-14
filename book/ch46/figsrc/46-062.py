import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pos(h, cx, cy, R):
    a = math.radians(90 - 30 * h); return (cx + R * math.cos(a), cy + R * math.sin(a))
def edge(p, q, off):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * off, p[1] + u[1] * off), (q[0] - u[0] * off, q[1] - u[1] * off)

fig, ax = canvas(74)
cx, cy, R = 44, 35, 16
for h in range(12):
    if h not in (0, 4, 8): x, y = pos(h, cx, cy, R); disc(ax, x, y, 0.9, 'fixe')
P = {h: pos(h, cx, cy, R) for h in (0, 4, 8)}
for h, role in ((0, 'resultat'), (4, 'sujet'), (8, 'sujet')): disc(ax, *P[h], 3.0, role, label=str(h), size='s')
for p, q in ((0, 4), (4, 8), (8, 0)):
    a, b = edge(P[p], P[q], 3.8); arrow(ax, a, b, 'varie', both=True)
text(ax, 58, 38, '± 4', 'varie', 's'); text(ax, 44, 30.5, '± 4', 'varie', 's'); text(ax, 30, 38, '± 4', 'varie', 's')
text(ax, 44, 57, 'e : aucun facteur', 'resultat', 's')
text(ax, 44, 68, r'$e,\ s_1,\ s_1s_2,\ \ldots,\ s_1\cdots s_r$', 'encre', 'm')
text(ax, 62, 27, '4 = s₁ : un facteur', 'sujet', 's', ha='left')
text(ax, 26, 27, '8 = 4 + 4 = s₁s₂', 'sujet', 's', ha='right')
text(ax, 44, 5, '⟨4⟩ = {0, 4, 8}', 'sujet', 'm', weight='bold')
save(fig, '46-062')
