import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cols = [(32, r'$v_1=1$', ['1', r'$\sqrt{3}$']), (54, r'$v_2=\sqrt{2}$', [r'$\sqrt{2}$', r'$\sqrt{6}$'])]
rows = [(34, r'$w_1=1$'), (18, r'$w_2=\sqrt{3}$')]
for x, h, vals in cols:
    text(ax, x + 10, 54, h, 'sujet', 's')
    for (y, _), v in zip(rows, vals):
        box(ax, x, y, 20, 14, 'resultat', label=v, size='m')
for y, h in rows:
    text(ax, 16, y + 7, h, 'autre', 's')
text(ax, 44, 8, r'$m\times r=2\times2=4$ produits', 'resultat', 'm')
save(fig, '61-104')
