# Architecture

AI Offer Creator is a standalone Flask application embedded in the members' My Resources page.

`app.py` serves the page from templates/index.html. `GET /api/strategies`, `POST /api/generate` and `POST /api/export-pdf`. The generator uses OpenAI; ReportLab builds branded and pro PDFs.

The members interface is bundled in `static/members/`: `app.css`, `look.css`, `tool.css`, and the images they use. Cross-origin frames cannot inherit their parent's styles. The template's stylesheet query values are the first 10 characters of each file's SHA-256; update them when CSS changes. `tool.css` adapts the existing layout.

`requirements.txt` pins dependencies and `Procfile` defines the hosted entry point.
