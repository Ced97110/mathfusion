import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# p = 2 : exponents 0..4 ; only multiples of p carry a coefficient
text(ax, 44, 58, r'$p=2$ : $f=b_0+b_1x^2+b_2x^4$', 'encre', 'm')
names = [r'$b_0$', '', r'$b_1$', '', r'$b_2$']
for e in range(5):
    x = 5 + e * 15.5
    on = e % 2 == 0
    box(ax, x, 32, 13.5, 12, 'sujet' if on else 'fixe', label=names[e] if on else None, fill=on, dash=not on)
    text(ax, x + 6.75, 27, r'$x^{%d}$' % e, 'sujet' if on else 'fixe', 's')
text(ax, 44, 50, 'puissances de $x^p$ seulement', 'sujet', 's')
arrow(ax, (44, 21), (44, 14.5), 'resultat')
box(ax, 22, 3, 44, 11, 'resultat', label=r'$f^{\prime}=0$')
save(fig, '62-110')
