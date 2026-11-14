import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
pa = lambda v: 8 + (v - 1.409) / 0.007 * 50
p1, ps, p2, p3 = pa(1.41), pa(2 ** 0.5), pa(1.415), 78
y = 24
line(ax, [(4, y), (60, y)], 'fixe')
line(ax, [(61, y - 2), (63, y + 2)], 'fixe'); line(ax, [(64, y - 2), (66, y + 2)], 'fixe')
arrow(ax, (67, y), (85, y), 'fixe')
line(ax, [(4, y), (ps, y)], 'sujet', lw=2.6)
for p, r in [(p1, 'sujet'), (p2, 'autre'), (p3, 'autre')]:
    disc(ax, p, y, 1.3, r)
disc(ax, ps, y, 1.7, 'limite', fill=False, lw=1.0)
text(ax, p1, 30, '1,41', 'sujet', 's'); text(ax, p2, 30, '1,415', 'autre', 's'); text(ax, p3, 30, '1,5', 'autre', 's')
line(ax, [(ps, 26.5), (ps, 38)], 'limite', dash=True)
text(ax, 38, 41, r'$\sqrt{2}$ : pas une fraction', 'limite', 's')
text(ax, 72, 41, 'majorants', 'autre', 's')
text(ax, p1, 17, '1,9881 < 2', 'sujet', 's'); text(ax, p2 + 2, 17, '2,002225 > 2', 'autre', 's'); text(ax, p3 + 1, 17, '2,25 > 2', 'autre', 's')
text(ax, 30, 8, r'ces fractions : $x^2 < 2$', 'sujet', 's')
save(fig, '79-069')
