import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
items = ('ch. 12 : $a(b+c)=ab+ac$', 'ch. 13 : moins par moins', 'ch. 15 : polynômes', 'ch. 44 : groupe, monoïde')
for i, lab in enumerate(items):
    y = 60 - i * 17
    box(ax, 2, y, 50, 13, 'varie', label=lab, size='s')
    arrow(ax, (52, y + 6.5), (60, 38), 'varie', lw=0.7)
box(ax, 60, 22, 26, 32, 'sujet')
text(ax, 73, 42, 'anneau', 'sujet', 'l')
text(ax, 73, 32, '8 règles', 'sujet', 's')
save(fig, '51-285')
