import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(r'$\sin(A+B)=$', 'sujet', r'$\sin A\cos B$', 'sujet', r'$+\cos A\sin B$', 'limite'),
        (r'$\sin(A-B)=$', 'autre', r'$\sin A\cos B$', 'autre', r'$-\cos A\sin B$', 'limite'),
        ('somme :', 'resultat', r'$2\sin A\cos B$', 'resultat', '0 : disparaît', 'limite')]
for i, (lab, lr, t1, r1, t2, r2) in enumerate(rows):
    y = 52 - 17 * i
    text(ax, 2, y + 5, lab, lr, 's', ha='left')
    box(ax, 29, y, 27, 10, r1, label=t1, size='s'); box(ax, 58, y, 28, 10, r2, label=t2, size='s')
text(ax, 44, 48.5, '+', 'varie', 'xl', weight='bold')
line(ax, [(2, 31.5), (86, 31.5)], 'varie', 1.0)
for yy in (52, 35):
    line(ax, [(61, yy + 5), (83, yy + 5)], 'encre', 0.6)
text(ax, 44, 11.5, r'$60^\circ,\ 30^\circ:\ 0{,}75+0{,}25=1\ ;\ 0{,}75-0{,}25=0{,}5$', 'fixe', 's')
text(ax, 44, 5, r'$1+0{,}5=2\times0{,}75$', 'fixe', 's')
save(fig, '35-048')
