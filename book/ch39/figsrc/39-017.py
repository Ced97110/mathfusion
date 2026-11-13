import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(54)
O = (12, 10); u = 20                               # 1 unité = 20 mm
P = pt(O, 2 * u, 60); H = (O[0] + 1 * u, O[1]); A = (O[0] + 2 * u, O[1])
arrow(ax, O, (62, 10), 'fixe', lw=0.9)
line(ax, [P, A], 'fixe', lw=1.0, dash=True)
line(ax, [O, H], 'varie', lw=1.8)
line(ax, [H, P], 'resultat', lw=1.8)
line(ax, [O, P], 'sujet', lw=1.8)
line(ax, [(H[0] - 2.2, H[1]), (H[0] - 2.2, H[1] + 2.2), (H[0], H[1] + 2.2)], 'encre', lw=0.7)
arc(ax, O, 8, 0, 60)
for q in (O, H, P, A):
    disc(ax, q[0], q[1], 1.1, 'sujet')
text(ax, 9.3, 6.8, 'O'); text(ax, H[0], 6.5, 'H'); text(ax, A[0], 6.5, 'A')
text(ax, 17.6, 29, '2', 'sujet', 'l')
text(ax, 22, 6.5, '1', 'varie', 'l')
text(ax, H[0] - 3, 28, r'$\sqrt{3}$', 'resultat', 'l')
text(ax, 45.5, 29, '2', 'fixe', 'l')
text(ax, 25, 14.5, '60°')
text(ax, 36, 49.5, r'$P\,(1,\ \sqrt{3})$', 'sujet', 'm', ha='left')
text(ax, 73, 26, r'$1^2+(\sqrt{3})^2=2^2$', 'encre', 's')
save(fig, '39-017')
