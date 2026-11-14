import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$[\mathbb{Q}(\sqrt{2}):\mathbb{Q}]=2$', 'sujet', 'm')
for i, l in enumerate(['1', r'$\sqrt{2}$']):
    box(ax, 28 + 17 * i, 50, 15, 11, 'sujet', label=l)
brace(ax, 28, 60, 50, 'sujet', label='2 nombres')
text(ax, 44, 36, r'$[\mathbb{Q}(\sqrt{2},\sqrt{3}):\mathbb{Q}]=4$', 'autre', 'm')
for i, l in enumerate(['1', r'$\sqrt{2}$', r'$\sqrt{3}$', r'$\sqrt{6}$']):
    box(ax, 9.5 + 18 * i, 20, 15, 11, 'autre', label=l)
brace(ax, 9.5, 78.5, 20, 'autre', label='4 nombres')
text(ax, 44, 5, 'fractions × base, puis +', 'fixe', 's')
save(fig, '63-036')
