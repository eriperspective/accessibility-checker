#!/usr/bin/env python3
"""
Accessibility Checker - CLI tool to audit websites for accessibility issues
Built with AI-assisted development using goose.
"""

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def print_header():
    """Print formatted header"""
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║     🦆 ACCESSIBILITY CHECKER v1.0                    ║")
    print("║     Powered by AI-Assisted Development               ║")
    print("╠══════════════════════════════════════════════════════╣\n")

def print_footer():
    """Print formatted footer"""
    print("\n╚══════════════════════════════════════════════════════╝\n")

def check_images(soup):
    """Check for images without alt text"""
    issues = []
    images = soup.find_all('img')
    
    for img in images:
        if not img.get('alt') or img.get('alt').strip() == '':
            src = img.get('src', 'unknown')
            issues.append(f"Image missing alt text: {src[:50]}")
    
    return issues

def check_buttons(soup):
    """Check for buttons without labels"""
    issues = []
    buttons = soup.find_all('button')
    
    for button in buttons:
        if not button.get('aria-label') and not button.text.strip():
            issues.append(f"Button without accessible label")
    
    return issues

def check_links(soup):
    """Check for links with vague text"""
    issues = []
    vague_texts = ['click here', 'read more', 'here', 'link', 'more']
    links = soup.find_all('a')
    
    for link in links:
        text = link.text.strip().lower()
        if text in vague_texts:
            issues.append(f"Link with vague text: '{text}'")
    
    return issues

def check_headings(soup):
    """Check heading hierarchy"""
    passed = []
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    if headings:
        passed.append(f"Found {len(headings)} semantic headings")
    
    return passed

def check_forms(soup):
    """Check form accessibility"""
    passed = []
    issues = []
    
    forms = soup.find_all('form')
    for form in forms:
        inputs = form.find_all(['input', 'textarea', 'select'])
        for inp in inputs:
            label = form.find('label', {'for': inp.get('id')})
            if not label and inp.get('type') != 'hidden':
                issues.append(f"Form input without associated label")
            else:
                passed.append("Form label properly associated")
    
    return issues, passed

def calculate_score(critical, warnings, passed):
    """Calculate overall accessibility score"""
    total_checks = critical + warnings + passed
    if total_checks == 0:
        return 0
    
    # Weight: passed = 1 point, warning = 0.5 points deducted, critical = 1 point deducted
    score = (passed - critical - (warnings * 0.5)) / total_checks * 10
    return max(0, min(10, score))

def check_accessibility(url):
    """Main function to check accessibility"""
    print_header()
    print(f"Analyzing: {url}")
    
    try:
        # Fetch the page
        print("⠿ Fetching page... ", end='', flush=True)
        headers = {'User-Agent': 'Mozilla/5.0 (Accessibility Checker)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print("✓")
        
        # Parse HTML
        print("⠿ Parsing HTML... ", end='', flush=True)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("✓")
        
        # Run checks
        print("⠿ Running accessibility checks... ", end='', flush=True)
        
        critical_issues = []
        warnings = []
        passed_checks = []
        
        # Check images
        image_issues = check_images(soup)
        critical_issues.extend(image_issues)
        
        # Check buttons
        button_issues = check_buttons(soup)
        critical_issues.extend(button_issues)
        
        # Check links
        link_issues = check_links(soup)
        warnings.extend(link_issues)
        
        # Check headings
        heading_passed = check_headings(soup)
        passed_checks.extend(heading_passed)
        
        # Check forms
        form_issues, form_passed = check_forms(soup)
        critical_issues.extend(form_issues)
        passed_checks.extend(form_passed)
        
        # Basic checks
        if soup.find('html', lang=True):
            passed_checks.append("Page language attribute set")
        else:
            warnings.append("Missing page language attribute")
        
        if soup.find('meta', attrs={'name': 'viewport'}):
            passed_checks.append("Responsive viewport meta tag present")
        
        print("✓\n")
        
        # Print results
        print("╔══════════════════════════════════════════════════════╗")
        print("║                    RESULTS                           ║")
        print("╠══════════════════════════════════════════════════════╣\n")
        
        # Critical issues
        print(f"🔴 CRITICAL ISSUES ({len(critical_issues)})")
        if critical_issues:
            for issue in critical_issues[:5]:  # Show first 5
                print(f"  • {issue}")
            if len(critical_issues) > 5:
                print(f"  ... and {len(critical_issues) - 5} more")
        else:
            print("  None found!")
        print()
        
        # Warnings
        print(f"🟡 WARNINGS ({len(warnings)})")
        if warnings:
            for warning in warnings[:5]:  # Show first 5
                print(f"  • {warning}")
            if len(warnings) > 5:
                print(f"  ... and {len(warnings) - 5} more")
        else:
            print("  None found!")
        print()
        
        # Passed checks
        print(f"✅ PASSED CHECKS ({len(passed_checks)})")
        if passed_checks:
            for check in passed_checks[:5]:  # Show first 5
                print(f"  • {check}")
            if len(passed_checks) > 5:
                print(f"  ... and {len(passed_checks) - 5} more")
        print()
        
        # Calculate score
        score = calculate_score(len(critical_issues), len(warnings), len(passed_checks))
        
        print("╔══════════════════════════════════════════════════════╗")
        print(f"║  OVERALL SCORE: {score:.1f}/10                               ║")
        print("╠══════════════════════════════════════════════════════╣\n")
        
        # Recommendations
        print("TOP RECOMMENDATIONS:")
        recommendations = []
        if any('alt text' in issue for issue in critical_issues):
            recommendations.append("1. Add descriptive alt text to all images")
        if any('label' in issue.lower() for issue in critical_issues):
            recommendations.append("2. Ensure all interactive elements have proper labels")
        if any('vague text' in issue for issue in warnings):
            recommendations.append("3. Use descriptive link text instead of 'click here'")
        
        if not recommendations:
            recommendations = ["1. Great job! Continue monitoring accessibility"]
        
        for rec in recommendations[:3]:
            print(f"  {rec}")
        
        print_footer()
        
    except requests.exceptions.Timeout:
        print("\n❌ Error: Request timed out. The website took too long to respond.")
        print_footer()
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error fetching page: {e}")
        print_footer()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print_footer()
        sys.exit(1)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("\n╔══════════════════════════════════════════════════════╗")
        print("║     🦆 ACCESSIBILITY CHECKER v1.0                    ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║                                                      ║")
        print("║  Usage: python check_accessibility.py <url>          ║")
        print("║                                                      ║")
        print("║  Example:                                            ║")
        print("║  python check_accessibility.py https://example.com   ║")
        print("║                                                      ║")
        print("╚══════════════════════════════════════════════════════╝\n")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Add https:// if not present
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    check_accessibility(url)

if __name__ == "__main__":
    main()
