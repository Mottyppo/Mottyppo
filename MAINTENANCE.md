# Maintaining the profile

This is the profile README for [Mottyppo](https://github.com/Mottyppo).
Keep this repository public, named `Mottyppo`, with a nonempty `README.md` on the default branch.

## Content and artwork

- Edit `README.md` to update the introduction, technologies or links.
- Original editorial banners are in `assets/banner-editorial-light.png` and `assets/banner-editorial-dark.png`. They feature an abstract silver/violet ribbon and custom-styled lettering, generated with OpenAI Imagegen. The PNGs are self-contained; no external font service is required.
- Technology icons are stored locally. Keep the visible text labels and image alternative text.
- GitHub selects the banner, LaTeX icon and snake variant using the picture element's color-scheme media queries. The light asset is the fallback.

## Contribution snake

The workflow runs daily at 04:17 UTC. It also runs when its file changes on `main`, or from **Actions → Contribution snake → Run workflow**.

The workflow uses the main [Platane/snk action](https://github.com/Platane/snk#usage) directly, pinned to the verified `v3` commit. Its two SVG outputs use the official default light palette and `palette=github-dark`, without color overrides. The default snake is purple (`#800080`); validation checks that before publication. The calendar and snake route reflect this account’s own contributions.

It reads `Mottyppo`'s contribution calendar using the repository Secret `SNAKE_TOKEN` when configured, falling back to the automatic `GITHUB_TOKEN` for publicly accessible calendars. A private profile needs an owner credential to read its calendar. Publication always uses `GITHUB_TOKEN`; the personal token is never used to push files.

Before publication, both SVGs must contain a moving snake path as well as valid XML and the purple palette. Empty calendars produce stationary SVGs and are rejected, preserving the last moving animation on `output`. An unavailable calendar, expired token or failed generation therefore leaves the previously published files untouched. Until credentials are configured, the restored animation is a historical snapshot rather than current activity.

### Private profile setup

1. As **Mottyppo**, create a dedicated personal access token (classic) named `Mottyppo contribution snake`, with an expiration date and only the `read:user` scope. This scope is documented for GraphQL contribution collections; no `repo`, `workflow` or write scopes are needed. See [GitHub's contribution API](https://docs.github.com/en/graphql/reference/users#contributionscollection).
2. In this repository, open **Settings → Secrets and variables → Actions → New repository secret**. Name it `SNAKE_TOKEN` and paste the value directly into GitHub. Do not put it in the README, workflow source, chat or logs.
3. Run **Actions → Contribution snake → Run workflow**. Verify both SVGs pass movement validation and the `output` branch is updated. Keep the profile's privacy setting unchanged.
4. Before expiration, replace the Secret with a new token using the same limited scope. If it expires first, the previous animation remains visible and the workflow reports the error.

The generated SVG exposes daily contribution counts visually through the README even when the rest of the profile is private. It contains no private repository names or code.

The job needs `contents: write`; other workflows receive no permissions from this file. If an account policy blocks an action, allow only the required action rather than broadly changing account security settings.

GitHub may disable scheduled workflows in public repositories after 60 days without repository activity. Re-enable the workflow in Actions and run it manually if that happens. Check the Actions page when diagnosing stale images; GitHub's image cache may also delay visible updates.

## Action versions and credits

Verified on 2026-09-28:

- [Platane/snk](https://github.com/Platane/snk), `v3`: `d8f6715049803e982ee5ff501b6b9b7d5deeb09b`.
- [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages), `v4.1.0`: `84c30a85c19949d7eee79c4ff27748b70285e453` (commit behind the annotated tag).
- Technology icons: [Devicon](https://github.com/devicons/devicon), `v2.17.0`, commit `54cfe13ac10eaa1ef817a343ab0a9437eb3c2e08`. MIT license included in `assets/icons/LICENSE.devicon`. `latex-dark.svg` is a recolored version for contrast on dark backgrounds. Technology logos belong to their respective owners.

When updating Actions, review the upstream release and replace the complete commit SHA; do not switch to floating tags.
