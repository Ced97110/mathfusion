#!/bin/bash
# Commit and push the interactive figures of the given chapters, one commit per chapter.
# Usage (from the repo root): tools/physique/figcommit.sh <done.json> <chapter> [<chapter> ...]
# done.json: {"interactive": [ids], ...} written by the batch agent. Stops on any rebase conflict.
set -u
DONE="$1"; shift
TRAILER=$'\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'

sync_push() {
  for _ in 1 2 3 4 5 6; do
    git fetch -q origin || { sleep 5; continue; }
    if ! git rebase -q origin/main; then git rebase --abort; echo "CONFLIT au rebase : arrêt"; exit 1; fi
    git push -q origin HEAD:main && return 0
    sleep 4
  done
  echo "ECHEC du push : arrêt"; exit 1
}

for ch in "$@"; do
  key=$(printf '%03d' "$ch")
  ids=$(python3 -c "import json,sys;print(' '.join(i for i in json.load(open('$DONE'))['interactive'] if i.startswith('c$key/')))")
  [ -z "$ids" ] && { echo "chapitre $ch : aucune figure interactive"; continue; }
  # index.json = sorted union of the ids already published and this chapter's ids
  python3 - "$ids" <<'EOF'
import json, sys
p = 'public/physique/fig/index.json'
ids = sorted(set(json.load(open(p))) | set(sys.argv[1].split()))
json.dump(ids, open(p, 'w'), indent=1)
EOF
  git add public/physique/fig/index.json "public/physique/fig/c$key"
  n=$(echo "$ids" | wc -w | tr -d ' ')
  git commit -q -m "Physique, figures interactives, chapitre $ch ($n figures)$TRAILER" || exit 1
  sync_push
  echo "chapitre $ch poussé ($n figures)"
done
