import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(70)
u, k = 4.5, 1.6
for cx, s, role, hd, cap in ((21, 1, 'sujet', 'a = 1 > 0', 'point le plus bas'), (65, -1, 'autre', 'a = −1 < 0', 'point le plus haut')):
    line(ax, [(cx - 17, 36), (cx + 17, 36)], 'fixe')
    curve(ax, lambda x: s * x * x, -3, 3, lambda x: cx + u * x, lambda y: 36 + k * y, role)
    disc(ax, cx, 36, 1.2, role)
    for x in (2, 3):
        disc(ax, cx + u * x, 36 + k * s * x * x, 1.0, role)
        text(ax, cx + u * x + 3.6, 36 + k * s * x * x, f'{s * x * x}'.replace('-', '−'), role, 's')
    text(ax, cx, 62, hd, role, 'm')
    text(ax, cx, 31 if s > 0 else 41, cap, role, 's')
text(ax, 21, 56, 'vers le haut', 'sujet', 's', ha='center')
text(ax, 65, 16, 'vers le bas', 'autre', 's')
save(fig, '23-086')
