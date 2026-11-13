import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 2, 3, 84, 54, 'sujet', True, lw=1.2)
text(ax, 44, 51, r'Formule : $ax^2+bx+c=0$', 'sujet', 'm')
for cx in (18, 45, 72): arrow(ax, (cx, 46.5), (cx, 42.6), 'sujet')
for x, s in [(6, 'Racine\ncarrée\n' + r'$x^2=49$'), (33, 'Factorisation\n' + r'$x(x+1)=156$'), (60, 'Compléter\nle carré\n' + r'$x^2+6x+9$')]:
    box(ax, x, 8, 24, 34, 'fixe', True, label=s, size='s')
save(fig, '23-007')
