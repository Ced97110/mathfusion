import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for i in range(8):
    box(ax, 10 + 8.5 * i, 54, 8.5, 9, 'sujet', label=rf'$b_{7 - i}$', size='s')
brace(ax, 10, 78, 53, 'sujet', label='1 octet : 8 bits')
arrow(ax, (44, 46), (44, 36), 'varie', lw=1.3)
box(ax, 10, 25, 68, 10, 'resultat', label=r'un élément de $\mathbb{F}_{256}$')
text(ax, 44, 17, r'$2^8=256$ éléments', 'resultat', 's')
text(ax, 44, 8, 'Reed-Solomon : QR, disques', 'encre', 's')
save(fig, '67-232')
