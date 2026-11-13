import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# columns for N rows share one header; Z row has its own labels
x0, dx = 38, 10
text(ax, 2, 56, r'$(\mathbb{Z},\times,1)$', 'sujet', 'm', ha='left')
for i, v in enumerate(range(-2, 3)):
    ok = v in (1, -1)
    disc(ax, x0 + i * dx, 56, 3.6, 'resultat' if ok else 'fixe', label=f'{v}'.replace('-', '−'), size='s')
for i in range(4):
    text(ax, x0 + i * dx, 40, str(i), 'encre', 's')
for y, lab, good in ((29, r'$(\mathbb{N},\times,1)$', 1), (13, r'$(\mathbb{N},+,0)$', 0)):
    text(ax, 2, y, lab, 'sujet', 'm', ha='left')
    for i in range(4):
        disc(ax, x0 + i * dx, y, 3.6, 'resultat' if i == good else 'fixe')
text(ax, 66, 66, 'vert : se défait', 'resultat', 's', ha='left')
text(ax, 66, 3, 'gris : ne se défait pas', 'fixe', 's', ha='right')
save(fig, '44-114')
