import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 22, 64, 'on connaît', 'fixe', 's'); text(ax, 68, 64, 'il recevra un nom', 'fixe', 's')
rows = [(r'$U(8)$ : 1, 3, 5, 7', "fonction d'Euler,\nFermat"),
        (r'$3\times4\equiv0$ (mod 12)', 'diviseurs de zéro'),
        (r'$\mathbb{Z}_p$, $p$ premier', 'corps'),
        ('puissance, retour', 'RSA')]
for i, (a, b) in enumerate(rows):
    y = 52 - i * 14
    box(ax, 2, y - 5.5, 42, 11, 'sujet', label=a, size='s')
    box(ax, 56, y - 5.5, 30, 11, 'autre', label=b, size='s')
    arrow(ax, (44.5, y), (55.5, y), 'varie')
save(fig, '44-274')
