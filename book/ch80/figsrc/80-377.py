import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, r'$24-24+12-4+1=9$', 'resultat', 'l')
for i in range(24):
    r, c = divmod(i, 6)
    box(ax, 4 + c * 6.8, 22 - r * 0 + (3 - r) * 6.8 - 2, 6, 6, 'resultat' if i < 9 else 'fixe', r=0.5)
box(ax, 50, 28, 5, 5, 'resultat', r=0.5); text(ax, 57, 30.5, '9 : personne n’a le sien', 'resultat', 's', ha='left')
box(ax, 50, 18, 5, 5, 'fixe', r=0.5); text(ax, 57, 20.5, '15 : au moins un l’a', 'fixe', 's', ha='left')
text(ax, 25, 4, '24 façons en tout', 'fixe', 's')
save(fig, '80-377')
