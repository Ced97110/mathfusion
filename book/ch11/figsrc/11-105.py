import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def grid(ax, x, y, n, m, c, role, lw=0.35):
    for i in range(n):
        for j in range(m):
            poly(ax, [(x+i*c, y+j*c), (x+(i+1)*c, y+j*c), (x+(i+1)*c, y+(j+1)*c), (x+i*c, y+(j+1)*c)], role, lw=lw)
fig, ax = canvas(52)
c = 4
xs = {2: 6, 3: 22, 5: 46}
for n, x in xs.items():
    grid(ax, x, 18, n, n, c, 'sujet')
    text(ax, x + n * c / 2, 13, f'$c$ = {n}', 'varie', 's')
    text(ax, x + n * c / 2, 8, f'{n} × {n} = {n * n}', 'resultat', 's', weight='bold')
text(ax, 44, 46, r'$A$ = $c$ × $c$ = $c^2$', 'sujet', 'l')
save(fig, '11-105')
