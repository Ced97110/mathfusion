import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
labs = [r'$x^3-3x+1$', r'$3x^2-3$', r'$2x-1$', '9/4']
text(ax, 44, 70, 'reste : signe renversé', 'varie', 'm')
for i in range(4):
    x = 3 + 21 * i
    box(ax, x, 50, 17, 11, 'sujet', label=labs[i], size='s')
    if i < 3:
        arrow(ax, (x + 17.3, 55.5), (x + 20.7, 55.5), 'varie')
box(ax, 3, 14, 38, 16, 'resultat', label='PGCD (ch. 21, 54)\ndernier terme constant', size='s')
box(ax, 46, 14, 39, 16, 'resultat', label=r'$V(-2)-V(2)=3-0=3$' + '\n' + 'trois racines', size='s')
arrow(ax, (66, 49), (24, 31.5), 'fixe')
arrow(ax, (76, 49), (70, 31.5), 'fixe')
save(fig, '69-133')
