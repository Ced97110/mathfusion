import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 24, 22, 18, 'sujet', label='huit règles', size='m')
box(ax, 31, 24, 22, 18, 'varie', label='une preuve', size='m')
arrow(ax, (24, 33), (31, 33), 'fixe')
names = ['ℤ entiers', 'cadran à 4 h', 'tableaux', 'ℍ quaternions']
for i, nm in enumerate(names):
    y = 52 - i*14
    box(ax, 62, y - 5, 24, 10, 'resultat', label=nm, size='s')
    arrow(ax, (53, 33), (62, y), 'resultat', lw=0.8)
text(ax, 28, 16, r'$0\cdot a=0$', 'encre', 'm')
text(ax, 28, 9, r'$(-a)(-b)=ab$', 'encre', 'm')
text(ax, 13, 23, 'démontrés :', 'fixe', 's')
text(ax, 74, 1.8, 'vrai partout', 'resultat', 's')
save(fig, '51-195')
