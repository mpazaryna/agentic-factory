# digest

Extract key points from any URL and organize the output into `~/Documents/zz-kairos/digest/`.

## Usage

```
/digest <url>
```

Works with YouTube URLs and web articles. Auto-detects the source type.

## What it does

1. Fetches the content (transcript for YouTube, article text for web)
2. Extracts key points via Claude using the `extract_wisdom` pattern
3. Writes a structured Markdown file to `~/Documents/zz-kairos/digest/`
4. Runs `organize` to classify the new file in place
5. Reports the output path
