import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
rows = [(2, [1, 2, 1]), (3, [1, 3, 3, 1]), (4, [1, 4, 6, 4, 1])]
cx = [20, 33, 46, 59, 72]
heads = [r'$F$', r'$V$', r'$\Lambda^2$', r'$\Lambda^3$', r'$\Lambda^4$']
for c, h in zip(cx, heads): text(ax, c, 51, h, 'encre', 'm')
p = 2.8
for ri, (n, cs) in enumerate(rows):
    y0 = 36 - ri * 15
    text(ax, 2, y0 + 2.5, f'$n={n}$', 'encre', 's', ha='left')
    for li, cnt in enumerate(cs):
        for k in range(cnt):
            gx = cx[li] - 1.5 * p + (k % 3) * p; gy = y0 + (k // 3) * p
            ax.add_patch(Rectangle((gx, gy), p - 0.5, p - 0.5, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
        if li > 0:
            xm = (cx[li] + cx[li - 1]) / 2
            line(ax, [(xm - 1.2, y0 + 2.2), (xm + 1.2, y0 + 2.2)], 'fixe'); line(ax, [(xm, y0 + 1.0), (xm, y0 + 3.4)], 'fixe')
    text(ax, 83, y0 + 2.5, f'{sum(cs)}', 'resultat', 'm', weight='bold')
text(ax, 83, 51, 'total', 'resultat', 's')
save(fig, '76-066')
