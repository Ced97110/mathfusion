import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 12, 76, 50, 0, 2, 1, arrow_right=False)
f2 = numberline(ax, 12, 76, 16, 0, 2, 1, arrow_right=False)
r = 2 ** 0.5
text(ax, 4, 64, 'dans ℝ : vrai', 'resultat', 'm', ha='left', weight='bold')
disc(ax, f(r), 50, 2.2, 'resultat'); text(ax, f(r), 57, '√2', 'resultat', 's')
text(ax, 4, 30, 'dans ℚ : faux', 'limite', 'm', ha='left', weight='bold')
for k in range(25):
    disc(ax, f2(k / 12), 16, 0.8, 'sujet')
disc(ax, f2(r), 16, 2.2, 'limite', fill=False)
text(ax, f2(r), 23, 'rien ici', 'limite', 's')
save(fig, '42-095')
