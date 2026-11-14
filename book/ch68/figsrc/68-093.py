import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for x, w, role, cap in [(4, '0000', 'sujet', 'mot du code'), (34, '0001', 'varie', 'mot reçu'), (64, '0011', 'sujet', 'mot du code')]:
    box(ax, x, 24, 20, 9, role, label=w)
    text(ax, x + 10, 38, cap, role, 's')
for x0, x1 in [(24, 34), (54, 64)]:
    arrow(ax, (x0, 28.5), (x1, 28.5), 'varie', both=True)
    text(ax, (x0 + x1) / 2, 20, 'distance 1', 'varie', 's')
brace(ax, 14, 74, 15, 'fixe', label=r'distance 2 = $d$')
text(ax, 44, 3, r'$t=0$ : 0001 est ambigu', 'limite', 'm')
save(fig, '68-093')
