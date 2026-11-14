import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# r = a + b√-5, s = c + d√-5 with a=1, b=1, c=2, d=1
a_, b_, c_, d_ = 1, 1, 2, 1
assert (a_ * c_ - 5 * b_ * d_) ** 2 == 9 and 5 * (a_ * d_ + b_ * c_) ** 2 == 45
assert (a_ * c_) ** 2 == 4 and -10 * a_ * b_ * c_ * d_ == -20 and 25 * (b_ * d_) ** 2 == 25
assert 5 * (a_ * d_) ** 2 == 5 and 10 * a_ * b_ * c_ * d_ == 20 and 5 * (b_ * c_) ** 2 == 20
text(ax, 44, 75, r'$r=1+\sqrt{-5}$     $s=2+\sqrt{-5}$', 'sujet', 'm')
text(ax, 44, 67, r'$rs=-3+3\sqrt{-5}$', 'sujet', 'm')
box(ax, 3, 36, 38, 24, 'sujet')
box(ax, 47, 36, 38, 24, 'autre')
text(ax, 22, 55, r'$(ac-5bd)^2=9$', 'sujet', 's')
text(ax, 66, 55, r'$5(ad+bc)^2=45$', 'autre', 's')
text(ax, 10, 43, '$4$\n$a^2c^2$', 'sujet', 's')
box(ax, 15, 37.5, 14, 11, 'varie', label='$-20$\n$-10abcd$', size='s')
text(ax, 34, 43, '$+25$\n$25b^2d^2$', 'sujet', 's')
text(ax, 54, 43, '$5$\n$5a^2d^2$', 'autre', 's')
box(ax, 59, 37.5, 14, 11, 'varie', label='$+20$\n$+10abcd$', size='s')
text(ax, 78, 43, '$+20$\n$5b^2c^2$', 'autre', 's')
arrow(ax, (22, 34), (66, 34), 'varie', curve=0.35, both=True)
text(ax, 44, 22, r'$-20+20=0$ : ils s’annulent', 'varie', 's')
text(ax, 44, 14, r'$N(rs)=9+45=54$', 'resultat', 'm')
text(ax, 44, 6, r'$N(r)N(s)=6\times9=54$', 'resultat', 'm')
save(fig, '56-180')
