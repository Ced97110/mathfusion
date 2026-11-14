import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 26
f = numberline(ax, 6, 70, y, 0, 2.5, step=0.5)
a = math.sqrt(5); b = a - 1; c = b / 4
disc(ax, f(a), y, 1.5, 'sujet'); disc(ax, f(b), y, 1.5, 'varie'); disc(ax, f(c), y, 1.5, 'resultat')
text(ax, f(a), 46, r'$\sqrt{5}\approx2{,}236$', 'sujet', 's')
text(ax, f(b), 46, r'$\approx1{,}236$', 'varie', 's')
text(ax, f(c), 46, r'$c\approx0{,}309$', 'resultat', 's')
arrow(ax, (f(a), y + 3), (f(b), y + 3), 'varie', curve=0.5)
arrow(ax, (f(b), y + 3), (f(c), y + 3), 'varie', curve=0.5)
text(ax, (f(a) + f(b)) / 2, y + 12, r'$-1$', 'varie', 'm')
text(ax, (f(b) + f(c)) / 2, y + 12, r'$\div4$', 'varie', 'm')
text(ax, 44, 7, r'$c=(\sqrt{5}-1)/4$', 'resultat', 'l')
save(fig, '66-018')
