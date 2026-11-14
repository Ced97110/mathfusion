import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\det(I-R_\theta)=2-2\cos\theta$', 'sujet', 'l')
base, u = 12, 8.5
line(ax, [(8, base), (80, base)], 'fixe')
for i, (ang, v) in enumerate([(60, 1), (90, 2), (180, 4)]):
    x = 18 + i * 24
    box(ax, x, base, 16, v * u, 'varie', label=str(v), size='l')
    text(ax, x + 8, base - 3.5, f'{ang}°', 'encre', 'm')
text(ax, 62, 50, r'$\cos\theta=1$ : 0 seulement', 'limite', 's', ha='center')
save(fig, '74-050')
