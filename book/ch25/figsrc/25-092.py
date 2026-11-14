import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
f = numberline(ax, 6, 76, 62, 0, 90, step=10, every=3, arrow_right=False)
for a in (0, 10, 20, 30, 40, 45, 50, 60, 70, 80, 85):
    disc(ax, f(a), 62, 1.2, 'sujet')
disc(ax, f(25), 62, 1.2, 'limite', fill=False)
line(ax, [(f(90), 59), (f(90), 65)], 'limite', lw=1.2)
text(ax, 44, 74, 'onze angles seulement', 'sujet', 's')
rows = [('10°', '0,1763', 'sujet'), ('25°', 'absent', 'limite'), ('40°', '0,8391', 'sujet'), ('80°', '5,6713', 'sujet')]
for i, (a, v, r) in enumerate(rows):
    y = 40 - i * 11
    dash = (r == 'limite')
    box(ax, 14, y, 24, 9, r, label=a, dash=dash)
    box(ax, 38, y, 36, 9, r, label=v, dash=dash)
save(fig, '25-092')
