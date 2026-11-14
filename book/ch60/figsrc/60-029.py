import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'deux écritures du même groupe', 'encre', 's')
box(ax, 8, 46, 24, 10, 'fixe', label='ℤ/12', size='m'); box(ax, 52, 46, 30, 10, 'fixe', label='ℤ/4 ⊕ ℤ/3', size='m')
box(ax, 22, 10, 20, 10, 'sujet', label='ℤ/2²', size='m'); box(ax, 48, 10, 20, 10, 'autre', label='ℤ/3', size='m')
for sx in (20, 67):
    for tx in (32, 58):
        arrow(ax, (sx, 45.5), (tx, 20.5), 'varie', lw=0.9)
text(ax, 44, 36, 'découper', 'varie', 's')
text(ax, 77, 15, 'même\nliste', 'resultat', 'm', weight='bold')
save(fig, '60-029')
