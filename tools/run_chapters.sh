#!/usr/bin/env bash
# Enchaîne des chapitres : une session Claude Code neuve par chapitre.
# Usage (depuis la racine du dépôt) : tools/run_chapters.sh 3     -> fait les 3 prochains chapitres
# Chaque session lit CLAUDE.md, fait un chapitre, vérifie que le site se construit, puis pousse.
# La boucle s'arrête dès qu'un chapitre n'est pas terminé (le sommaire n'a pas avancé).
set -euo pipefail
cd "$(dirname "$0")/.."
N="${1:-1}"
for i in $(seq 1 "$N"); do
  CH="$(python3 tools/next_chapter.py)"
  if [ -z "$CH" ]; then echo "Tous les chapitres sont faits."; exit 0; fi
  echo "=== Chapitre $CH ($i sur $N) ==="
  claude -p "Fais le chapitre $CH du livre en suivant exactement la procédure de CLAUDE.md, du début à la fin, sans poser de question. Termine par le bilan demandé." \
    --permission-mode acceptEdits \
    --allowedTools "Read,Write,Edit,Bash,Agent,Task"
  AFTER="$(python3 tools/next_chapter.py)"
  if [ "$AFTER" = "$CH" ]; then echo "Le chapitre $CH n'a pas été terminé : arrêt de la boucle."; exit 1; fi
done
