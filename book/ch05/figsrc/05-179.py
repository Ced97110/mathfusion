import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
yl = 22
f = numberline(ax, 6, 76, yl, -8, 8, 1, labels=False)
for v in range(-8, 9, 2):
    role = 'sujet' if v in (4, 6) else 'resultat'
    disc(ax, f(v), yl, 1.5, role)
for v in (2, 4, 6):
    text(ax, f(v), yl - 4.5, str(v), 'resultat' if v == 2 else 'sujet', 's', weight='bold')
arrow(ax, (f(6), yl + 2.4), (f(2), yl + 2.4), 'varie', curve=0.5)
text(ax, f(4), yl + 10, r'$4\times(-1)+6\times1=2$', 'varie', 's')
brace(ax, f(-8), f(8), yl + 14, 'resultat', 'combinaisons de 4 et de 6', down=False)
brace(ax, f(-8), f(8), yl - 8.5, 'resultat', 'multiples de 2 = PGCD(4, 6)', down=True)
save(fig, '05-179')
