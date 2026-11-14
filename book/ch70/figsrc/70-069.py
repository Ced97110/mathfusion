import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
f = numberline(ax, 8, 70, 22, -2, 3, arrow_right=True)
r2 = 2 ** 0.5
for v in (-2, 0, 1, 1.5):
    disc(ax, f(v), 22, 1.0, 'sujet')
disc(ax, f(r2), 22, 1.0, 'autre')
line(ax, [(f(r2), 23.2), (f(r2), 29)], 'autre')
text(ax, f(r2) + 2, 31.5, r'$\sqrt{2}$ : pas une fraction', 'autre', 's')
line(ax, [(f(1.5), 20.8), (f(1.5), 12)], 'sujet')
text(ax, f(1.5), 9.5, '1,5', 'sujet', 's')
brace(ax, f(-2) - 1, f(3) + 1, 38, 'sujet', label='ℝ : tous les points', down=False, size='m')
save(fig, '70-069')
