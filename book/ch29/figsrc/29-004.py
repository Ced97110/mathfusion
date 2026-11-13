import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(68)
cw, ch = 20, 12
xs = [4, 28, 52]
top = [(r'$2\pi$', 'varie'), ('500', 'sujet'), ('12', 'autre')]
bot = [top[1], top[2], top[0]]
yt, yb = 46, 14
for i, (lab, ro) in enumerate(top):
    box(ax, xs[i], yt, cw, ch, ro, label=lab)
for i, (lab, ro) in enumerate(bot):
    box(ax, xs[i], yb, cw, ch, ro, label=lab)
for i, (lab, ro) in enumerate(top):
    j = [l for l, _ in bot].index(lab)
    arrow(ax, (xs[i] + cw / 2, yt), (xs[j] + cw / 2, yb + ch), ro, lw=0.9)
text(ax, 80, yt + ch / 2, r'$\div 360$', 'fixe', 's')
text(ax, 80, yb + ch / 2, r'$\div 360$', 'fixe', 's')
text(ax, 44, 63, 'ordre 1', 'fixe', 's')
text(ax, 44, 7, 'ordre 2 : mêmes facteurs', 'fixe', 's')
save(fig, '29-004')
