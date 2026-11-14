import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'on remplace $x$ par 3', 'sujet', 'm')
box(ax, 2, 42, 30, 10, 'fixe', label=r'$x^3-1=26$')
box(ax, 35, 42, 28, 10, 'varie', label=r'$\div\ (x-1)=2$')
box(ax, 66, 42, 20, 10, 'resultat', label=r'$=13$')
arrow(ax, (63, 47), (66, 47), 'varie')
u = 5.0
x0 = 9.0
terms = [(r'$x^2=9$', 9), (r'$x=3$', 3), ('1', 1)]
x = x0
for lab, v in terms:
    box(ax, x, 14, v * u, 10, 'resultat', label=lab, r=0.5)
    x += v * u
brace(ax, x0, x0 + 13 * u, 12, 'fixe', label=r'$x^2+x+1=13$')
arrow(ax, (76, 41), (71, 25.5), 'resultat', curve=0.0)
text(ax, 80, 33, 'égal', 'resultat', 's')
save(fig, '66-045')
