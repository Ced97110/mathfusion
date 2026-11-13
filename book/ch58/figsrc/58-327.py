import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda v: 6 + v * 3.1
text(ax, 44, 62, '4ℤ et 6ℤ dans ℤ', 'encre', 's')
text(ax, 6, 52, '4ℤ', 'sujet', 's', ha='left', weight='bold')
text(ax, 6, 36, '6ℤ', 'autre', 's', ha='left', weight='bold')
for v in range(0, 25):
    if v % 4 == 0:
        disc(ax, f(v), 46, 2.0, 'sujet')
    if v % 6 == 0:
        disc(ax, f(v), 30, 2.0, 'autre')
line(ax, [(f(24), 43.5), (f(24), 32.5)], 'limite', lw=1.4, dash=True)
line(ax, [(f(12), 43.5), (f(12), 32.5)], 'limite', lw=0.8, dash=True)
text(ax, f(24) - 1, 54, '24', 'limite', 's', weight='bold')
text(ax, f(24) - 1, 22, '24', 'limite', 's', weight='bold')
text(ax, f(12), 54, '12', 'limite', 's')
text(ax, f(12), 22, '12', 'limite', 's')
box(ax, 4, 2, 80, 14, 'limite', label='24 = 4 × 6 est multiple de 4 et de 6,\nil n’est pas nul : intersection ≠ {0}', size='s')
save(fig, '58-327')
