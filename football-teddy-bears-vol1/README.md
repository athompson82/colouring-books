# Football Teddy Bears – Vol. 1

8.5 × 11 in colouring book for teens and adults, 40 single-sided pages, Style C (hybrid teddy bear / sports mascot).

- `plan/`: concept, 40-page plan, prompts, Amazon listing draft
- `style-test/`: the 3-style × 3-scene test, contact sheet and generation log
- `reference/`: character references (intense scowl, friendly grin)
- `pages/`: final pages `p01`–`p40` (1792×2400 PNG), Runway task IDs (`tasks.tsv` round 1, `tasks_v2.tsv` friendly round), `expression-map.md`, review contact sheets
- `scripts/`: one-off helper scripts (contact sheets)

Model: Runway Nano Banana 2.1, 2K, 3:4, at 6 credits per image.
- `output/interior_8.5x11.pdf`: **KDP interior**, 84 pages, 8.5 × 11 in, no bleed, B&W. Rebuild with `python3 scripts/build_interior.py .` (from this folder)
- `output/cover_wrap.pdf`: **KDP wrap cover**, 17.439 × 11.25 in (0.125 in bleed, 0.189 in spine for 84 pages, white paper). Imprint: Cedar & Ink Press. Rebuild with `python3 scripts/build_cover.py . cover/front_art.png`
- `cover/`: front art (4K), flattened wrap, preview with trim/spine/barcode guides (cyan = trim/spine, magenta = KDP barcode zone)
- `output/preview_for_sharing.pdf`: small low-res preview (cover + all 40 pages) for emailing. Not for upload.

## KDP upload settings
Paperback · Ink: black & white · Paper: white · Trim: 8.5 × 11 in · Bleed: **No bleed** (interior) · Cover finish: matte or glossy · Upload `output/interior_8.5x11.pdf` and `output/cover_wrap.pdf` · AI-generated content: **Yes** (images) · Author / imprint: Cedar & Ink Press
