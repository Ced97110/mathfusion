import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# U dans Z
text(ax, 6, 62, 'Dans ℤ :', 'encre', 'm', ha='left')
box(ax, 26, 57, 36, 10, 'sujet', label='U = {1, −1}')
f = numberline(ax, 12, 76, 42, -3, 3, arrow_right=False)
for v in range(-3, 4):
    if v in (-1, 1):
        disc(ax, f(v), 42, 2.6, 'sujet')
    elif v != 0:
        disc(ax, f(v), 42, 1.2, 'fixe')
arrow(ax, (f(1), 56), (f(1), 46), 'sujet')
arrow(ax, (f(-1), 56), (f(-1), 46), 'sujet')
# U dans les fractions
text(ax, 6, 22, 'Fractions :', 'encre', 'm', ha='left')
box(ax, 26, 17, 40, 10, 'sujet', label='U = tout sauf 0')
x0, x1 = 6, 82
line(ax, [(x0, 6), (44 - 1.5, 6)], 'sujet', lw=2.0)
line(ax, [(44 + 1.5, 6), (x1, 6)], 'sujet', lw=2.0)
disc(ax, 44, 6, 1.4, 'limite', fill=False)
text(ax, 44, 1.8, '0', 'limite', 's')
save(fig, '56-033')
