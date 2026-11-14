import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(74)
text(ax, 44, 70, r'$(1-\sin x)(1+\sin x)$', 'encre', 'm')
text(ax, 26, 62, r'$1$', 'sujet', 's'); text(ax, 52, 62, r'$+\sin x$', 'autre', 's')
text(ax, 8, 52, r'$1$', 'sujet', 's'); text(ax, 8, 37, r'$-\sin x$', 'autre', 's', ha='left')
box(ax, 16, 46, 20, 12, 'fixe', r'$1$', 'm'); box(ax, 40, 46, 24, 12, 'varie', r'$+\sin x$', 'm')
box(ax, 16, 30, 20, 12, 'varie', r'$-\sin x$', 'm'); box(ax, 40, 30, 24, 12, 'fixe', r'$-\sin^2 x$', 'm')
text(ax, 76, 44, "s'annulent", 'varie', 's', ha='center', rot=0) if False else None
line(ax, [(65, 52), (70, 52), (70, 36), (65, 36)], 'varie'); text(ax, 78, 44, "s'annulent", 'varie', 's')
box(ax, 8, 12, 72, 12, 'resultat', r'$= 1-\sin^2 x = \cos^2 x$', 'm')
text(ax, 44, 4, r'$30^\circ$ : $0{,}5 \times 1{,}5 = 0{,}75$', 'fixe', 's')
save(fig, '31-126')
