import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
disc(ax, 14, 36, 7, 'sujet', label='12', size='l'); disc(ax, 74, 36, 7, 'autre', label='20', size='l')
arrow(ax, (23, 41), (65, 41), 'limite'); arrow(ax, (65, 31), (23, 31), 'limite')
text(ax, 44, 46, '20 ÷ 12 ≈ 1,67', 'limite', 's'); text(ax, 44, 26, '12 ÷ 20 = 0,6', 'limite', 's')
text(ax, 44, 36, 'pas entiers', 'limite', 's')
box(ax, 18, 4, 52, 9, 'fixe', label='12 et 20 incomparables')
save(fig, '79-003')
