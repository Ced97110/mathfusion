"""Commit one chapter through a private Git index.

Several sessions share this working tree and its .git/index. A plain
`git add` + `git commit` can pick up files another session staged in between.
This script builds the commit in a temporary index: HEAD, plus this chapter's
lines of book/JOURNAL.md and content/toc.json, plus book/chNN and
public/chapters/chNN.html. It refuses to commit any other path.

Usage (from the repo root, after the journal line and tools/site.py):
    python3 tools/commit_chapter.py N "Titre du chapitre" NB_FICHES [chemin_exclu ...]
Then: git push origin main.
"""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

Run = subprocess.CompletedProcess


def git(*args: str, inp: str | None = None, env: dict[str, str] | None = None) -> str:
    res: Run = subprocess.run(
        ["git", *args], input=inp, capture_output=True, text=True, check=True, env=env or os.environ
    )
    return res.stdout.strip()


def own_journal_lines(n: int, work: list[str]) -> tuple[str, str]:
    row = re.compile(rf"^\| [0-9-]+ \| {n} ")
    rows = [line for line in work if row.match(line)]
    notes = [line for line in work if line.startswith(f"- Chapitre {n} :")]
    if len(rows) != 1 or len(notes) != 1:
        sys.exit(f"journal : attendu 1 ligne de tableau et 1 remarque pour le chapitre {n}")
    return rows[0], notes[0]


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    n, title, nf = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    exclude = sys.argv[4:]
    nn = f"{n:02d}"
    base = git("rev-parse", "HEAD")

    journal = git("show", f"{base}:book/JOURNAL.md").split("\n")
    row, note = own_journal_lines(n, Path("book/JOURNAL.md").read_text(encoding="utf-8").split("\n"))
    if any(re.match(rf"^\| [0-9-]+ \| {n} ", line) for line in journal):
        sys.exit(f"le chapitre {n} est déjà dans le journal de HEAD")
    last = max(k for k, line in enumerate(journal) if re.match(r"^\| \d{4}-", line))
    journal.insert(last + 1, row)
    journal.append(note)

    toc = json.loads(git("show", f"{base}:content/toc.json"))
    work_toc = {e["key"]: e for e in json.load(open("content/toc.json", encoding="utf-8"))}
    if "file" not in work_toc.get(str(n), {}):
        sys.exit("content/toc.json ne publie pas ce chapitre : lancer tools/site.py")
    toc = [work_toc[str(n)] if e["key"] == str(n) else e for e in toc]

    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, GIT_INDEX_FILE=os.path.join(tmp, "index"))
        git("read-tree", base, env=env)
        blobs: dict[str, str] = {}
        for path, text in [
            ("book/JOURNAL.md", "\n".join(journal)),
            ("content/toc.json", json.dumps(toc, ensure_ascii=False)),
        ]:
            blobs[path] = git("hash-object", "-w", "--stdin", inp=text)
            git("update-index", "--cacheinfo", f"100644,{blobs[path]},{path}", env=env)
        git("add", f"book/ch{nn}", f"public/chapters/ch{nn}.html", env=env)
        for path in exclude:
            git("rm", "--cached", "-q", "--ignore-unmatch", path, env=env)
        tree = git("write-tree", env=env)

    allowed = {"book/JOURNAL.md", "content/toc.json", f"public/chapters/ch{nn}.html"}
    names = git("diff-tree", "-r", "--name-only", base, tree).split("\n")
    stray = [p for p in names if p not in allowed and not p.startswith(f"book/ch{nn}/")]
    if stray:
        sys.exit(f"fichiers hors du chapitre : {stray}")

    msg = f"Chapitre {n} : {title} ({nf} fiches)"
    commit = git("commit-tree", tree, "-p", base, inp=msg)
    git("update-ref", "refs/heads/main", commit, base)
    # Keep the shared index in step with the new HEAD for the files we touched.
    for path, blob in blobs.items():
        git("update-index", "--cacheinfo", f"100644,{blob},{path}")
    git("reset", "-q", "--", f"book/ch{nn}", f"public/chapters/ch{nn}.html")
    print(commit[:8], len(names), "fichiers")


if __name__ == "__main__":
    main()
