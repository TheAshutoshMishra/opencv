#!/usr/bin/env python3
"""
Verify Prism.js build output for OpenCV documentation
Checks for proper minification and exclusion of source files
"""

import os
import sys
from pathlib import Path

def check_file_exists(html_dir, filename):
    """Check if a file exists in the HTML output directory"""
    filepath = html_dir / filename
    exists = filepath.exists()
    size = filepath.stat().st_size if exists else 0
    return exists, size

def check_tutorial_references(html_dir):
    """Check tutorial HTML files for correct script references"""
    # Find a tutorial file to check
    tutorial_patterns = [
        "tutorial_js_usage.html",
        "tutorial_js_setup.html",
        "tutorial_js_intro.html"
    ]
    
    found_tutorials = []
    for pattern in tutorial_patterns:
        filepath = html_dir / pattern
        if filepath.exists():
            found_tutorials.append(filepath)
            break
    
    if not found_tutorials:
        # Try to find any tutorial file
        for file in html_dir.glob("tutorial_js_*.html"):
            found_tutorials.append(file)
            break
    
    if not found_tutorials:
        return None, "No tutorial HTML files found"
    
    tutorial_file = found_tutorials[0]
    with open(tutorial_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_minified_js = 'prism.min.js' in content
    has_minified_textarea = 'prism-textarea.min.js' in content
    has_minified_css = 'prism.min.css' in content
    has_unminified_js = 'src="prism.js"' in content or 'src=\'prism.js\'' in content
    has_unminified_textarea = 'src="prism-textarea.js"' in content or 'src=\'prism-textarea.js\'' in content
    
    return {
        'file': tutorial_file.name,
        'has_minified_js': has_minified_js,
        'has_minified_textarea': has_minified_textarea,
        'has_minified_css': has_minified_css,
        'has_unminified_js': has_unminified_js,
        'has_unminified_textarea': has_unminified_textarea
    }, None

def check_for_duplicates(html_dir):
    """Check for both minified and unminified versions (indicates exclusion failure)"""
    files_in_dir = [f.name for f in html_dir.glob("prism*")]
    
    # Expected files (minified only)
    expected = ['prism.min.js', 'prism-textarea.min.js', 'prism.min.css']
    
    # Unwanted files (source/unminified versions)
    unwanted = ['prism.js', 'prism-textarea.js', 'prism.css']
    
    found_unwanted = [f for f in unwanted if f in files_in_dir]
    found_expected = [f for f in expected if f in files_in_dir]
    
    return {
        'all_prism_files': files_in_dir,
        'expected_found': found_expected,
        'unwanted_found': found_unwanted
    }

def main():
    # Determine HTML output directory
    if len(sys.argv) > 1:
        html_dir = Path(sys.argv[1])
    else:
        # Default path
        html_dir = Path("E:/contribution/opencv/build/doc/doxygen/html")
    
    if not html_dir.exists():
        print(f"❌ ERROR: HTML directory does not exist: {html_dir}")
        print(f"\nAlternative paths to check:")
        print(f"  - E:\\contribution\\opencv\\opencv\\build\\doc\\doxygen\\html")
        print(f"  - {Path.cwd() / 'build/doc/doxygen/html'}")
        return 1
    
    print(f"🔍 Verifying Prism.js build output in:\n   {html_dir}\n")
    print("=" * 70)
    
    # Test 1: Check required files exist
    print("\n📋 TEST 1: Required Minified Files")
    print("-" * 70)
    
    required_files = [
        'prism.min.js',
        'prism-textarea.min.js',
        'prism.min.css'
    ]
    
    all_exist = True
    for filename in required_files:
        exists, size = check_file_exists(html_dir, filename)
        status = "✅" if exists else "❌"
        size_str = f"({size:,} bytes)" if exists else "(missing)"
        print(f"{status} {filename:30s} {size_str}")
        if not exists:
            all_exist = False
    
    if all_exist:
        print("\n✅ All required minified files are present")
    else:
        print("\n❌ Some required files are missing!")
    
    # Test 2: Check for unwanted duplicates
    print("\n📋 TEST 2: Check for Duplicate/Unwanted Files")
    print("-" * 70)
    
    dup_check = check_for_duplicates(html_dir)
    
    if dup_check['unwanted_found']:
        print(f"❌ FAILURE: Unwanted source files found in output!")
        print(f"   This means the exclusion loop FAILED.")
        print(f"\n   Unwanted files: {', '.join(dup_check['unwanted_found'])}")
        all_exist = False
    else:
        print(f"✅ No unwanted source files in output directory")
    
    print(f"\n   All Prism files in directory: {', '.join(dup_check['all_prism_files']) if dup_check['all_prism_files'] else 'None'}")
    
    # Test 3: Check tutorial HTML references
    print("\n📋 TEST 3: Tutorial HTML Script References")
    print("-" * 70)
    
    tutorial_check, error = check_tutorial_references(html_dir)
    
    if error:
        print(f"⚠️  WARNING: {error}")
    elif tutorial_check:
        print(f"📄 Checking: {tutorial_check['file']}")
        print()
        
        if tutorial_check['has_minified_js']:
            print(f"   ✅ References prism.min.js (correct)")
        else:
            print(f"   ❌ Does NOT reference prism.min.js (wrong!)")
            all_exist = False
        
        if tutorial_check['has_minified_textarea']:
            print(f"   ✅ References prism-textarea.min.js (correct)")
        else:
            print(f"   ❌ Does NOT reference prism-textarea.min.js (wrong!)")
            all_exist = False
        
        if tutorial_check['has_minified_css']:
            print(f"   ✅ References prism.min.css (correct)")
        else:
            print(f"   ❌ Does NOT reference prism.min.css (wrong!)")
            all_exist = False
        
        if tutorial_check['has_unminified_js']:
            print(f"   ❌ WRONG: References unminified prism.js!")
            all_exist = False
        
        if tutorial_check['has_unminified_textarea']:
            print(f"   ❌ WRONG: References unminified prism-textarea.js!")
            all_exist = False
    
    # Final verdict
    print("\n" + "=" * 70)
    if all_exist and not dup_check['unwanted_found']:
        print("🎉 SUCCESS: All checks passed!")
        print("   - Minified files are present")
        print("   - No source file duplicates")
        print("   - Tutorial references are correct")
        return 0
    else:
        print("❌ FAILURE: Some checks failed")
        print("\n   Possible causes:")
        print("   1. CMake configure step didn't run")
        print("   2. BUILD_DOCS=ON not set")
        print("   3. Exclusion filters in CMakeLists.txt not working")
        print("   4. Build incomplete (try: cmake --build . --target doxygen)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
