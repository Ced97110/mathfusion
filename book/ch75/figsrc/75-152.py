import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# the data: table h, arrows a and b
for (cx, cy, v) in ((4, 71, '1'), (16, 71, r'$i$'), (4, 62, r'$-i$'), (16, 62, '1')):
    box(ax, cx, cy, 11, 8, 'sujet', label=v, size='s')
text(ax, 62, 67, r'$a=(1,\ 1)\ \ b=(1,\ 0)$', 'encre', 's')
rows = [('(1, 1)', r'$h_{11}a_1\bar b_1=1\times1\times1=1$'), ('(1, 2)', r'$h_{12}a_1\bar b_2=i\times1\times0=0$'),
        ('(2, 1)', r'$h_{21}a_2\bar b_1=-i\times1\times1=-i$'), ('(2, 2)', r'$h_{22}a_2\bar b_2=1\times1\times0=0$')]
for k, (c, e) in enumerate(rows):
    y = 48 - k * 11
    box(ax, 2, y, 17, 9, 'fixe', label=c, size='s')
    arrow(ax, (20, y + 4.5), (24, y + 4.5), 'fixe')
    box(ax, 25, y, 61, 9, 'sujet', label=e, size='s')
box(ax, 25, 2, 61, 10, 'resultat', label=r'somme : $1+0-i+0=1-i$', size='s', weight='bold')
save(fig, '75-152')
