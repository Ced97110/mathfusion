import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$q=|G|/|P|=6/2=3$', 'encre', 'm')
text(ax, 64, 51, r'$q$ en $n_p$ groupes égaux', 'fixe', 's')
cell = lambda i: 48 + 10 * i
def cells(y):
    for i in range(3):
        box(ax, cell(i), y, 7, 7, 'sujet', r=0.5)
def out(i0, i1, y, role):
    box(ax, cell(i0) - 1.5, y - 1.5, cell(i1) + 7 - cell(i0) + 3, 10, role, fill=False, lw=1.0)
y = 36; cells(y); out(0, 2, y, 'resultat'); text(ax, 4, y + 3.5, r'$n_p=1$ : divise 3', 'resultat', 'm', ha='left')
y = 20; cells(y); out(0, 1, y, 'limite'); out(2, 2, y, 'limite'); text(ax, 4, y + 3.5, r'$n_p=2$ : ne divise pas 3', 'limite', 'm', ha='left')
y = 4; cells(y)
for i in range(3): out(i, i, y, 'resultat')
text(ax, 4, y + 3.5, r'$n_p=3$ : divise 3', 'resultat', 'm', ha='left')
save(fig, '50-045')
