import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 31, 47, 'discriminant', 'autre', 's')
text(ax, 76, 47, 'déterminant', 'sujet', 's')
for y, lab, d, t in [(26, 'cas 5, 6, 5', '−64', '16'), (4, 'cas 1, 4, 1', '12', '−3')]:
    text(ax, 2, y + 6, lab, 'encre', 's', ha='left')
    box(ax, 22, y, 18, 12, 'autre', label=d, size='l')
    box(ax, 68, y, 18, 12, 'sujet', label=t, size='l')
    arrow(ax, (40, y + 6), (68, y + 6), 'varie')
    text(ax, 54, y + 10.5, 'opposé, divisé par 4', 'varie', 's')
save(fig, '71-180')
