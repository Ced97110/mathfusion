import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cases = [(3, 'sujet', [r'$\sqrt{3}(7+\sqrt{6})$', r'$7\sqrt{3}+\sqrt{18}$', r'$7\sqrt{3}+3\sqrt{2}$'], r'$\sqrt{18}=3\sqrt{2}$'),
         (47, 'autre', [r'$\sqrt{2}(5+\sqrt{6})$', r'$5\sqrt{2}+\sqrt{12}$', r'$5\sqrt{2}+2\sqrt{3}$'], r'$\sqrt{12}=2\sqrt{3}$')]
w, h, gap = 38, 9, 9
for x, role, exprs, simp in cases:
    cx = x + w / 2
    for i, e in enumerate(exprs):
        y = 52 - i * (h + gap)
        box(ax, x, y, w, h, role, label=e, size='s')
        if i < 2:
            arrow(ax, (cx, y), (cx, y - gap), 'varie')
            text(ax, cx + 3, y - gap / 2, 'on distribue' if i == 0 else simp, 'varie', 's', ha='left')
save(fig, '22-155')
