import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 6, 61.5, r'$D$ : 16 pièces de 10 centimes', 'sujet', 's', ha='left')
for i in range(16):
    disc(ax, 8 + 4.7 * i, 56, 1.9, 'sujet')
text(ax, 6, 45.5, r'$Q$ : 11 pièces de 25 centimes', 'autre', 's', ha='left')
for i in range(11):
    disc(ax, 8 + 4.7 * i, 40, 1.9, 'autre')
text(ax, 21, 29, 'on compte les pièces', 'fixe', 's')
text(ax, 66, 29, 'on compte les centimes', 'fixe', 's')
box(ax, 3, 14, 36, 10, 'sujet', fill=True, label=r'$D+Q=27$')
box(ax, 46, 14, 39, 10, 'autre', fill=True, label=r'$10D+25Q=435$')
save(fig, '24-060')
