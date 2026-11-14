"""Check a rewritten chapter against book/reecriture/consigne.md. Zero tokens.

Usage (from the repo root): python3 tools/reecriture/check.py 41
Reads book/reecriture/chNN/{chNN.html, calculs.json, termes.json}. Prints a report and a score (0-1);
exit code 1 if a blocking check fails.
"""
from __future__ import annotations

import json
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TAGS = {'div', 'h1', 'h2', 'h3', 'p', 'b', 'i', 'img', 'details', 'summary', 'span', 'sub', 'sup', 'br'}
CLASSES = {'pk', 'li', 'eq', 'vf', 'cap', 'rappel', 'avous', 'plus', 'retenir', 'rt', 'm'}
BANNED = ['évidemment', 'clairement', 'il suffit', 'on voit facilement', 'trivial', 'bien sûr']
MAX_WORDS = 15  # target sentence length (consigne, rule 1)


class Scan(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.bad: list[str] = []
        self.imgs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag not in TAGS:
            self.bad.append(f'balise <{tag}>')
        for c in (a.get('class') or '').split():
            if c not in CLASSES:
                self.bad.append(f'classe "{c}"')
        if tag == 'img':
            self.imgs.append(a.get('src') or '')


def plain(html: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html)).strip()


def blocks(html: str) -> list[str]:
    """Text of each block (p, h1-h3, summary): sentences never run across two blocks."""
    return [plain(b) for b in re.findall(r'<(?:p|h[123]|summary)\b[^>]*>(.*?)</(?:p|h[123]|summary)>', html, re.S)]


def check_calcs(path: Path) -> tuple[int, list[str]]:
    env = {k: getattr(math, k) for k in ('sqrt', 'cos', 'sin', 'tan', 'atan', 'atan2', 'acos', 'asin', 'radians', 'degrees', 'pi')}
    errors = []
    calcs = json.loads(path.read_text(encoding='utf8'))
    for c in calcs:
        try:
            got = eval(c['expr'], {'__builtins__': {}}, env)  # expressions written by the rewriting agent, local file
        except Exception as exc:  # noqa: BLE001 - report any bad expression
            errors.append(f"{c.get('ou')}: expression invalide {c['expr']!r} ({exc})")
            continue
        if abs(got - float(c['affiche'])) > float(c.get('tol', 0.01)):
            errors.append(f"{c.get('ou')}: {c['expr']} = {got:.4f}, le texte affiche {c['affiche']}")
    return len(calcs), errors


def first_use(text: str, term: str) -> int:
    m = re.search(r'\b' + re.escape(term.lower()) + r's?\b', text.lower())
    return m.start() if m else -1


def main() -> None:
    n = sys.argv[1].zfill(2)
    d = ROOT / 'book' / 'reecriture' / f'ch{n}'
    html = (d / f'ch{n}.html').read_text(encoding='utf8')
    blocking: list[str] = []
    warn: list[str] = []

    scan = Scan()
    scan.feed(html)
    blocking += [f'non autorisé : {b}' for b in sorted(set(scan.bad))]
    figs = [f['src'] for f in json.loads((d / 'figures.json').read_text(encoding='utf8'))]
    figs += [f'/chapters/img/ch{n}/{f.name}' for f in sorted((d / 'fig').glob('*.svg'))]  # figures added by the rewrite
    missing = [f for f in figs if f not in scan.imgs]
    blocking += [f'figure absente : {f}' for f in missing]
    blocking += [f'image inconnue : {s}' for s in scan.imgs if s not in figs]

    n_calc, calc_err = check_calcs(d / 'calculs.json')
    blocking += calc_err

    # A term must not appear before the paragraph that defines it (its first <b>).
    terms = json.loads((d / 'termes.json').read_text(encoding='utf8'))
    text = plain(re.sub(r'<details>.*?</details>', ' ', html, flags=re.S))
    bold = plain(html)
    for t in terms:
        term = t['terme']
        m = re.search(r'<b>\s*' + re.escape(term), html, re.I)
        body = html[html.find('</h1>') + 5:] if '</h1>' in html else html  # the title may name the subject
        if not m:
            warn.append(f'terme jamais mis en gras : {term}')
            continue
        defined_at = len(plain(body[:body.find(m.group(0))]))
        bold = plain(body)
        used_at = first_use(bold, term)
        if 0 <= used_at < defined_at - 1:
            warn.append(f'« {term} » employé avant sa définition : …{bold[max(0, used_at - 40):used_at + 30]}…')

    prose = re.sub(r'<p class="eq">.*?</p>', ' ', re.sub(r'<details>.*?</details>', ' ', html, flags=re.S))
    sentences = [s for b in blocks(prose) for s in re.split(r'(?<=[.?!])\s+', b) if len(s.split()) > 2]
    lengths = [len(s.split()) for s in sentences]
    long = [s for s in sentences if len(s.split()) > MAX_WORDS + 7]
    for b in BANNED:
        if b in text.lower():
            warn.append(f'mot à éviter : « {b} »')
    counts = {c: html.count(f'class="{c}"') for c in ('rappel', 'avous', 'plus', 'retenir')}
    if not counts['retenir']:
        warn.append('pas d’encadré « À retenir »')

    short_share = sum(x <= MAX_WORDS for x in lengths) / max(1, len(lengths))
    score = (1.0 if not blocking else 0.0) * (0.5 + 0.5 * short_share) * (0.97 ** len(warn))
    print(f'chapitre {n} : {len(text.split())} mots, {len(sentences)} phrases, '
          f'{sum(lengths) / max(1, len(lengths)):.1f} mots/phrase, {short_share:.0%} ≤ {MAX_WORDS} mots')
    print(f'encadrés : {counts} ; termes définis : {len(terms)} ; calculs vérifiés : {n_calc - len(calc_err)}/{n_calc}')
    for b in blocking:
        print('BLOQUANT', b)
    for w in warn:
        print('attention', w)
    for s in long[:8]:
        print(f'phrase longue ({len(s.split())} mots) : {s[:110]}')
    print(f'score {score:.2f}')
    sys.exit(1 if blocking else 0)


if __name__ == '__main__':
    main()
