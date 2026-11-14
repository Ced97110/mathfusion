import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 20, 22, 22
for i in range(10):
    a = 40 + 10 * i
    poly(ax, [(cx, cy)] + arcp(cx, cy, R, a, a + 10, 6), 'varie' if i == 5 else 'resultat', lw=0.5)
line(ax, arcp(cx, cy, R, 40, 140), 'varie', lw=1.6)
text(ax, 24, 56, 'coupé en secteurs fins', 'encre', 's')
tx = 64
line(ax, [(tx, 22), (58, 48.4)], 'sujet')
line(ax, [(tx, 22), (70, 48.4)], 'sujet')
poly(ax, [(tx, 22), (58, 48), (64, 49), (70, 48)], 'varie')
line(ax, [(58, 48), (64, 49), (70, 48)], 'varie', lw=1.8)
line(ax, [(tx, 22), (tx, 48.6)], 'sujet', dash=True)
text(ax, 66, 58, 'presque un triangle', 'encre', 's')
text(ax, 72, 35, 'hauteur r', 'sujet', 's', ha='left')
text(ax, 72, 50, 'petit arc', 'varie', 's', ha='left')
arrow(ax, (21, 45), (57, 44), 'varie', curve=-0.3)
for i in range(10):
    poly(ax, [(8 + 7.2 * i, 10.8), (15.2 + 7.2 * i, 10.8), (15.2 + 7.2 * i, 13.2), (8 + 7.2 * i, 13.2)], 'varie', lw=0.5)
text(ax, 32, 6, 'bases bout à bout : arc s', 'varie', 's')
text(ax, 72, 5.5, r'$A=\frac{1}{2}\,r\,s$', 'resultat', 'l')
save(fig, '29-085')
