import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 78, 8, -6, 12, step=1, arrow_right=False, every=3)
text(ax, 2, 56, 'I : multiples de 4', 'fixe', 's', ha='left')
for v in (-4, 0, 4, 8, 12): disc(ax, f(v), 48, 1.6, 'fixe')
for a in (-4, 0, 4, 8):
    arrow(ax, (f(a) + 0.5, 45.5), (f(a + 3) - 0.5, 27), 'varie')
for v in (-5, -1, 3, 7, 11): disc(ax, f(v), 24, 1.6, 'sujet')
text(ax, f(-5.2), 36, '+ 3', 'varie', 's')
text(ax, 2, 15, 'a + I = 3 + I : reste 3', 'sujet', 's', ha='left')
save(fig, '52-064')
