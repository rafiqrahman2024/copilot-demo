#!/bin/bash

msg=$(git diff | ollama run phi <<EOF
Generate a clean git commit message:

- Use conventional commits
- Keep it short
- No explanation

EOF
)

git add commit-ai.sh
git commit -m "$msg"
git push