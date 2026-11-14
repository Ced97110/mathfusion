import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
steps = [r'$2^2-1=3$ divise $2^4-1=15$',
         r'$y=x^3$ : $y^5-1=(y-1)(y^4+\dots+1)$',
         r'$x^3-1$ divise $x^{15}-1$',
         r'$\times\,x$ : $x^4-x$ divise $x^{16}-x$']
roles = ['fixe', 'varie', 'varie', 'resultat']
ys = [92, 74, 56, 38]
for s, r, y in zip(steps, roles, ys): box(ax, 4, y - 6, 80, 12, r, label=s, size='s')
for y in ys[:3]: arrow(ax, (44, y - 7), (44, y - 11), 'fixe')
for i in range(16): disc(ax, 7 + i * 5.2, 20, 2.2, 'resultat' if i < 4 else 'fixe')
brace(ax, 4.6, 24, 16, 'resultat', label=r'4 racines de $x^4-x$', down=True)
text(ax, 60, 4, r'parmi les 16 de $x^{16}-x$', 'fixe', 's')
save(fig, '67-111')
