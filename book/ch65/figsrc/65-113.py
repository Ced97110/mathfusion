import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cxs = (18, 44, 70)
roots = (r'$y_1=-3$', r'$y_2=1$', r'$y_3=2$')
for c, r in zip(cxs, roots):
    box(ax, c - 11, 57, 22, 9, 'fixe', label=r, size='s')
rowA = (r'$\times 1$', r'$\times 1$', r'$\times 1$')
rowB = (r'$\times 1$', r'$\times w$', r'$\times w^2$')
for c, a, b, rb in zip(cxs, rowA, rowB, ('sujet', 'varie', 'varie')):
    box(ax, c - 11, 43, 22, 9, 'fixe', label=a, size='s')
    box(ax, c - 11, 19, 22, 9, rb, label=b, size='s')
box(ax, 7, 33, 74, 8, 'fixe', label=r'somme : $-3+1+2=0$', size='s')
box(ax, 7, 7, 74, 10, 'sujet', label=r'$z_1=-3+w+2w^2=-5-w$', size='s')
save(fig, '65-113')
