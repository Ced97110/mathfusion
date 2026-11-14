import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
words = ['0000', '0011', '0101', '0110', '1001', '1010', '1100', '1111']
cw, gx = 18, 3.5
for k, wd in enumerate(words):
    r, c = divmod(k, 4)
    role = 'sujet' if k == 0 else ('autre' if k == 1 else 'fixe')
    box(ax, 2 + c * (cw + gx), 40 - r * 14, cw, 9, role, label=wd)
arrow(ax, (11, 50), (32.5, 50), 'varie', curve=-0.5)
text(ax, 21.75, 57, 'distance 2', 'varie', 'm')
text(ax, 44, 17, '28 paires de mots', 'fixe', 'm')
text(ax, 44, 8, r'$d=2$', 'resultat', 'l')
save(fig, '68-060')
