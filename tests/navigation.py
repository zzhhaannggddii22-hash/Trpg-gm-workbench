from pathlib import Path
import json
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit
HERE = Path(__file__).resolve().parent

def slug(text):
    text = re.sub(r"<[^>]*>", "", text.casefold())
    return re.sub(r"[^\w\s-]", "", text).replace(" ", "-")


def scan_links(documents, known_paths=None):
    parsed = json.loads(subprocess.check_output(
        ["node", str(HERE / "scan_markdown.cjs")],
        input=json.dumps(documents, ensure_ascii=False).encode(),
    ))
    # Markdown documents are parsed for links/headings, but links may validly
    # target scripts, fixtures, images, or other tracked non-Markdown assets.
    known_paths = set(known_paths or documents)
    dirs = {""}
    for path in known_paths:
        while "/" in path:
            path = posixpath.dirname(path)
            dirs.add(path)
    anchors = {}
    for path, item in parsed.items():
        known = set()
        for heading in item["headings"]:
            base = slug(heading)
            name = base
            ordinal = 1
            while name in known:
                name = f"{base}-{ordinal}"
                ordinal += 1
            known.add(name)
        known.update(re.findall(r'<a\s+(?:name|id)="([^"]+)"', documents[path]))
        anchors[path] = known
    result = {"distinct_external_url_count": 0, "local_links": 0, "missing_paths": [], "anchor_candidates": []}
    external = set()
    for path, item in parsed.items():
        for href, raw in item["links"]:
            try:
                parts = urlsplit(href)
            except ValueError:
                continue
            if parts.scheme or parts.netloc:
                external.add(href)
                continue
            result["local_links"] += 1
            target = unquote(parts.path)
            dest = (posixpath.normpath(target.lstrip("/")) if target.startswith("/") else
                    posixpath.normpath(posixpath.join(posixpath.dirname(path), target))) if target else path
            dest = "" if dest == "." else dest
            offset = documents[path].find(raw)
            line = 1 + documents[path].count("\n", 0, offset) if offset >= 0 else None
            entry = {"file": path, "line": line, "href": href, "resolved": dest}
            if dest not in known_paths and dest not in dirs:
                result["missing_paths"].append(entry)
            elif parts.fragment and dest in anchors and unquote(parts.fragment) not in anchors[dest]:
                result["anchor_candidates"].append(entry)
    result["distinct_external_url_count"] = len(external)
    return result
