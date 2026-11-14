import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r'$\overline{D}=\mathbb{Z}/(2)$ : deux classes', 'encre', 'm')
for i, v in enumerate((0, 2, 4)):
    disc(ax, 14 + i * 12, 50, 4.2, 'sujet', label=str(v))
for i, v in enumerate((1, 3, 5)):
    disc(ax, 54 + i * 12, 50, 4.2, 'autre', label=str(v))
arrow(ax, (26, 44), (26, 33), 'sujet')
arrow(ax, (66, 44), (66, 33), 'autre')
box(ax, 10, 22, 32, 10, 'sujet', label='0 : les pairs')
box(ax, 50, 22, 32, 10, 'autre', label='1 : les impairs')
text(ax, 44, 10, r'$1+1=0$ dans cet anneau', 'resultat', 'm')
save(fig, '56-148')
