import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 3, 74, 'les entiers', 'sujet', 'm', ha='left')
f = numberline(ax, 8, 70, 66, 0, 6, role='sujet')
disc(ax, f(5), 66, 2.2, 'sujet', fill=True)
text(ax, 3, 50, 'cadran à 4 heures', 'autre', 'm', ha='left')
for i in range(4):
    disc(ax, 14 + i * 14, 40, 4.5, 'autre' if i == 3 else 'fixe', label=str(i), size='m')
box(ax, 20, 8, 22, 12, 'sujet', label='5', size='l')
box(ax, 42, 8, 22, 12, 'autre', label='3', size='l')
text(ax, 18, 14, '(', 'encre', 'xl', ha='right'); text(ax, 66, 14, ')', 'encre', 'xl', ha='left')
text(ax, 31, 3.5, 'place dans les entiers', 'sujet', 's'); text(ax, 53, 24.5, 'place dans le cadran', 'autre', 's')
save(fig, '51-051')
