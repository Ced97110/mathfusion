import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'racines 2 et 3 : $(2-3)^2=1$', 'sujet', 'l')
s = 9.0
for i in range(4):
    box(ax, 3 + i * (s + 2), 26, s, s, 'sujet', label='1', lw=0.9, r=0.6)
brace(ax, 3, 3 + 4 * s + 6, 26, 'varie', label=r'$a^2=2^2=4$ carrés', down=True)
text(ax, 54, 30.5, '=', 'encre', 'xl')
box(ax, 60, 21, 26, 19, 'resultat', label='$b^2-4ac$\n$=100-96$\n$=4$', size='s')
text(ax, 44, 8, 'le discriminant de $2x^2-10x+12$', 'fixe', 's')
save(fig, '55-115')
