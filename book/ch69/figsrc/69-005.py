import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 90, r'$x^3-3x+1$', 'sujet', 'l')
coefs = ['1', '0', '−3', '1']
pows = [r'$x^3$', r'$x^2$', r'$x$', r'$x^0$']
for i in range(4):
    x = 9 + 18 * i
    text(ax, x + 8, 82, pows[i], 'sujet', 's')
    box(ax, x, 70, 16, 8, 'sujet', label=coefs[i])
arrow(ax, (44, 68), (44, 55), 'varie')
text(ax, 50, 61.5, 'nombre fini d’étapes', 'fixe', 's', ha='left')
box(ax, 12, 44, 64, 10, 'varie', label='+ − × ÷ et signe d’un nombre')
arrow(ax, (44, 44), (44, 33), 'varie')
box(ax, 14, 22, 60, 10, 'resultat', label='nombre exact de racines')
text(ax, 44, 12, 'Sturm, années 1830', 'fixe', 's')
save(fig, '69-005')
