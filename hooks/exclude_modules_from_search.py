"""Strip the modules.html record from the search index.

The modules page is just a flat TOC linking to every module page; without
this hook it pollutes search results with link-only entries that out-rank
no actual content. The mkdocs-exclude-search plugin can't do this for us
because it treats any URL without a slash as a 'required root record'
and refuses to drop it — incompatible with `use_directory_urls: false`.
"""

import json
from pathlib import Path


def on_post_build(config, **_):
    idx = Path(config["site_dir"]) / "search" / "search_index.json"
    if not idx.exists():
        return
    data = json.loads(idx.read_text(encoding="utf-8"))
    data["docs"] = [
        d for d in data["docs"]
        if not d["location"].startswith("modules.html")
    ]
    idx.write_text(json.dumps(data), encoding="utf-8")
