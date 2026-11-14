import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def row(y, k, lab, role):
    for i in range(k):
        disc(ax, 30 + i * 11, y, 4, role, label=str(i), size='s')
    text(ax, 11, y, lab, role, 'l')
row(44, 2, r'$\mathbb{F}_2$', 'sujet')
row(30, 3, r'$\mathbb{F}_3$', 'sujet')
text(ax, 11, 14, r'$\mathbb{F}_q$', 'varie', 'l')
for i in range(3):
    disc(ax, 30 + i * 11, 14, 4, 'varie')
text(ax, 63, 14, '…', 'varie', 'l')
brace(ax, 26, 66, 8, 'varie', label=r'$q$ éléments')
save(fig, '75-058')
