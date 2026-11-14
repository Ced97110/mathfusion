import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 20, 56, 48, 10, 'sujet', label=r'$\alpha^4+\alpha+1=0$')
arrow(ax, (44, 56), (44, 49.8), 'varie')
text(ax, 47, 52.9, r'car $-1=1$', 'varie', 's', ha='left')
box(ax, 20, 40, 48, 10, 'sujet', label=r'$\alpha^4=\alpha+1$')
text(ax, 44, 35, r'$\alpha^4$ en quatre bits', 'sujet')
heads = [r'$1$', r'$\alpha$', r'$\alpha^2$', r'$\alpha^3$']
bits = [1, 1, 0, 0]
for c in range(4):
    x = 16 + c * 15
    text(ax, x + 7, 29, heads[c], 'fixe')
    box(ax, x, 17, 14, 9, 'sujet' if bits[c] else 'fixe', label=str(bits[c]))
text(ax, 44, 7, r'$2\times2\times2\times2=16$ mots', 'resultat')
save(fig, '67-169')
