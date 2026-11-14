import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$27q^2+4p^3=108-108=0$', 'encre', 'm')
labs = [r'$x^3-3x+2$', r'$3x^2-3$', r'$18x-18$']
for i in range(3):
    box(ax, 3 + 21 * i, 32, 17, 12, 'sujet', label=labs[i], size='s')
    if i < 2:
        arrow(ax, (20.3 + 21 * i, 38), (23.7 + 21 * i, 38), 'varie')
arrow(ax, (63.3, 38), (66.7, 38), 'varie')
box(ax, 66, 32, 17, 12, 'fixe', label='0', dash=True, fill=False)
text(ax, 74.5, 48, 'terme absent', 'fixe', 's')
arrow(ax, (11.5, 31), (11.5, 22), 'fixe')
text(ax, 11.5, 17, r'$F(1)=0$', 'resultat', 's')
arrow(ax, (53.5, 31), (53.5, 22), 'fixe')
text(ax, 53.5, 17, r'$18x-18=0$ en $x=1$', 'resultat', 's')
text(ax, 44, 6, r'$x=1$ : racine commune', 'resultat', 'm')
save(fig, '69-125')
