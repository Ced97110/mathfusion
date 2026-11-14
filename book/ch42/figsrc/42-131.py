import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 3, 4, 82, 44, 'fixe', fill=False, lw=1.0)
text(ax, 10, 43, r'$U$', 'fixe', 'l', weight='bold')
for i in range(3):
    disc(ax, 13 + i * 10, 30, 4, 'fixe', label=str(i + 1))
    disc(ax, 55 + i * 10, 30, 4, 'sujet', label=str(i + 4))
box(ax, 7, 22, 32, 16, 'fixe', fill=False, dash=True)
box(ax, 49, 22, 32, 16, 'sujet', fill=False, dash=True)
text(ax, 23, 17, r'$A$', 'fixe', 'l')
text(ax, 65, 17, r"$A'$ (A prime)", 'sujet', 'l')
text(ax, 44, 9, 'le reste de U, hors de A', 'sujet', 's')
save(fig, '42-131')
