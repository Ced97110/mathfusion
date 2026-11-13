import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [4 + i * 21 for i in range(4)]
top = [8, 10, 12, 15]
bot = [8, 12, 10, 15]
yt, yb, h, w = 48, 24, 10, 14
for x, v in zip(xs, top):
    role = 'varie' if v in (10, 12) else 'sujet'
    box(ax, x, yt, w, h, role, label=str(v))
for x, v in zip(xs, bot):
    role = 'varie' if v in (10, 12) else 'sujet'
    box(ax, x, yb, w, h, role, label=str(v))
arrow(ax, (xs[0] + 7, yt - 0.5), (xs[0] + 7, yb + h + 0.5), 'fixe')
arrow(ax, (xs[3] + 7, yt - 0.5), (xs[3] + 7, yb + h + 0.5), 'fixe')
arrow(ax, (xs[1] + 7, yt - 0.5), (xs[2] + 7, yb + h + 0.5), 'varie', lw=1.3)
arrow(ax, (xs[2] + 7, yt - 0.5), (xs[1] + 7, yb + h + 0.5), 'varie', lw=1.3)
text(ax, 22, 40, 'échange', 'varie', 's')
brace(ax, xs[0], xs[1] + w, yb - 1, 'resultat', label='8 + 12', size='s')
brace(ax, xs[2], xs[3] + w, yb - 1, 'resultat', label='10 + 15', size='s')
box(ax, 14, 2, 60, 10, 'resultat', label='permis : 10 + 12 = 12 + 10', size='s')
save(fig, '57-046')
