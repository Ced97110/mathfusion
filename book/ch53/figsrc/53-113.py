import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
assert int('11011', 2) == 27
text(ax, 4, 57, 'base 10 : ×10 par case', 'autre', 's', ha='left')
for i, d in enumerate('27'):
    box(ax, 4 + i * 16, 40, 14, 12, 'autre', label=d, size='l')
text(ax, 4, 30, 'base 2 : ×2 par case', 'sujet', 's', ha='left')
for i, (w, d) in enumerate(zip((16, 8, 4, 2, 1), '11011')):
    box(ax, 4 + i * 16, 10, 14, 12, 'sujet', label=d, size='l')
    text(ax, 11 + i * 16, 5, str(w), 'sujet', 's')
save(fig, '53-113')
