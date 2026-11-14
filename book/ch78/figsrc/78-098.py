import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 28, 56, r'$x$', 'sujet', 'l'); text(ax, 69, 56, r'$\bar{x}$', 'sujet', 'l')
rows = [('ℝ', '(1)', '(1)', False), ('ℂ', '(1, 2)', '(1, −2)', True), ('ℍ', '(1, 2, 3, 4)', '(1, 2, 3, 4)'.replace('2, 3, 4', '−2, −3, −4'), True)]
for k, (n, a, b, ch) in enumerate(rows):
    y = 38 - k * 17
    text(ax, 6, y + 4, n, 'sujet', 'l')
    box(ax, 14, y, 28, 8, 'sujet', label=a)
    arrow(ax, (44, y + 4), (52, y + 4), 'varie' if ch else 'fixe')
    box(ax, 54, y, 31, 8, 'varie' if ch else 'fixe', label=b)
save(fig, '78-098')
