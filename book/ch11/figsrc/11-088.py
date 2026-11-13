import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(76)
xs = [16, 44, 72]; ds = [20, 25, 30]; Cs = ['62,8', '78,5', '94,2']; k = 0.6
for x, dd, c in zip(xs, ds, Cs):
    disc(ax, x, 62, dd * k / 2, 'sujet'); ring(ax, x, 62, dd * k / 2, 'sujet', 1.2)
    text(ax, x, 46, f'$d$ = {dd}', 'sujet', 's'); text(ax, x, 42.5, f'$C$ = {c}', 'sujet', 's')
    box(ax, x - 13, 28, 26, 7, 'resultat', label=f'{c} ÷ {dd} = 3,14'.replace('÷', r'$\div$'), size='s')
    arrow(ax, (x, 28), (44, 20), 'resultat', lw=0.8)
box(ax, 18, 4, 52, 16, 'sujet', label=r'$\pi$ = $C$ $\div$ $d$ = 3,14…', size='m', weight='bold')
save(fig, '11-088')
