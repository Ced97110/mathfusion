import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def steps(ax, y_top, items, h=11, gap=4, nums=True):
    x0 = 12 if nums else 4
    cx = (x0 + 86) / 2; y = y_top
    for i, (role, l1, l2) in enumerate(items):
        yb = y - h
        box(ax, x0, yb, 86 - x0, h, role, lw=1.6 if role == "varie" else 0.8)
        text(ax, cx, yb + h * 0.7, l1, role, "s"); text(ax, cx, yb + h * 0.27, l2, "encre", "s")
        if nums: disc(ax, 7, yb + h / 2, 3, role, label=str(i + 1), size="s")
        if i < len(items) - 1: arrow(ax, (cx, yb), (cx, yb - gap), "fixe")
        y = yb - gap

fig, ax = canvas(70)
text(ax, 44, 66, r'diviseurs de 30 : $a$ = 2, $b$ = 6 ; $\wedge$ = PGCD, $\vee$ = PPCM', 'encre', 's')
steps(ax, 61, [('sujet', r'$a\leq b$ donne $b=a\vee b$', 'PPCM(2, 6) = 6'),
               ('varie', r'De Morgan sur $b=a\vee b$', r'$b^{\prime}=a^{\prime}\wedge b^{\prime}$ : 5 = PGCD(15, 5)'),
               ('fixe', r'$a\wedge b^{\prime}=(a\wedge a^{\prime})\wedge b^{\prime}$', '2 ∧ 5 = (2 ∧ 15) ∧ 5'),
               ('resultat', r'$a\wedge a^{\prime}=O$, donc $a\wedge b^{\prime}=O$', '1 ∧ 5 = 1')])
save(fig, '80-237')
