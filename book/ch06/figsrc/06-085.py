import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 18
f = numberline(ax, 8, 70, y, 0, 1, step=0.25, every=4, arrow_right=False)
fr = [r'$3/4$', r'$6/8$', r'$9/12$', r'$12/16$', r'$15/20$', '…']
xs = [10 + 14 * i for i in range(6)]
xp = f(0.75)
for i, (x, s) in enumerate(zip(xs, fr)):
    text(ax, x, 54, s, 'sujet' if i == 0 else 'autre', 'm')
    if i < 5:
        line(ax, [(x, 45), (xp, 19.5)], 'sujet' if i == 0 else 'autre', lw=0.8)
    if 0 < i < 5:
        text(ax, x, 49, rf'$\times {i+1}$', 'varie', 's')
disc(ax, xp, y, 1.4, 'resultat')
text(ax, xp, 10.5, r'$P$', 'resultat', 'm')
save(fig, '06-085')
