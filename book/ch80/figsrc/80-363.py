import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 13.5, 82, r'$U$', 'sujet', 'm'); text(ax, 43.5, 82, r'$V$', 'autre', 'm')
text(ax, 68, 82, r'$\mu(U,V)$', 'resultat', 'm')
rows = [('000', '110', r'$(-1)^2=1$'), ('010', '011', r'$(-1)^1=-1$'), ('101', '101', r'$(-1)^0=1$')]
dw = 2.02
for r, (u, v, res) in enumerate(rows):
    y = 58 - r * 24
    box(ax, 6, y, 15, 10, 'sujet', label=u, size='l')
    box(ax, 36, y, 15, 10, 'autre', label=v, size='l')
    arrow(ax, (22.5, y + 5), (34.5, y + 5), 'fixe')
    for i in range(3):
        if u[i] == '0' and v[i] == '1':
            mx = 43.5 + (i - 1) * dw
            poly(ax, [(mx - 0.9, y + 1.0), (mx + 0.9, y + 1.0), (mx, y + 2.6)], 'varie')
    text(ax, 56, y + 5, res, 'resultat', 'm', ha='left')
poly(ax, [(6, 3.2), (8.2, 3.2), (7.1, 5.2)], 'varie')
text(ax, 10.5, 4, 'chiffre qui monte de 0 à 1', 'varie', 's', ha='left')
save(fig, '80-363')
