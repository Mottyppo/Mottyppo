# Maintaining the profile

This is the profile README for [Mottyppo](https://github.com/Mottyppo).
Keep this repository public, named `Mottyppo`, with a nonempty `README.md` on the default branch.

## Content and artwork

- Edit `README.md` to update the introduction, technologies or links.
- Original geometric monogram banners are in `assets/banner-light.svg` and `assets/banner-dark.svg`.
- Technology icons are stored locally. Keep the visible text labels and image alternative text.
- GitHub selects the banner, LaTeX icon and snake variant using the picture element's color-scheme media queries. The light asset is the fallback.

The banner uses **Space Grotesk** by Florian Karsten, distributed under the SIL Open Font License. Its letters are converted to vector paths so the design renders consistently without external fonts. The source font and license are in `assets/fonts/`; rebuild both variants with `python3 scripts/build_banner.py` after installing `fonttools==4.60.2`. Font source: [google/fonts](https://github.com/google/fonts/tree/00a38a53f92aef923b9353f40128e8f4552ddae4/ofl/spacegrotesk).

## Contribution snake

The workflow runs daily at 04:17 UTC. It also runs when its file changes on `main`, or from **Actions → Contribution snake → Run workflow**.

The two SVG output options match [Tobi Mey’s tutorial workflow](https://github.com/tobimey/tobimey/blob/main/.github/workflows/snake.yml): the default light palette and `palette=github-dark`, without custom color overrides. The calendar and snake route reflect this account’s own contributions.

It reads `Mottyppo`'s contribution calendar using the repository's automatic `GITHUB_TOKEN`, generates two SVGs, validates both and publishes them to `output`. No personal access token, GitHub Pages site or paid service is required. A failed generation or validation does not replace the last successful images.

The job needs `contents: write`; other workflows receive no permissions from this file. If an account policy blocks an action, allow only the required action rather than broadly changing account security settings.

GitHub may disable scheduled workflows in public repositories after 60 days without repository activity. Re-enable the workflow in Actions and run it manually if that happens. Check the Actions page when diagnosing stale images; GitHub's image cache may also delay visible updates.

## Action versions and credits

Verified on 2026-09-28:

- [Platane/snk](https://github.com/Platane/snk), `v3`: `d8f6715049803e982ee5ff501b6b9b7d5deeb09b`.
- [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages), `v4.1.0`: `84c30a85c19949d7eee79c4ff27748b70285e453` (commit behind the annotated tag).
- Technology icons: [Devicon](https://github.com/devicons/devicon), `v2.17.0`, commit `54cfe13ac10eaa1ef817a343ab0a9437eb3c2e08`. MIT license included in `assets/icons/LICENSE.devicon`. `latex-dark.svg` is a recolored version for contrast on dark backgrounds. Technology logos belong to their respective owners.

When updating Actions, review the upstream release and replace the complete commit SHA; do not switch to floating tags.
