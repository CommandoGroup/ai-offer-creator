"""Check the REC test note in a GitHub pull_request event."""
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit


def check(body, tree):
    text = re.sub(r"<!--.*?(?:-->|$)", "", body or "", flags=re.S)
    sections = re.split(r"^## Test note[ \t]*\r?$", text, flags=re.M)
    if len(sections) != 2:
        raise ValueError("Include exactly one '## Test note' section from the PR template.")
    note = re.split(r"^#{1,2} ", sections[1], maxsplit=1, flags=re.M)[0]
    fields = {}
    for key in ("Tested tree", "Environment", "Verified by", "Tested", "Observed", "Evidence", "Staging"):
        values = re.findall(r"^- " + key + r":[ \t]*([^\r\n]*)", note, flags=re.M)
        if len(values) != 1 or values[0].strip().lower() in ("", "todo", "tbd", "...", "n/a"):
            raise ValueError(f"Fill in '{key}' once in the test note.")
        fields[key] = values[0].strip()
    if fields["Tested tree"] != tree:
        raise ValueError(f"Test evidence must cover the proposed merge tree {tree}.")
    link = urlsplit(fields["Evidence"])
    if link.scheme != "https" or not link.hostname or link.username or link.password or re.search(r"\s", fields["Evidence"]):
        raise ValueError("Use a plain HTTPS evidence link without embedded credentials.")
    if not re.fullmatch(r"(?:N/A - \S.*|[^|]+\s*\|\s*[0-9a-fA-F]{64})", fields["Staging"]):
        raise ValueError("Supply the staging deployment ID | installed SHA-256, or N/A - reason.")


if __name__ == "__main__":
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text(encoding="utf-8"))
    tree = subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], text=True).strip()
    try:
        check(event["pull_request"]["body"], tree)
    except ValueError as error:
        raise SystemExit(str(error))
    print(f"Test note present for proposed merge tree {tree}.")
