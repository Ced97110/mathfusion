import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 95, r'dans $\mathbb{N}$ : $3$ n’a pas d’inverse', 'limite', 's')
g = numberline(ax, 14, 74, 34, -3, 3, arrow_right=False, size='s')
text(ax, 44, 57, r'dans $\mathbb{Z}$ : chacun a son inverse', 'resultat', 's')
# N: only 1, 2, 3 and 0 exist; the left half is missing
f = lambda v: g(v)
y = 84
line(ax, [(f(0), y), (f(3), y)], 'fixe')
for v in range(0, 4):
    disc(ax, f(v), y, 1.6, 'sujet' if v == 3 else 'fixe')
line(ax, [(f(-3), y), (f(0) - 2, y)], 'limite', dash=True)
cx, cy = f(-3), y
line(ax, [(cx - 1.8, cy - 1.8), (cx + 1.8, cy + 1.8)], 'limite', lw=1.4); line(ax, [(cx - 1.8, cy + 1.8), (cx + 1.8, cy - 1.8)], 'limite', lw=1.4)
text(ax, f(-3), y - 6, r'$-3$ absent', 'limite', 's')
# Z: pairs
for k in (1, 2, 3):
    disc(ax, g(k), 34, 1.8, 'sujet'); disc(ax, g(-k), 34, 1.8, 'resultat')
    arrow(ax, (g(-k), 36.5), (g(k), 36.5), 'resultat', lw=0.9, curve=-0.45, both=True)
text(ax, 44, 17, r'$1+(-1)=2+(-2)=3+(-3)=0$', 'resultat', 's')
text(ax, 44, 6, r'$a\,a^{-1}=1=a^{-1}a$ pour chaque $a$', 'encre', 's')
save(fig, '44-103')
