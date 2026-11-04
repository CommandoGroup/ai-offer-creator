# Operations

Railway service: `offer-generator-ai`. Production URL: https://web-production-5bf5a.up.railway.app/

The GitHub repository's `main` branch is connected to automatic production deployment. A push to `main` is the live trigger. Tags and review branches do not establish that production is running their source.

## Local preparation

Install `requirements.txt` in an isolated Python environment. Set any required key through the environment without printing it. Run `python app.py` and use the local address printed by Flask.

Set `OPENAI_API_KEY` in Railway. `PORT` is supplied by Railway. The Procfile starts 2 Gunicorn workers with a 120-second timeout.

## Release

1. Prepare the reviewed commit on a branch. Fetch `origin` and verify that the candidate includes the current `origin/main`. Run the focused validation before publishing it.
2. Test the candidate in a nonproduction running environment at both supported widths. Record the source commit and results before the live step.
3. The owner advances `main` to the exact validated candidate with an ordinary fast-forward push. This starts Railway production deployment. Do not rewrite history.
4. Read Railway's deployment status and deployed source commit. Require a successful deployment of that exact candidate.
5. Open the tool inside My Resources on the live member site at 1280 and 390 pixels. Generate 2 offers using keys returned by `/api/strategies` (for example `cash`). Download branded and pro PDFs and confirm both open. Reset the form.
6. Record the deployed SHA, verification and screenshots before releasing the next app.

## Rollback

In Railway, select the preceding successful deployment and use its redeploy action. Record its source SHA and rerun the affected live checks. Do not force-push a branch as rollback.
