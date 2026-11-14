import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 6, 76, 30, 0, 10, labels=False, arrow_right=True)
for v in range(11):
    inorb = v % 3 == 1
    sub = v % 3 == 0 and v <= 9
    if inorb or sub:
        disc(ax, f(v), 30, 3.1, 'sujet' if inorb else 'fixe', label=str(v), size='s')
    else:
        text(ax, f(v), 24.5, str(v), 'fixe', 's')
for a, b in [(1, 4), (4, 7), (7, 10)]:
    arrow(ax, (f(a) + 2.5, 36), (f(b) - 2.5, 36), 'varie', curve=-0.5)
text(ax, f(5.5), 48, r'$+3$ : l’action du sous-groupe', 'varie', 's')
box(ax, 4, 4, 38, 8, 'fixe', label=r'sous-groupe : 0, 3, 6, 9', size='s')
box(ax, 45, 4, 40, 8, 'sujet', label='classe de 1 = orbite de 1', size='s')
save(fig, '49-298')
