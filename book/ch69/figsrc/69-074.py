import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [16, 40, 64]
f_row = [('resultat', r'$x-1$'), ('fixe', r'$x-1$'), ('fixe', r'$x+2$')]
g_row = [('resultat', r'$x-1$'), ('fixe', r'$x+1$'), ('fixe', r'$3$')]
text(ax, 8, 53, r'$f$', 'sujet', 'l')
text(ax, 8, 35, r"$f'$", 'sujet', 'l')
for x, (r1, l1), (r2, l2) in zip(xs, f_row, g_row):
    box(ax, x, 48, 20, 10, r1, label=l1)
    box(ax, x, 30, 20, 10, r2, label=l2)
arrow(ax, (26, 48), (26, 40.5), 'resultat', both=True)
text(ax, 29, 44.2, 'facteur commun', 'resultat', 's', ha='left')
arrow(ax, (26, 30), (26, 20.5), 'resultat')
box(ax, 10, 6, 68, 14, 'resultat', label=r'dernier terme $f_s=2(x-1)$' + '\n' + r"PGCD de $f$ et $f'$ (au signe près)")
save(fig, '69-074')
