import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for i in range(10):
    x = 8 + 8 * i
    r = 'fixe' if i % 2 else ('resultat' if i % 4 == 0 else 'sujet')
    disc(ax, x, 22, 3.4, r, label=str(i), size='s')
disc(ax, 8, 44, 2.6, 'sujet'); text(ax, 13, 44, r"$f^{-1}(\{\bar0,\bar2\})=2$ℤ pairs", 'sujet', 's', ha='left')
disc(ax, 8, 37, 2.6, 'resultat'); text(ax, 13, 37, "noyau 4ℤ : multiples de 4", 'resultat', 's', ha='left')
text(ax, 44, 8, "tout multiple de 4 est pair", 'encre', 's')
save(fig, '48-067')
