import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

word = 'ALGEBRE'
nums = [ord(c) - 65 for c in word]
imgs = [(5 * n + 3) % 26 for n in nums]
cipher = ''.join(chr(65 + r) for r in imgs)
assert nums == [0, 11, 6, 4, 1, 17, 4] and imgs == [3, 6, 7, 23, 8, 10, 23] and cipher == 'DGHXIKX'

fig, ax = canvas(58)
w, pitch, x0 = 11.0, 11.8, 2.7
ytop, ymid, ybot = 42, 26, 6
for i, (c, n, r, d) in enumerate(zip(word, nums, imgs, cipher)):
    x = x0 + i * pitch
    rep = c == 'E'
    box(ax, x, ytop, w, 12, 'autre' if rep else 'sujet', label=f'{c}\n{n}', size='s')
    box(ax, x, ybot, w, 12, 'autre' if rep else 'resultat', label=f'{d}\n{r}', size='s')
    arrow(ax, (x + w / 2, ytop), (x + w / 2, ymid + 8), 'fixe', lw=0.8)
    arrow(ax, (x + w / 2, ymid), (x + w / 2, ybot + 12), 'fixe', lw=0.8)
box(ax, x0, ymid, 7 * pitch - 0.8, 8, 'varie', label=r'$\times\,5$, puis $+\,3$, puis reste par 26', size='s')
save(fig, '53-049')
