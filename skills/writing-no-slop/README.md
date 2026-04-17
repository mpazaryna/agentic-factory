# anti-slop

Background style guide that strips LLM clichés and produces clean, human-sounding prose.

## What It Does

This skill is background knowledge — Claude loads it automatically when writing prose, articles, or documentation. It is not invoked directly.

It enforces three things:

- **Banned vocabulary**: A specific list of overused AI-generated words and phrases (delve, transformative, paradigm-shifting, seamlessly integrates, etc.) that must not appear unless the user wrote them first.
- **Banned sentence structures**: Patterns like "It isn't just X, it's Y" and "This is where X comes in" that signal low-effort writing.
- **Structural discipline**: Full paragraphs over bullet lists, sparse headings, no em dashes, no question-as-hook openers, no meta transition sentences.

Claude silently checks output against these rules before presenting it and removes violations without explaining what changed.

## When Claude Applies It

Any writing task — blog posts, documentation, README files, articles, emails — triggers this skill. It applies alongside any other writing skill (e.g., `writing`).

## See Also

- `writing` — Full blog post creation workflow with SEO and approval steps
