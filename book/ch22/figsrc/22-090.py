import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(84)
text(ax, 44, 79, r'$(a+b)(a-b)$', 'sujet', 'l')
items = [(2, r'$a\times a$', 'sujet'), (24, r'$-a\times b$', 'varie'), (46, r'$+b\times a$', 'varie'), (68, r'$-b\times b$', 'sujet')]
for x, l, r in items:
    box(ax, x, 60, 18, 9, r, label=l, size='s')
brace(ax, 24, 64, 58, 'varie', label='s’annulent', depth=1.6)
arrow(ax, (11, 59), (31, 40), 'sujet'); arrow(ax, (77, 59), (57, 40), 'sujet')
box(ax, 14, 31, 60, 9, 'resultat', label=r'$a^{2}-b^{2}$', size='l')
text(ax, 44, 22, r'pour $a=4$ et $b=\sqrt{6}$', 'fixe', 's')
text(ax, 44, 14, r'$16-6=10$', 'resultat', 'l')
text(ax, 44, 5, r'$(\sqrt{6})^{2}=6$ : plus de racine', 'resultat', 's')
save(fig, '22-090')
