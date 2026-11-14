import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
s, g = 8, 2.5
for i in range(4): box(ax, 32 + i * (s + g), 36, s, s, 'sujet', label='2')
for i in range(3): box(ax, 32 + i * (s + g), 8, s, s, 'sujet', label='2')
box(ax, 32 + 3 * (s + g), 8, s, s, 'varie', fill=False, dash=True, label='2')
text(ax, 15, 40, r'$2^{4}=16$', 'sujet', 'm')
text(ax, 15, 12, r'$2^{3}=8$', 'sujet', 'm')
arrow(ax, (51, 34), (51, 19), 'varie')
text(ax, 48.5, 27, 'exposant − 1', 'varie', 's', ha='right')
text(ax, 54, 27, '÷ 2', 'varie', 'l', ha='left')
text(ax, 67, 3.5, 'facteur retiré', 'varie', 's')
save(fig, '14-010')
