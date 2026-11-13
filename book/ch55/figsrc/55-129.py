import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
x, y, z = 1, 2, 4
e1 = x + y + z
e2 = x * y + x * z + y * z
assert (e1, e2) == (7, 14) and x * x + y * y + z * z == 21 == e1 ** 2 - 2 * e2 and 49 - 28 == 21
box(ax, 3, 90, 82, 8, 'autre', label=r'2 variables : $x^2+y^2=e_1^2-2e_2$', size='s')
box(ax, 3, 79, 82, 8, 'sujet', label=r'3 variables : $x^2+y^2+z^2=e_1^2-2e_2$', size='s')
for c, lab in zip((16, 44, 72), (r'$x=1$', r'$y=2$', r'$z=4$')):
    disc(ax, c, 64, 6, 'sujet', label=lab, size='s')
box(ax, 3, 38, 40, 11, 'varie', label=r'$e_1=1+2+4=7$', size='s')
box(ax, 45, 38, 41, 11, 'varie', label=r'$e_2=2+4+8=14$', size='s')
arrow(ax, (18, 57.5), (20, 49.5), 'varie')
arrow(ax, (70, 57.5), (68, 49.5), 'varie')
arrow(ax, (23, 37.5), (32, 31.5), 'varie')
arrow(ax, (65, 37.5), (56, 31.5), 'varie')
box(ax, 4, 20, 80, 11, 'resultat', label=r'$e_1^2-2e_2=49-28=21$', size='m')
text(ax, 44, 16, r'$=$', 'resultat', 'l')
box(ax, 4, 3, 80, 10, 'resultat', label=r'contrôle : $1+4+16=21$', size='m')
save(fig, '55-129')
