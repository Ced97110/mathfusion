import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# forme générale
text(ax, 44, 75, r'$f=q\,g+r$', 'encre', 'xl')
box(ax, 20, 56, 12, 10, 'sujet', label=r'$f$', size='l')
text(ax, 38, 61, '=', 'fixe', 'l')
for x, s in [(44, r'$q$'), (56, r'$g$'), (68, r'$r$')]:
    box(ax, x, 56, 10, 10, 'fixe', label=s, size='l')
text(ax, 26, 51, 'dividende', 'sujet', 's')
# entiers
text(ax, 4, 41, 'Entiers', 'fixe', 's', ha='left')
box(ax, 4, 28, 14, 9, 'sujet', label='156')
text(ax, 21, 32.5, '=', 'fixe')
text(ax, 44, 32.5, r'$13\times12+0$', 'fixe')
# polynômes
text(ax, 4, 20, 'Polynômes', 'fixe', 's', ha='left')
box(ax, 4, 6, 30, 9, 'sujet', label=r'$x^3-2x^2+4$')
text(ax, 38, 10.5, '=', 'fixe')
text(ax, 64, 10.5, r'$(x^2-x-1)(x-1)+3$', 'fixe', 's')
save(fig, '54-149')
