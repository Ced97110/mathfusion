import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'nombres complexes : 1 nombre nouveau', 'fixe', 's')
box(ax, 31, 40, 26, 12, 'fixe', label=r'$i^2=-1$', size='l')
text(ax, 44, 34, r'$x^2=-1$ : $i$ et $-i$', 'fixe', 's')
line(ax, [(2, 29), (86, 29)], 'fixe', dash=True, lw=0.5)
text(ax, 44, 24, 'quaternions : 3 nombres nouveaux', 'sujet', 's')
for k, (x, name) in enumerate(zip((4, 32, 60), ('i', 'j', 'k'))):
    box(ax, x, 5, 24, 12, 'sujet', label=r'$%s^2=-1$' % name, size='l')
save(fig, '39-139')
