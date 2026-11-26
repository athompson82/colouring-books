# Colouring Books (Cedar & Ink Press)

| Book | Folder | Status |
|---|---|---|
| Football Teddy Bears: Gridiron Grit | `football-teddy-bears-vol1/` | Ready for KDP |
| Hockey Teddy Bears: Breakaway | `hockey-teddy-bears-vol1/` | Ready for KDP |
| Soccer Teddy Bears: Golden Goal | `soccer-teddy-bears-vol1/` | Ready for KDP |
| Baseball Teddy Bears: Grand Slam | `baseball-teddy-bears-vol1/` | Ready for KDP |

Each book's `output/` folder holds the two upload files (`interior_8.5x11.pdf`, `cover_wrap.pdf`) and a small `preview_for_sharing.pdf`.
KDP settings (all four books): paperback · black & white interior · white paper · 8.5 × 11 in · no bleed · 84 pages · author/imprint Cedar & Ink Press · AI-generated images: Yes.

Series plan: `sports-teddy-bears-series-plan.md`. Shared build scripts: `scripts/` (settings per book in `book.json`).
Rebuild a book: `python3 scripts/build_interior.py <book-folder>` and `python3 scripts/build_cover.py <book-folder> <book-folder>/cover/front_art.png`.
