import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
V = [(1, 0), (0, 1), (1, 1)]
pairs = [(a, b) for a in V for b in V if a != b]
u = 9
for i, (e, f) in enumerate(pairs):
    cx, cy = 14 + (i % 3) * 28, 44 - (i // 3) * 26
    arrow(ax, (cx, cy), (cx + e[0] * u, cy + e[1] * u), 'sujet', lw=1.1)
    arrow(ax, (cx, cy), (cx + f[0] * u, cy + f[1] * u), 'varie', lw=1.1)
    disc(ax, cx, cy, 0.8, 'encre')
    box(ax, cx - 5, cy - 6, 21, 21, 'resultat', fill=False, lw=1.1)
text(ax, 44, 70, 'les 6 paires de flèches', 'encre', 's')
text(ax, 8, 7, r'$e$', 'sujet', 'm'); text(ax, 20, 7, r'$f$', 'varie', 'm')
text(ax, 62, 7, r'les six : $\det=B(e,f)=1$', 'resultat', 's')
save(fig, '75-126')
