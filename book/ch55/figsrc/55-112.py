import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
xs = [3, 31, 59]
w, h = 26, 11
top = [r'$(-1)^2=1$', r'$(-3)^2=9$', r'$(-2)^2=4$']
bot = [r'$1^2=1$', r'$(-2)^2=4$', r'$(-3)^2=9$']
yt, yb = 50, 20
text(ax, 3, 68, 'valeurs 1, 2, 4', 'sujet', 'm', ha='left', weight='bold')
text(ax, 85, 68, r'$1\times 9\times 4=36$', 'sujet', 'm', ha='right')
text(ax, 3, 12, 'on échange : 2, 1, 4', 'varie', 'm', ha='left', weight='bold')
text(ax, 85, 12, r'$1\times 4\times 9=36$', 'varie', 'm', ha='right')
link = [(0, 0), (1, 2), (2, 1)]
for a, b in link:
    line(ax, [(xs[a] + w / 2, yt - 0.5), (xs[b] + w / 2, yb + h + 0.5)], 'resultat', lw=1.1)
for x, t in zip(xs, top):
    box(ax, x, yt, w, h, 'sujet', label=t, size='s')
for x, t in zip(xs, bot):
    box(ax, x, yb, w, h, 'varie', label=t, size='s')
save(fig, '55-112')
