# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static site generator that converts markdown to HTML. The project uses Python and follows a node-based architecture for representing text and HTML content.

## Commands

**Run the application:**
```bash
./main.sh
# or
python3 src/main.py
```

**Run all tests:**
```bash
./test.sh
# or
python3 -m unittest discover -s src
```

**Run a single test file:**
```bash
python3 -m unittest src.test_textnode
python3 -m unittest src.test_htmlnode
```

## Architecture

The codebase uses a two-layer node architecture:

1. **TextNode Layer** (`textnode.py`): Represents markdown-style text with different types (plain text, bold, italic, code, links, images). This is the intermediate representation layer that parses markdown syntax.

2. **HTMLNode Layer** (`htmlnode.py`): Represents HTML elements with tags, values, children, and properties. TextNodes are converted to HTMLNodes, which are then rendered to HTML strings.

The conversion flow is: Markdown → TextNode → HTMLNode → HTML string

### Key Classes

- **TextNode**: Has `text`, `text_type` (from TextType enum), and optional `url` for links/images
- **HtmlNode**: Has `tag`, `value`, `children`, and `props`. The `to_html()` method must be implemented by subclasses. The `props_to_html()` helper converts the props dict to HTML attribute strings.

### Directory Structure

- `src/`: All Python source code
- `content/`: Source markdown files (currently empty)
- `static/`: Static assets to be copied to output
- `public/`: Generated HTML output directory
- `template.html`: HTML template for generated pages
