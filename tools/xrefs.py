"""Turn Quarto cross-references to another book into plain links.

numbers(docs) reads a rendered Quarto book and returns {id: (href, text)}, where
text is what Quarto shows for the reference there ("Chapter 31", "Section 31.4",
"Figure 31.2", "Table 5.1", "Appendix A").

rewrite(files, ids, nums, base) replaces each @id in the given .qmd files, for
ids in `ids`, by [text](base + href).
"""
import os, re, html

def numbers(docs):
    out = {}
    for f in sorted(os.listdir(docs)):
        if not f.endswith(".html"):
            continue
        s = open(os.path.join(docs, f), encoding="utf-8").read()
        if 'http-equiv="refresh"' in s:
            continue
        # quarto-xref links seen anywhere give the exact text
        for m in re.finditer(r'<a href="\./([^"#]+)(#[^"]*)?" class="quarto-xref">(.*?)</a>', s, re.S):
            href, frag, text = m.group(1), m.group(2) or "", html.unescape(re.sub("<[^>]+>", "", m.group(3)))
            i = frag[1:] if frag else None
            text = text.replace("\xa0", " ").strip()
            if i:
                out.setdefault(i, (href + frag, text))
        # chapter title
        m = re.search(r'<span id="((?:sec)-[\w-]+)" class="quarto-section-identifier"><span class="chapter-number">([^<]+)</span>', s)
        if m:
            num = m.group(2).strip()
            word = "Appendix" if re.fullmatch(r"[A-Z]", num) else "Chapter"
            out[m.group(1)] = (f, f"{word} {num}")
        for m in re.finditer(r'<section id="(sec-[\w-]+)"[^>]*data-number="([^"]+)"', s):
            out[m.group(1)] = (f"{f}#{m.group(1)}", f"Section {m.group(2).strip()}")
        for m in re.finditer(r'id="((fig|tbl)-[\w-]+)".{0,4000}?(Figure|Table)(?:&nbsp;|\xa0| )([0-9A-Z]+\.[0-9]+)', s, re.S):
            out.setdefault(m.group(1), (f"{f}#{m.group(1)}", f"{m.group(3)} {m.group(4)}"))
    return out

REF = re.compile(r"@((?:sec|fig|tbl)-[\w-]*\w)")

def rewrite(files, ids, nums, base):
    missing = set(); count = 0
    for p in files:
        raw = open(p, encoding="utf-8").read()
        nl = "\r\n" if "\r\n" in raw else "\n"
        s = raw.replace("\r\n", "\n")
        def sub(m):
            nonlocal count
            i = m.group(1)
            if i not in ids:
                return m.group(0)
            if i not in nums:
                missing.add(i); return m.group(0)
            count += 1
            href, text = nums[i]
            return f"[{text}]({base}{href})"
        # leave code chunks alone
        parts = re.split(r"(```.*?```)", s, flags=re.S)
        s = "".join(x if x.startswith("```") else REF.sub(sub, x) for x in parts)
        open(p, "w", encoding="utf-8", newline="").write(s.replace("\n", nl))
    return count, missing
