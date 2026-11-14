import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = [8, 36, 64]
top = [r'$4x^2$', r'$6x$', r'$10$']
bot = [r'$2x^2$', r'$3x$', r'$5$']
text(ax, 44, 64, r'$4x^2+6x+10$', 'fixe', 'm')
for x, a, b in zip(xs, top, bot):
    box(ax, x, 46, 16, 9, 'fixe', label=a)
    arrow(ax, (x + 8, 45), (x + 8, 31), 'varie')
    box(ax, x, 22, 16, 9, 'resultat', label=b)
text(ax, 44, 38, r'$\div 2$', 'varie', 'm', ha='center') if False else None
text(ax, 84, 38, r'$\div 2$', 'varie', 'm', ha='right')
text(ax, 44, 14, 'contenu $2$ ; partie primitive', 'sujet', 's')
text(ax, 44, 8, r'$2x^2+3x+5$ : contenu $1$', 'resultat', 's')
save(fig, '56-145')
