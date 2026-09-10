---
name: deep-research
description: Multi-source deep research using the Firecrawl MCP (web search, scraping, crawling, and a scientific paper index) with optional Exa. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence and citations.
metadata:
  origin: ECC
---

# Deep Research

> **Drift-prone skill.** Firecrawl/Exa MCP tool names, quotas, and result
> shapes change. Verify the configured MCP tools and current API docs before
> promising coverage or quoting live source counts. Tool inventory and call
> signatures below were verified against `firecrawl-fastmcp` v3.22.4 on
> 2026-07-25.

Produce thorough, cited research reports from multiple web sources using the
Firecrawl MCP tools (and Exa, if configured).

## When to Activate

- User asks to research any topic in depth
- Competitive analysis, technology evaluation, or market sizing
- Due diligence on companies, investors, or technologies
- Academic or engineering questions where papers and repos are the real sources
- Any question requiring synthesis from multiple sources
- User says "research", "deep dive", "investigate", or "what's the current state of"

## Tooling

**Configured for this project:** Firecrawl MCP over HTTP at
`https://mcp.firecrawl.dev/v2/mcp`, registered at local scope in
`~/.claude.json` with a `Authorization: Bearer` header. The API key lives in
that config only — never copy it into this repo, a skill file, or a report.

Exa is **not** configured. Its calls are kept below as an optional second
source; skip them unless `web_search_exa` actually appears in the tool list.

Available Firecrawl tools, by job:

| Job | Tools |
| --- | --- |
| Discovery | `firecrawl_search`, `firecrawl_map` |
| Reading | `firecrawl_scrape`, `firecrawl_crawl`, `firecrawl_check_crawl_status` |
| Structured pulls | `firecrawl_extract`, `firecrawl_agent`, `firecrawl_agent_status` |
| Local documents | `firecrawl_parse` |
| Academic + code | `firecrawl_research_search_papers`, `firecrawl_research_inspect_paper`, `firecrawl_research_read_paper`, `firecrawl_research_related_papers`, `firecrawl_research_search_github` |
| Live pages | `firecrawl_interact`, `firecrawl_interact_stop` |
| Recurring checks | `firecrawl_monitor_*` |

If none of these are in the tool list, the MCP server is not connected —
see **Troubleshooting** at the bottom before promising any coverage.

## Workflow

### Step 1: Understand the Goal

Ask 1-2 quick clarifying questions:
- "What's your goal — learning, making a decision, or writing something?"
- "Any specific angle or depth you want?"

If the user says "just research it" — skip ahead with reasonable defaults.

### Step 2: Plan the Research

Break the topic into 3-5 research sub-questions. Example:
- Topic: "Impact of AI on healthcare"
  - What are the main AI applications in healthcare today?
  - What clinical outcomes have been measured?
  - What are the regulatory challenges?
  - What companies are leading this space?
  - What's the market size and growth trajectory?

Then pick the right entry point per sub-question:

- **Open-ended / current state** -> `firecrawl_search`
- **Peer-reviewed claims, benchmarks, prior art** -> the research index (Step 3b)
- **Everything on one known site** -> `firecrawl_map` then `firecrawl_scrape`
- **Same field across many known URLs** -> `firecrawl_extract`
- **A local PDF/DOCX the user supplied** -> `firecrawl_parse`

### Step 3: Execute Multi-Source Search

For EACH sub-question, search using available MCP tools.

**With firecrawl** — `query` is the only required argument:

```
firecrawl_search(query: "<sub-question keywords>", limit: 8)
```

Useful narrowing arguments:

- `sources: [{type: "web"}, {type: "news"}]` — `web`, `news`, or `images`
- `categories: ["research"]` — `github`, `research`, or `pdf`
- `tbs` — time filter for recency (e.g. past year)
- `includeDomains` / `excludeDomains` — pin to or exclude specific sites
- `location` — region-specific results
- `scrapeOptions` — return full page content with the results instead of
  snippets only, saving a second round trip on high-confidence hits

**With exa** (only if configured):
```
web_search_exa(query: "<sub-question keywords>", numResults: 8)
web_search_advanced_exa(query: "<keywords>", numResults: 5, startPublishedDate: "2025-01-01")
```

**Search strategy:**
- Use 2-3 different keyword variations per sub-question
- Mix general and news-focused queries
- Aim for 15-30 unique sources total
- Prioritize: academic, official, reputable news > blogs > forums

### Step 3b: Search the Research Index

Use this whenever the topic is scientific, technical, or engineering — it
searches a purpose-built paper index (metadata plus full-text passages) and
GitHub history, which plain web search will not surface well.

```
firecrawl_research_search_papers(query: "<natural-language question>", k: 10)
    optional: authors, categories, from: "YYYY-MM-DD", to: "YYYY-MM-DD"

firecrawl_research_inspect_paper(paperId: "<id>")
    metadata for a paper returned above

firecrawl_research_read_paper(paperId: "<id>", question: "<what you need>", k: 5)
    returns the top full-text passages answering that question

firecrawl_research_related_papers(seed_ids: ["<id>"], intent: "<why>",
                                  mode: "similar" | "citers" | "references")
    citation expansion — "citers" for follow-on work, "references" for foundations

firecrawl_research_search_github(query: "<query>", k: 10)
    issues, PRs, discussions, and READMEs
```

