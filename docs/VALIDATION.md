# Validation

Test the changed seam and sibling checks that touch changed files. The existing `tests/browser/` reports describe earlier source checks, not the current production deployment.

Run the actual Flask app, then check its form and results at 1280 and 390 pixels, including the embedded member page. Verify keyboard focus, reduced motion, readable contrast and no horizontal overflow. Use the delivered members interface as the visual comparison.

Generate 2 offers using keys returned by `/api/strategies` (for example `cash`). Download branded and pro PDFs and confirm both open. Reset the form.

Use actual UI actions so requests come from the tool's own JavaScript. For exports, require a successful response whose bytes start with `%PDF-` and open the PDF. Never substitute source-string assertions for executed behavior.

For styling changes, remove the actual `tool.css` link, require the focused browser presentation assertion to exit nonzero, then restore the source byte-identically. Keep positive and negative evidence bound to the source SHA.
