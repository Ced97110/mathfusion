import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 38
f = numberline(ax, 6, 76, y, 1760, 1900, 20, role='fixe', arrow_right=False, every=2)
for yr, name, desc, h in [(1770, 'Lagrange 1770', 'permute les racines', 58), (1822, 'Galois 1811–1832', 'groupe : quelles équations', 58), (1872, 'Klein 1872', 'groupe de transformations', 46)]:
    pass
line(ax, [(f(1770), y), (f(1770), 56)], 'sujet')
text(ax, f(1770) + 1, 60, 'Lagrange 1770', 'sujet', 's', ha='left'); text(ax, f(1770) + 1, 56.5, 'permute les racines', 'fixe', 's', ha='left')
line(ax, [(f(1811), y), (f(1832), y)], 'sujet', lw=2.5)
line(ax, [(f(1822), y), (f(1822), 48)], 'sujet')
text(ax, f(1822) - 8, 52, 'Galois 1811–1832', 'sujet', 's', ha='left'); 
line(ax, [(f(1872), y), (f(1872), 44)], 'sujet')
text(ax, f(1872) + 1, 44, 'Klein 1872', 'sujet', 's', ha='left')
text(ax, f(1872) + 1, 40.5, 'transformations', 'fixe', 's', ha='left')
line(ax, [(f(1770), 22), (f(1880), 22)], 'sujet', lw=2.5)
text(ax, f(1825), 17.5, 'les groupes servent déjà', 'sujet', 's')
line(ax, [(f(1880), 22), (f(1900), 22)], 'autre', lw=2.5)
text(ax, f(1890), 11, 'définition par\naxiomes (fin XIXe)', 'autre', 's')
save(fig, '44-277')