Typical chain: `search_papers` -> `inspect_paper` on the promising hits ->
`read_paper` with your actual sub-question -> `related_papers` with
`mode: "citers"` to find what superseded it. Cite the paper, not the summary.

### Step 4: Deep-Read Key Sources

For the most promising URLs, fetch full content:

**With firecrawl** — `url` is the only required argument:
```
firecrawl_scrape(url: "<url>", onlyMainContent: true)
```

- `formats` accepts `markdown`, `summary`, `links`, `html`, `json`, and more —
  `["markdown"]` is the default choice; add `summary` for long pages
- `onlyMainContent: true` strips nav and boilerplate
- `maxAge` serves a recent cached copy, which is much faster on re-reads
- `waitFor` helps on JS-heavy pages that render late
- Public document URLs (PDF, DOCX) go through `scrape` — not `parse`

**With exa** (only if configured):
```
crawling_exa(url: "<url>", tokensNum: 5000)
```

Read 3-5 key sources in full for depth. Do not rely only on search snippets.

**Scaling past single pages:**

```
firecrawl_map(url: "<site>", search: "<filter>", limit: 100)
    URL discovery — cheap way to see what a site holds before crawling

firecrawl_crawl(url: "<site>", limit: 50, includePaths: [...], excludePaths: [...])
    bulk extraction; poll firecrawl_check_crawl_status for the result

firecrawl_extract(urls: ["<url>", ...], prompt: "<what to pull>", schema: {...})
    same structured fields across many pages — ideal for comparison tables
```

Prefer `map` then targeted `scrape` over a broad `crawl`; crawls are slow and
burn quota fast.

**Local documents:** when the user supplies a file rather than a URL, use
`firecrawl_parse(filePath: "<path>")` — it handles PDF, DOCX, DOC, ODT, RTF,
XLSX, XLS, and HTML up to 50 MB and returns clean markdown. `formats` and
`onlyMainContent` work the same as on `scrape`.

### Step 5: Synthesize and Write Report

Structure the report:

```markdown
# [Topic]: Research Report
*Generated: [date] | Sources: [N] | Confidence: [High/Medium/Low]*

## Executive Summary
[3-5 sentence overview of key findings]

## 1. [First Major Theme]
[Findings with inline citations]
- Key point ([Source Name](url))
- Supporting data ([Source Name](url))

## 2. [Second Major Theme]
...

## 3. [Third Major Theme]
...

## Key Takeaways
- [Actionable insight 1]
- [Actionable insight 2]
- [Actionable insight 3]

## Sources
1. [Title](url) — [one-line summary]
2. ...

## Methodology
Searched [N] queries across web and news. Analyzed [M] sources.
Sub-questions investigated: [list]
```

### Step 6: Deliver

- **Short topics**: Post the full report in chat
- **Long reports**: Post the executive summary + key takeaways, save full report to a file

## Parallel Research with Subagents

For broad topics, use subagents (the Agent tool) to parallelize:

```
Launch 3 research agents in parallel:
1. Agent 1: Research sub-questions 1-2
2. Agent 2: Research sub-questions 3-4
3. Agent 3: Research sub-question 5 + cross-cutting themes
```

Each agent searches, reads sources, and returns findings. The main session
synthesizes into the final report. Sub-questions are independent by
construction, so fan them out rather than running them in sequence.

## Quality Rules

1. **Every claim needs a source.** No unsourced assertions.
2. **Cross-reference.** If only one source says it, flag it as unverified.
3. **Recency matters.** Prefer sources from the last 12 months.
4. **Acknowledge gaps.** If you couldn't find good info on a sub-question, say so.
5. **No hallucination.** If you don't know, say "insufficient data found."
6. **Separate fact from inference.** Label estimates, projections, and opinions clearly.
7. **Cite the primary source.** For technical claims, cite the paper or repo
   found via the research index, not a blog post summarizing it.
8. **Report real counts.** Source counts in the report must match what was
   actually fetched — never round up or estimate coverage.

## Troubleshooting

- **No `firecrawl_*` tools in the tool list** — the MCP server isn't connected.
  It is registered per-project in `~/.claude.json`, and `/mcp` only reads the
  server list at startup, so restart Claude Code. Re-add with:
  `claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp --header "Authorization: Bearer <key>"`.
  Do not use `--scope project` — that writes the key into a `.mcp.json` in the
  repo.
- **Auth errors** — the key is a header on the MCP server entry in
  `~/.claude.json`. Without a valid key the endpoint still serves search,
  scrape, interact, and parse on a rate-limited keyless tier, but crawl, map,
  monitor, extract, and agent all require the key. Say so in the report rather
  than silently narrowing coverage.
- **Rate limited** — reduce `limit`, lean on `maxAge` for cached reads, and
  prefer `map` + targeted `scrape` over `crawl`.
- **A call fails or returns something unexpected** — don't guess at parameters.
  Firecrawl's API reference at https://docs.firecrawl.dev is the source of
  truth for request and response shapes.

## Examples

```
"Research the current state of nuclear fusion energy"
"Deep dive into Rust vs Go for backend services in 2026"
"Research the best strategies for bootstrapping a SaaS business"
"What's happening with the US housing market right now?"
"Investigate the competitive landscape for AI code editors"
```
