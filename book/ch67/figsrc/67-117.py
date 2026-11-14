import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
c = 8; x0 = 8; y = 38
blocks = [1, 1, 1, 2, 2, 2]
x = x0
for d in blocks:
    box(ax, x + 0.4, y, d * c - 0.8, 11, 'sujet' if d == 1 else 'varie', label=str(d), size='s', r=0.4)
    x += d * c
brace(ax, x0, x0 + 9 * c, y + 11, 'fixe', label=r'degré $q^n=3^2=9$', down=False)
brace(ax, x0, x0 + 3 * c, y, 'sujet', label='3 de degré 1 : 3', down=True)
brace(ax, x0 + 3 * c, x0 + 9 * c, y, 'varie', label=r'$N(2,3)$ de degré 2 : 6', down=True)
text(ax, 44, 12, r'$3+2N(2,3)=9$', 'encre', 'l')
text(ax, 44, 3, r'donc $N(2,3)=3$', 'resultat', 'm')
save(fig, '67-117')
