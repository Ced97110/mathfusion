import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u, x0 = 0.48, 8
rows = [(150, 'a + b + c = 150 = 2s', 'sujet'), (70, 'b + c − a = 70 = 2(s − a)', 'autre'),
        (50, 'a − b + c = 50 = 2(s − b)', 'autre'), (30, 'a + b − c = 30 = 2(s − c)', 'autre')]
fig, ax = canvas(64)
for i, (v, title, role) in enumerate(rows):
    y = 49 - 14*i
    h = v / 2
    box(ax, x0, y, h*u, 7, role, label=f'{h:g}', r=0.5)
    box(ax, x0 + h*u, y, h*u, 7, role, label=f'{h:g}', r=0.5)
    text(ax, x0, y + 10.5, title, role, 'm', ha='left')
save(fig, '37-086')
