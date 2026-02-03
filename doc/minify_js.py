#!/usr/bin/env python3
"""
<<<<<<< HEAD
Simple JavaScript minifier for OpenCV documentation build.
Removes comments and excess whitespace to reduce file size.
=======
JavaScript Minification Script for OpenCV Documentation Build

This script minifies JavaScript files using Python's built-in libraries only.
No external dependencies required.

Usage:
    python minify_js.py input.js output.min.js
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
"""

import sys
import re

<<<<<<< HEAD
def minify_js(content):
    """Minify JavaScript by removing comments and whitespace."""
    # Remove single-line comments (but preserve URLs)
    content = re.sub(r'(?<!:)//[^\n]*', '', content)
    
    # Remove multi-line comments
    content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    
    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in content.split('\n')]
    
    # Remove empty lines
    lines = [line for line in lines if line]
    
    # Join with spaces
    result = ' '.join(lines)
    
    # Reduce multiple spaces to single space
    result = re.sub(r'\s+', ' ', result)
    
    # Remove spaces around operators and punctuation
    result = re.sub(r'\s*([{}();,=+\-*/<>!&|:])\s*', r'\1', result)
    
    return result.strip()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: minify_js.py input.js output.min.js')
=======

def minify_js(input_file, output_file):
    """
    Minify JavaScript file using basic transformations.
    
    This is a simple minifier that:
    - Removes single-line comments (// ...)
    - Removes multi-line comments (/* ... */)
    - Removes leading/trailing whitespace
    - Reduces multiple spaces to single space
    - Preserves strings and regexes
    
    Args:
        input_file: Path to input JavaScript file
        output_file: Path to output minified file
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Remove single-line comments but preserve URLs (http://, https://)
    code = re.sub(r'(?<!:)//(?!/).*?(?=\n|$)', '', code)
    
    # Remove multi-line comments
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    
    # Remove leading/trailing whitespace from each line
    lines = [line.strip() for line in code.split('\n')]
    
    # Join lines and reduce multiple spaces
    code = ' '.join(lines)
    code = re.sub(r'\s+', ' ', code)
    
    # Remove spaces around operators and punctuation
    code = re.sub(r'\s*([{}();,:])\s*', r'\1', code)
    code = re.sub(r'\s*([=+\-*/%&|^!<>])\s*', r'\1', code)
    
    # Write minified output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(code)
    
    # Report compression
    input_size = len(open(input_file, 'r', encoding='utf-8').read())
    output_size = len(code)
    reduction = ((input_size - output_size) / input_size * 100) if input_size > 0 else 0
    
    print(f"Minified {input_file} -> {output_file}")
    print(f"Size: {input_size} bytes -> {output_size} bytes ({reduction:.1f}% reduction)")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python minify_js.py input.js output.min.js")
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
<<<<<<< HEAD
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        minified = minify_js(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(minified)
        
        original_size = len(content)
        minified_size = len(minified)
        reduction = 100 - (minified_size * 100 / original_size)
        
        print(f'Minified {input_file} -> {output_file}')
        print(f'Size: {original_size} -> {minified_size} bytes ({reduction:.1f}% reduction)')
        
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
=======
        minify_js(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        sys.exit(1)
