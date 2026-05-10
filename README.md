# MD2PDF

**MD2PDF** is a premium, client-side web application designed to transform Markdown documents into beautifully formatted, print-ready PDF files. Built with a focus on aesthetics and simplicity, it leverages the power of **PyScript** to handle Markdown processing directly in your browser.

## Overview

In a world where documentation is predominantly written in Markdown, there is often a need to share these documents in a more formal, universally readable format like PDF. MD2PDF bridges this gap by providing a live-preview environment that optimizes your Markdown for the "reading experience."

Unlike heavy desktop applications, MD2PDF is a **completely static web app**. No servers, no installations, just pure browser-based conversion.

## Key Features

- **Live Preview**: See your changes in real-time as you type.
- **Premium Design**: A modern, glassmorphic interface designed for focus and productivity.
- **Print Optimized**: Custom CSS media queries ensure that the exported PDF looks professional, with clean typography and proper spacing.
- **Privacy First**: All processing happens locally in your browser. Your data never leaves your machine.
- **Static & Portable**: Can be hosted on GitHub Pages, Vercel, or even run locally without a backend.

## Technology Stack

- **HTML5 & CSS3**: For structure and high-end styling (Inter & Fira Code typography).
- **PyScript**: To run Python code in the browser for robust Markdown parsing.
- **Python `markdown` Library**: A high-quality parser used for the core conversion logic.
- **Browser Native Print**: Utilized for reliable PDF generation with full CSS support.

## File Structure

```text
MD2PDF/
├── index.html       # Main entry point and UI structure
├── style.css        # Premium styling and print-specific optimizations
├── main.py          # PyScript logic for Markdown conversion
├── pyscript.toml    # Configuration and dependencies for PyScript
└── README.md        # Project documentation (you are here)
```

## Background & Rationale

Most Markdown to PDF converters are either CLI tools that are hard to use for non-developers, or online services that require you to upload your files. MD2PDF was created to provide a **"Zero-Setup"** alternative that combines the ease of a web interface with the privacy and power of local processing.

By using **PyScript**, we bring the mature ecosystem of Python's Markdown processing to the web, ensuring that complex Markdown features (like TOCs and tables) are handled correctly.

## Getting Started

### Prerequisites
You only need a modern web browser (Chrome, Firefox, Edge, or Safari).

### Usage
1. Open `index.html` in your browser.
2. Type or paste your Markdown text into the left-hand editor.
3. Observe the live preview on the right.
4. Click the **"Export PDF"** button to open the browser's print dialog.
5. Set the destination to **"Save as PDF"** and ensure "Background graphics" is enabled for the best look.
