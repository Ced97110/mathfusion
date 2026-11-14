import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 2, 8, 42, 40, 'sujet')
text(ax, 23, 43, r"paquet $3K$", 'sujet', 's')
for i, v in enumerate(['3', '7', '11']):
    disc(ax, 10 + 12 * i, 24, 4, 'sujet', label=v, size='s')
arrow(ax, (46, 28), (66, 28), 'resultat', lw=1.4)
text(ax, 56, 33, r"$\bar f$", 'resultat', 'm')
disc(ax, 76, 28, 4.5, 'resultat', label='3', size='m')
text(ax, 76, 19, "position 3", 'resultat', 's')
text(ax, 54, 8, r"$\bar f(3K)=f(3)$", 'encre', 's')
save(fig, '48-070')
