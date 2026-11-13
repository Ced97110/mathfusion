import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
labs = ['000', '001', '010', '011', '100', '101', '110', '111']
dx = 10.5; x0 = 44 - dx * 3.5
for i, l in enumerate(labs):
    x = x0 + dx * i
    disc(ax, x, 30, 4.4, 'resultat', label=l, size='s')
    arrow(ax, (x - 2.2, 35.0), (x + 2.2, 35.0), 'varie', lw=0.9, curve=-1.6)
brace(ax, x0 - 4.8, x0 + dx * 7 + 4.8, 23, 'resultat', '8 cycles d’une entrée')
text(ax, 44, 52, 'l’identité ne déplace rien', 'encre', 'm')
text(ax, 44, 8, r'2 sorties par cycle : $2^{8}=256$', 'resultat', 'l')
save(fig, '49-267')
