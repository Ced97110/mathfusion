import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
f = numberline(ax, 10, 78, 40, 0, 4, 1, labels=False, arrow_right=False)
text(ax, 44, 74, r'$p(x)=(x-2)(x-1)(x-3)$', 'sujet', 'm')
for v in (1, 2, 3):
    disc(ax, f(v), 40, 1.3, 'sujet')
    text(ax, f(v), 36, str(v), 'sujet', 's')
for (a, b, sg, role) in ((0, 1, '−', 'fixe'), (1, 2, '+', 'resultat'), (2, 3, '−', 'fixe'), (3, 4, '+', 'resultat')):
    box(ax, f(a) + 1.5, 44, f(b) - f(a) - 3, 8, role, label=sg, size='l')
disc(ax, f(1.5), 40, 0.9, 'varie'); disc(ax, f(2.5), 40, 0.9, 'varie')
arrow(ax, (f(1.5), 53), (f(1.5), 58), 'varie', lw=0.9)
arrow(ax, (f(2.5), 53), (f(2.5), 58), 'varie', lw=0.9)
text(ax, f(1.5) - 5, 62, r'$p(1{,}5)=0{,}375$', 'varie', 's')
text(ax, f(2.5) + 5, 62, r'$p(2{,}5)=-0{,}375$', 'varie', 's')
brace(ax, f(1), f(3), 31, 'limite', '1 et 3 : pas consécutives')
save(fig, '70-138')
