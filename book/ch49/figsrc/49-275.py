import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 28, 50, 15, 'fixe')
rots = ['1', r'$r$', r'$r^2$', r'$r^3$']
for i, l in enumerate(rots):
    role = 'sujet' if i in (1, 3) else 'fixe'
    disc(ax, 8.5+i*12, 35.5, 4.4, role, label=l, size='s')
text(ax, 27, 47, 'commutent avec r : 4', 'fixe', 'm')
refl = [r'$s$', r'$rs$', r'$r^2s$', r'$r^3s$']
for i, l in enumerate(refl):
    disc(ax, 8.5+i*12, 14, 4.4, 'fixe', fill=False, label=l, size='s')
text(ax, 27, 5, 'les 4 autres', 'fixe', 's')
box(ax, 58, 28, 28, 15, 'sujet', label='classe : 2')
box(ax, 58, 8, 28, 12, 'resultat', label=r'2 $\times$ 4 = 8', weight='bold')
save(fig, '49-275')
