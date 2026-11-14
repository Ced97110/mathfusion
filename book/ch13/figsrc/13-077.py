import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
yt, yb = 56, 16
ft = numberline(ax, 8, 72, yt, -4.5, 4.5, labels=False, arrow_right=False)
fb = numberline(ax, 8, 72, yb, -4.5, 4.5, labels=False, arrow_right=False)
line(ax, [(ft(0), yb + 3), (ft(0), yt - 3)], 'fixe', dash=True)
for v, name in ((-3, 'B'), (0, 'O'), (2, 'A')):
    disc(ax, ft(v), yt, 2.4, 'sujet', label=f'${name}$', size='s')
    text(ax, ft(v), yt + 5.5, f'${v}$', 'sujet', 's')
for v, name in ((3, 'B'), (0, 'O'), (-2, 'A')):
    disc(ax, fb(v), yb, 2.4, 'resultat', label=f"${name}'$", size='s')
    text(ax, fb(v), yb - 5.5, f'${v}$', 'resultat', 's')
arrow(ax, (ft(2), yt - 3), (fb(-2), yb + 3), 'varie')
arrow(ax, (ft(-3), yt - 3), (fb(3), yb + 3), 'varie')
text(ax, ft(0) + 2, 36, 'miroir en 0', 'fixe', 's', ha='left')
save(fig, '13-077')
