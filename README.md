# Accessibility Checker 🦆

Python CLI tool for automated WCAG accessibility compliance auditing of websites. Analyzes web pages for common accessibility issues and generates detailed reports with actionable remediation guidance.

## Features

- **Image Accessibility**: Validates alt text presence and quality
- **Interactive Elements**: Identifies buttons and links without accessible labels
- **Link Quality**: Detects vague link text patterns (e.g., "click here", "read more")
- **Form Validation**: Verifies proper label associations for form inputs
- **Semantic Structure**: Analyzes heading hierarchy and HTML5 semantic elements
- **Comprehensive Reporting**: Generates formatted accessibility audit reports with scoring

## Requirements

- Python 3.7+
- BeautifulSoup4
- Requests

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python check_accessibility.py <url>
```

### Examples

```bash
# Audit a single webpage
python check_accessibility.py https://example.com

# Audit a GitHub repository page
python check_accessibility.py https://github.com
```

## Sample Output

![Accessibility Checker Output](Accessibility%20Checker.png)

*See [SAMPLE_REPORT.md](SAMPLE_REPORT.md) for detailed analysis and recommendations.*

## Technical Stack

- **Python 3**: Core programming language
- **BeautifulSoup4**: HTML/XML parsing and DOM traversal
- **Requests**: HTTP library for web page retrieval
- **Built with goose**: AI-assisted development workflow

## About

This tool was developed to demonstrate the effectiveness of AI-assisted development in creating practical developer tooling. It serves as both a functional accessibility auditing solution and an exploration of accessibility-first design principles, making WCAG compliance testing more accessible to developers of all experience levels.

## License

MIT License

Copyright (c) 2025 eriperspective

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


