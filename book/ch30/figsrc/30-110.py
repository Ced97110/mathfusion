import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def curve(ax, f, a, b, ox, oy, sx, sy, role, n=160, lw=1.2, clip=None, dash=False):
    seg = []
    for i in range(n + 1):
        x = a + (b - a) * i / n; y = f(x)
        if clip is not None and abs(y) > clip:
            if len(seg) > 1: line(ax, seg, role, lw=lw, dash=dash)
            seg = []; continue
        seg.append((ox + x * sx, oy + y * sy))
    if len(seg) > 1: line(ax, seg, role, lw=lw, dash=dash)

fig, ax = canvas(66)
text(ax, 44, 61, r'$y = 3\cos(2(x - 1)) + 5$', 'sujet', 'l')
text(ax, 44, 53, 'avant la fonction : on prépare l\'angle', 'varie', 's')
labs1 = [r'$x = 1$', r'$x - 1 = 0$', r'$2 \times 0 = 0$']
labs2 = [r'$\cos 0 = 1$', r'$3 \times 1 = 3$', r'$3 + 5 = 8$']
xs = [2, 32, 62]
for i, l in enumerate(labs1):
    box(ax, xs[i], 38, 24, 9, 'varie', label=l, size='s')
    if i: arrow(ax, (xs[i - 1] + 24.5, 42.5), (xs[i] - 0.5, 42.5), 'varie')
text(ax, 86, 30, 'la fonction, puis la valeur', 'sujet', 's', ha='right')
roles = ['sujet', 'varie', 'resultat']
for i, l in enumerate(labs2):
    box(ax, xs[i], 14, 24, 9, roles[i], label=l, size='s')
    if i: arrow(ax, (xs[i - 1] + 24.5, 18.5), (xs[i] - 0.5, 18.5), 'varie')
arrow(ax, (74, 37.5), (14, 23.5), 'varie', curve=0.0)
text(ax, 44, 6, r'les nombres $A, B, C, D$ valent pour toute fonction', 'fixe', 's')
save(fig, '30-110')
