import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 76 / 80; x = 6; y = 26; h = 10
parts = [(25, 'sujet', r'$\|x\|^2$'), (30, 'resultat', r'$2\langle x,y\rangle$'), (25, 'autre', r'$\|y\|^2$')]
for v, role, sym in parts:
    box(ax, x, y, v * s, h, role, label=str(v), r=0.5)
    text(ax, x + v * s / 2, y - 4, sym, role, 's')
    x += v * s
brace(ax, 6, 82, y + h + 1, 'fixe', label=None, down=False)
text(ax, 44, 46, r'$\|x+y\|^2=80$', 'encre', 'l')
text(ax, 44, 11, 'on retire 25 et 25 : il reste 30', 'encre', 's')
text(ax, 44, 5.5, r'la moitié de 30 : $\langle x,y\rangle=15$', 'resultat', 's')
save(fig, '73-090')
