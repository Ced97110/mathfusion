import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def P(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    n = 30; line(ax, [P(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw=lw)
def square(ax, v, d1, d2, s=2.2, role="encre"):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); w = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(v[0] + s * u[0], v[1] + s * u[1]), (v[0] + s * (u[0] + w[0]), v[1] + s * (u[1] + w[1])), (v[0] + s * w[0], v[1] + s * w[1])], role, lw=0.7)

fig, ax = canvas(84)
fig, ax = canvas(84)
box(ax, 14, 70, 60, 9, 'sujet', label=r'on connaît $\sin A = 0{,}6$', size='s')
forms = [(r'$\cos^2 A - \sin^2 A$', 'manque cos A', 'fixe'), (r'$2\cos^2 A - 1$', 'manque cos A', 'fixe'), (r'$1 - 2\sin^2 A$', 'tout est connu', 'resultat')]
for i, (f, tag, role) in enumerate(forms):
    y = 50 - i * 14
    box(ax, 4, y, 44, 9, role, dash=(role == 'fixe'), label=f, size='s')
    text(ax, 52, y + 4.5, tag, role, 's', ha='left')
arrow(ax, (44, 69), (30, 59.8), 'varie', curve=0.0) if False else None
arrow(ax, (10, 69.3), (10, 59.8), 'fixe') if False else None
arrow(ax, (82, 69), (82, 24), 'resultat', curve=-0.0) if False else None
box(ax, 14, 2, 60, 9, 'resultat', label=r'$1 - 2 \times 0{,}36 = 0{,}28$', size='s')
arrow(ax, (26, 22), (26, 11.5), 'resultat')
save(fig, '34-089')
