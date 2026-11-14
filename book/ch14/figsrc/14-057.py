import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'$a^{-n}=1/a^n$', 'sujet', 'l')
H = 16; base = 26
xs = [14, 34, 54, 74]
for k, (x, hrs, ex, fr) in enumerate(zip(xs, ('9 h', '10 h', '11 h', '12 h'), (-3, -2, -1, 0), (8, 4, 2, 1))):
    w = H / fr
    role = 'sujet' if fr == 1 else 'varie'
    ax.add_patch(Rectangle((x - w / 2, base), w, H, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, x, base + H + 3.5, hrs, 'encre', 's')
    text(ax, x, base - 4, r'$2^{%d}=%s$' % (ex, '1/%d' % fr if fr > 1 else '1'), role, 's')
for k in range(3):
    xa = xs[k + 1] - H / (8 >> (k + 1)) / 2 - 1
    xb = xs[k] + H / (8 >> k) / 2 + 1
    arrow(ax, (xa, base + H / 2), (xb, base + H / 2), 'varie')
text(ax, 44, 8, 'chaque heure avant : moitié', 'varie', 's')
save(fig, '14-057')
