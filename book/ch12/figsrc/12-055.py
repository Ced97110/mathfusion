import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 68, 30, 0, 4, labels=False)
for v, lab, ly in [(0.5, '1/2', 44), (0.75, '0,75', 52), (3.14159, 'π', 44)]:
    disc(ax, f(v), 30, 1.2, 'sujet')
    line(ax, [(f(v), 31.5), (f(v), ly - 2.2)], 'sujet', lw=0.6)
    text(ax, f(v), ly, lab, 'sujet', 'm')
text(ax, f(0), 35, r'$O$', 'varie', 'm')
text(ax, f(0), 26.4, '0', 'fixe', 's'); text(ax, f(1), 26.4, '1', 'fixe', 's')
arrow(ax, (f(0), 22), (f(1), 22), 'varie', both=True)
disc(ax, f(0.5), 17.5, 1.8, 'varie', label='3', size='s')
disc(ax, f(0), 17.5, 1.8, 'varie', label='2', size='s'); disc(ax, 43, 24, 1.8, 'varie', label='1', size='s')
for cx, s in [(15, '1 tracer une ligne'), (44, '2 choisir l\'origine'), (73, '3 choisir l\'unité')]:
    text(ax, cx, 6, s, 'varie', 's')
save(fig, '12-055')
