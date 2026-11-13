import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
S = {'1': 74, '2': 62, '3': 50}; T = {'a': 68, 'b': 56}; U = {'z': 74, 'y': 62, 'x': 50}
for k, y in S.items(): disc(ax, 14, y, 3.5, 'sujet', label=k)
for k, y in T.items(): disc(ax, 44, y, 3.5, 'autre', label=k)
for k, y in U.items(): disc(ax, 74, y, 3.5, 'limite' if k == 'y' else 'resultat', label=k)
for s, t in (('1', 'a'), ('2', 'a'), ('3', 'b')): arrow(ax, (17.7, S[s]), (40.3, T[t]), 'sujet')
for t, u in (('a', 'z'), ('b', 'x')): arrow(ax, (47.7, T[t]), (70.3, U[u]), 'autre')
text(ax, 44, 83, r'1. application : $f$ puis $g$', 'encre', 'm', weight='bold')
rows = [('limite', r'2. injective ? $f$ non, $g$ oui'), ('limite', r'3. surjective ? $f$ oui, $g$ non'),
        ('resultat', r'4. $g \circ f$ : 1, 2 $\mapsto$ z ; 3 $\mapsto$ x'), ('resultat', r'5. $(g \circ f)^{-1}(z) = \{1, 2\}$')]
for k, (role, lab) in enumerate(rows):
    box(ax, 2, 34 - 10 * k, 84, 8, role, label=lab, size='s')
save(fig, '42-272')
