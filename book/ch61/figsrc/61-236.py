import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
hd = [r'$u$', r'$1+u$']
cw, ch, x0, y0 = 32, 16, 20, 22
text(ax, 10, 59, r'$\times$', 'encre', 'l')
for i in range(2):
    text(ax, x0 + cw * i + cw / 2, 59, hd[i], 'encre', 'm')
    text(ax, 10, y0 + ch * (1 - i) + ch / 2, hd[i], 'encre', 'm')
cells = [(0, 0, 'sujet', r'$u\times u=u+1$'), (1, 0, 'resultat', r'$u\times(1+u)=1$'),
         (0, 1, 'resultat', r'$(1+u)\times u=1$'), (1, 1, 'autre', r'$(1+u)^2=u$')]
for c, r, role, lab in cells:
    box(ax, x0 + cw * c, y0 + ch * (1 - r), cw, ch, role, label=lab, size='s')
text(ax, 44, 14, 'produits par 0 et par 1 : immédiats', 'fixe', 's')
text(ax, 44, 6, 'les quatre cases : les trois produits', 'fixe', 's')
save(fig, '61-236')
