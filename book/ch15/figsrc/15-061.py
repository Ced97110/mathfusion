import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for y, pre, n, mean in [(58, 'mono', 1, 'un'), (42, 'bi', 2, 'deux'), (26, 'tri', 3, 'trois'), (10, 'poly', 5, 'plusieurs')]:
    box(ax, 3, y - 4.5, 22, 9, 'sujet', label=pre, size='l')
    for i in range(n): disc(ax, 33 + i * 7.5, y, 2.8, 'varie')
    text(ax, 70, y, mean, 'resultat', 'm', ha='left')
save(fig, '15-061')
