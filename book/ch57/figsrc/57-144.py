import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 14, 58, 60, 10, 'sujet', label=r'$M/N$ : les classes de $\mathbb{Z}^2$ modulo $N$', size='s')
text(ax, 2, 50, 'on additionne les classes', 'encre', 's', ha='left')
y = 33
box(ax, 3, y, 24, 11, 'autre', label=r'$\overline{(1\,;\,0)}$')
text(ax, 31, y + 5.5, '+', 'encre', 'm')
box(ax, 35, y, 24, 11, 'autre', label=r'$\overline{(0\,;\,1)}$')
text(ax, 63, y + 5.5, '=', 'encre', 'm')
box(ax, 67, y, 19, 11, 'resultat', label=r'$\overline{(1\,;\,1)}$')
text(ax, 2, 25, 'les entiers agissent sur les classes', 'encre', 's', ha='left')
y = 8
text(ax, 8, y + 5.5, r'$3\times$', 'varie', 'm')
box(ax, 16, y, 24, 11, 'autre', label=r'$\overline{(1\,;\,0)}$')
text(ax, 46, y + 5.5, '=', 'encre', 'm')
box(ax, 52, y, 24, 11, 'resultat', label=r'$\overline{(3\,;\,0)}$')
save(fig, '57-144')
