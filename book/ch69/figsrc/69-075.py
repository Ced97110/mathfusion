import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx = [42, 60, 78]
for x, h in zip(cx, [r'$x<1$', r'$x=1$', r'$x>1$']):
    text(ax, x, 66, h, 'encre', 'm')
text(ax, 2, 51, 'avec −reste\n(Sturm)', 'resultat', 'm', ha='left')
text(ax, 2, 25, 'avec le reste\nordinaire', 'autre', 'm', ha='left')
sturm = ['− − +\nV = 1', '− 0 +\nV = 1', '− + +\nV = 1']
ordi = ['− − −\nV = 0', '− 0 −\nV = 0', '− + −\nV = 2']
for k, x in enumerate(cx):
    box(ax, x - 8, 42, 16, 18, 'resultat', label=sturm[k])
    box(ax, x - 8, 16, 16, 18, 'limite' if k == 2 else 'autre', label=ordi[k])
text(ax, 60, 7, r'signes de $f_0$, $f_1$, $f_2$', 'fixe', 's')
save(fig, '69-075')
