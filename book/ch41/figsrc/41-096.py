import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$OH=u\cdot v\,/\,\|v\|$', 'resultat', 'l')
text(ax, 44, 66, r'pour $u=\langle1,3\rangle$ et $v=\langle4,2\rangle$', 'fixe', 's')
rows = [('1', 'sujet', r'$u\cdot v=1\times4+3\times2=10$'),
        ('2', 'autre', r'$\|v\|=\sqrt{20}\approx4{,}472$'),
        ('3', 'resultat', r'$10\div4{,}472\approx2{,}236$')]
y = 60
for n, role, expr in rows:
    y -= 13
    box(ax, 22, y, 62, 11, role, label=expr, size='s')
    text(ax, 10, y + 5.5, n, role, 'l')
    arrow(ax, (50, y), (50, y - 4), 'fixe', lw=0.8) if n != '3' else None
    y -= 3
text(ax, 44, 4, 'aucun angle dans le calcul', 'varie', 's')
save(fig, '41-096')
