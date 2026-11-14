import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
f = numberline(ax, 14, 74, 66, -2, 2, 1, arrow_right=False, labels=False)
disc(ax, f(0), 66, 1.5, 'sujet')
text(ax, f(0), 74, r'$f=x^2$ : seule racine $0$', 'sujet', 's')
text(ax, f(0), 58, r'$g(0)=0$ : $0$ est interdit', 'limite', 's')
box(ax, 3, 6, 40, 38, 'limite', label='exposant 1 :\n$g=x$\n$x^2$ ne divise pas $x$\nsolution annoncée\n(fausse)', size='s')
box(ax, 45, 6, 40, 38, 'resultat', label='exposant $h=2$ :\n$g^2=x^2$\n$x^2$ divise $x^2$\naucune solution\n(juste)', size='s')
save(fig, '70-133')
