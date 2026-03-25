# readme.md

## Project Overview

Statistics Peek is a Jekyll-based GitHub Pages site for hosting small statistical reports in Spanish. It uses the Minima theme with custom CSS for enhanced table presentation.

## Development Commands

```bash
# Local development server
bundle exec jekyll serve

# Build site (for preview without server)
bundle exec jekyll build
```

No build step is required for deployment - pushing to main branch triggers automatic GitHub Pages builds.

## Pages
- https://github.com/memoteca/memoteca.github.io/actions
- https://memoteca.github.io/ 

## Architecture
- **Static Site Generator**: Jekyll with GitHub Pages hosting
- **Theme**: Minima (extends via `assets/css/style.css`)
- **Markdown**: Kramdown with GitHub Flavored Markdown

### Key Directories

- `_posts/` - Published articles (format: `YYYY-MM-DD-title.md`)
- `_drafts/` - Work-in-progress posts (not deployed)
- `assets/main.scss` - Custom styling, especially table formatting

## Content Guidelines

- Posts written in Spanish, code/comments in English
- Tables can use Markdown syntax or HTML with CSS classes
- Use `.num` class on `<td>` elements for right-aligned numeric columns

## CSS Classes for Tables

```html
<td class="num">1.234,56</td>  <!-- Right-aligned, tabular numbers -->
```
