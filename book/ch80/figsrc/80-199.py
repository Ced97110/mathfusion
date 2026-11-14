import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
codes = ['000','001','010','011','100','101','110','111']
out = [0, 1, 0, 1, 1, 0, 0, 1]
x0, cw = 4, 10.5
for i, c in enumerate(codes):
    box(ax, x0 + i * cw, 42, 9.5, 7, 'sujet', label=c, size='s')
    disc(ax, x0 + i * cw + 4.75, 32, 3, 'resultat' if out[i] else 'fixe', fill=bool(out[i]))
text(ax, 44, 55, '8 positions (3 interrupteurs)', 'sujet', 'm')
text(ax, 44, 22, 'pleine : 1 (allumée), vide : 0', 'fixe', 's')
text(ax, 44, 12, r'8 choix de 2 : $2^{8}=256$', 'resultat', 'l')
text(ax, 44, 3.5, '256 fonctions booléennes', 'resultat', 'm')
save(fig, '80-199')
