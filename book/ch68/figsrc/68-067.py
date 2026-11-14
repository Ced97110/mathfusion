import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [(3, 1, 'répétition triple'), (8, 7, 'bit de parité'), (7, 4, 'code de Hamming')]
sq, g, x0 = 4.5, 1.0, 30
for r, (n, k, name) in enumerate(rows):
    yc = 46 - r * 15
    text(ax, 14, yc + 2.5, f'$({n},\\ {k})$', 'sujet', 'l')
    text(ax, 14, yc - 4, name, 'fixe', 's')
    for i in range(n):
        x = x0 + i * (sq + g)
        poly(ax, [(x, yc - sq / 2), (x + sq, yc - sq / 2), (x + sq, yc + sq / 2), (x, yc + sq / 2)], 'sujet' if i < k else 'varie')
    text(ax, x0 + n * (sq + g) + 2, yc, f'$n={n}$', 'fixe', 's', ha='left')
for x, role, lab in [(4, 'sujet', r'$k$ : bits du bloc'), (46, 'varie', r'$n-k$ : ajoutés')]:
    poly(ax, [(x, 2), (x + 4.5, 2), (x + 4.5, 6.5), (x, 6.5)], role)
    text(ax, x + 6.5, 4.25, lab, role, 's', ha='left')
save(fig, '68-067')
