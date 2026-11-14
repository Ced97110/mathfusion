import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# (7+2i)(2-i) = 14 - 7i + 4i - 2i^2 = 16 - 3i ; (2+i)(2-i) = 4 + 1 = 5
z = (7 + 2j) * (2 - 1j); assert z == 16 - 3j and (2 + 1j) * (2 - 1j) == 5
text(ax, 15, 38, r'$\frac{7+2i}{2+i}$', 'sujet', 'xl')
text(ax, 32, 38, r'$\times$', 'fixe', 'l')
text(ax, 48, 38, r'$\frac{2-i}{2-i}$', 'varie', 'xl')
text(ax, 63, 38, '=', 'fixe', 'l')
text(ax, 77, 38, r'$\frac{16-3i}{5}$', 'resultat', 'xl')
text(ax, 15, 28, r'$a/b$', 'sujet', 's')
text(ax, 48, 28, 'conjugué de $b$', 'varie', 's')
text(ax, 77, 28, 'quotient exact', 'resultat', 's')
text(ax, 44, 16, r'haut : $(7+2i)(2-i)=16-3i$', 'resultat', 's')
text(ax, 44, 8, r'bas : $(2+i)(2-i)=4+1=5$', 'resultat', 's')
save(fig, '56-175')
