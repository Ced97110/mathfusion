import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
f1 = numberline(ax, 8, 76, 50, 0, 360, step=30, every=3, arrow_right=False)
text(ax, 44, 61, 'départ : 4 solutions', 'sujet', 's')
for v in (90, 210, 270, 330): disc(ax, f1(v), 50, 2.2, 'resultat')
f2 = numberline(ax, 8, 76, 18, 0, 360, step=30, every=3, arrow_right=False)
text(ax, 44, 31, 'après ÷ cos x : 2 solutions', 'autre', 's')
for v in (210, 330): disc(ax, f2(v), 18, 2.2, 'resultat')
for v in (90, 270):
    disc(ax, f2(v), 18, 2.2, 'limite', fill=False, lw=1.2)
    text(ax, f2(v), 24, 'perdue', 'limite', 's')
save(fig, '32-122')
