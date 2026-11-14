import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x0, cw, ch, ytop = 14, 16, 10, 52
cell = {(n % 3, n % 4): n for n in range(12)}
text(ax, x0 + (cw - 1) / 2, ytop + 3.5, 'Dy', 'sujet', 'm', weight='bold')
text(ax, 6.5, ytop - ch / 2, 'Dz', 'autre', 'm', weight='bold')
text(ax, 75, 38, '0 : seule case\ncommune', 'resultat', 's')
for (c, r), n in cell.items():
    role = 'fixe'
    if c == 0: role = 'sujet'
    if r == 0: role = 'autre'
    if n == 0: role = 'resultat'
    if n == 7: role = 'varie'
    box(ax, x0 + cw * c, ytop - ch * (r + 1) + 0, cw - 1, ch - 1, role, label=str(n), r=0.5)
text(ax, 75, 24, '7 = 3 + 4', 'varie', 'm')
text(ax, 75, 17, 'colonne + ligne', 'varie', 's')
save(fig, '60-051')
