import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 3.2
def grid(cx, n, role, miss=None):
    x0 = cx - n * u / 2
    for i in range(n):
        for j in range(n):
            if miss and (i, j) == miss:
                box(ax, x0 + i * u, 12 + j * u, u, u, 'limite', fill=False, r=0.1, dash=True, lw=0.5); continue
            box(ax, x0 + i * u, 12 + j * u, u, u, role, r=0.1, lw=0.5)
grid(13, 4, 'sujet'); grid(37, 7, 'sujet')
x0 = 62 - 7; box(ax, 57, 12, 14, 14, 'sujet', label=r'$x^2$', size='m')
grid(80, 2, 'limite', miss=(1, 1))
text(ax, 13, 6.5, '16 = 4 × 4', 'sujet', 's')
text(ax, 37, 6.5, '49 = 7 × 7', 'sujet', 's')
text(ax, 64, 6.5, r'$x\times x$', 'sujet', 's')
text(ax, 80, 6.5, '3 : non', 'limite', 's')
text(ax, 37, 38, 'carrés parfaits', 'sujet', 'm', weight='bold')
text(ax, 74, 38, 'pas un carré', 'limite', 'm', weight='bold')
save(fig, '18-051')
