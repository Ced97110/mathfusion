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

fig, ax = canvas(88)
text(ax, 44, 84, r'diviseurs de 30 : $a$ = 2, $b$ = 6 ; $\wedge$ = PGCD, $\vee$ = PPCM', 'encre', 's')
steps(ax, 80, [('sujet', r'départ : $a^{\prime}\vee b=I$', 'PPCM(15, 6) = 30'),
               ('fixe', r'$a=a\wedge I=a\wedge(a^{\prime}\vee b)$', '2 = 2 ∧ 30'),
               ('varie', r'distributivité : $(a\wedge a^{\prime})\vee(a\wedge b)$', '(2 ∧ 15) ∨ (2 ∧ 6) = 1 ∨ 2'),
               ('fixe', r'$a\wedge a^{\prime}=O$ : il reste $a\wedge b$', '1 ∨ 2 = 2 = 2 ∧ 6'),
               ('resultat', r'$a=a\wedge b$, donc $a\leq b$', '2 divise 6')], nums=False)
save(fig, '80-238')
