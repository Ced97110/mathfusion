import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
y = 34
box(ax, 2, y - 5, 21, 10, 'sujet', label='position 7')
arrow(ax, (24.5, y), (32.5, y), 'varie', both=True)
text(ax, 28.5, y + 5, 'devient', 'varie', 's')
box(ax, 34, y - 5, 16, 10, 'sujet', label=r'$\alpha^7$')
arrow(ax, (51.5, y), (60, y), 'varie', both=True)
text(ax, 55.7, y + 5, 'table', 'varie', 's')
bits = ['1', '1', '0', '1']
subs = [r'$1$', r'$\alpha$', r'$\alpha^2$', r'$\alpha^3$']
for i in range(4):
    box(ax, 62 + 5.5 * i, y - 5, 5.5, 10, 'resultat', label=bits[i], r=0.5)
    text(ax, 64.75 + 5.5 * i, y - 9, subs[i], 'fixe', 's')
text(ax, 44, 15, r'retrouver $i$ : chercher ces bits', 'resultat', 's')
save(fig, '67-226')
