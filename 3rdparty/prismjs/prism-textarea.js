<<<<<<< HEAD
// Textarea syntax highlighting for OpenCV.js tutorials
// This adds Prism.js highlighting to editable code textareas
(function() {
    if (typeof Prism === 'undefined') {
        return;
    }

    function setupTextareaHighlighting(textarea) {
=======
/**
 * Prism Textarea Extension for OpenCV.js Tutorials
 * 
 * This extension adds syntax highlighting to editable textarea elements
 * by creating an overlay approach that preserves editability while displaying
 * syntax-highlighted code.
 * 
 * @author OpenCV Contributors
 * @license MIT
 */

(function() {
    'use strict';

    if (typeof Prism === 'undefined') {
        console.warn('Prism is not loaded. Textarea highlighting requires Prism.js');
        return;
    }

    /**
     * Set up syntax highlighting for a single textarea element
     * @param {HTMLTextAreaElement} textarea - The textarea to enhance
     */
    function setupTextareaHighlighting(textarea) {
        // Skip if already initialized
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        if (textarea.dataset.highlighted) {
            return;
        }

<<<<<<< HEAD
=======
        // Create wrapper container
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        var wrapper = document.createElement('div');
        wrapper.className = 'prism-textarea-wrapper';
        wrapper.style.position = 'relative';
        wrapper.style.display = 'inline-block';
        wrapper.style.width = '100%';

<<<<<<< HEAD
=======
        // Create pre/code elements for syntax highlighting
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        var pre = document.createElement('pre');
        var code = document.createElement('code');
        code.className = 'language-javascript';
        pre.appendChild(code);
<<<<<<< HEAD
        
=======

        // Match textarea styling to ensure perfect overlay
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        var computedStyle = window.getComputedStyle(textarea);
        pre.style.position = 'absolute';
        pre.style.top = '0';
        pre.style.left = '0';
<<<<<<< HEAD
        pre.style.width = '100%';
        pre.style.height = '100%';
=======
        pre.style.right = '0';
        pre.style.bottom = '0';
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        pre.style.margin = '0';
        pre.style.padding = computedStyle.padding;
        pre.style.border = '1px solid transparent';
        pre.style.font = computedStyle.font;
<<<<<<< HEAD
        pre.style.fontSize = computedStyle.fontSize;
        pre.style.lineHeight = computedStyle.lineHeight;
=======
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        pre.style.whiteSpace = 'pre-wrap';
        pre.style.wordWrap = 'break-word';
        pre.style.overflow = 'hidden';
        pre.style.pointerEvents = 'none';
        pre.style.background = computedStyle.backgroundColor;
<<<<<<< HEAD
        pre.style.boxSizing = 'border-box';
        
        textarea.style.background = 'transparent';
        textarea.style.position = 'relative';
        textarea.style.zIndex = '2';
        textarea.style.color = 'rgba(0,0,0,0.01)';
        textarea.style.caretColor = '#000';
        textarea.style.MozCaretColor = '#000';
        textarea.style.webkitTextFillColor = 'rgba(0,0,0,0.01)';
        textarea.style.textShadow = '0 0 0 transparent';
        textarea.style.cursor = 'text';
        textarea.style.boxSizing = 'border-box';

=======

        // Make textarea text invisible while keeping cursor visible
        textarea.style.background = 'transparent';
        textarea.style.position = 'relative';
        textarea.style.zIndex = '2';
        textarea.style.color = 'rgba(0,0,0,0.01)'; // Nearly invisible
        textarea.style.caretColor = '#000'; // Black cursor
        textarea.style.MozCaretColor = '#000'; // Firefox
        textarea.style.webkitTextFillColor = 'rgba(0,0,0,0.01)'; // WebKit
        textarea.style.textShadow = '0 0 0 transparent';
        textarea.style.cursor = 'text';

        // Insert wrapper into DOM
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        textarea.parentNode.insertBefore(wrapper, textarea);
        wrapper.appendChild(pre);
        wrapper.appendChild(textarea);

<<<<<<< HEAD
        function update() {
            code.textContent = textarea.value;
            Prism.highlightElement(code);
=======
        /**
         * Update the syntax highlighting
         */
        function update() {
            code.textContent = textarea.value;
            Prism.highlightElement(code);
            // Sync scroll position
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
            pre.scrollTop = textarea.scrollTop;
            pre.scrollLeft = textarea.scrollLeft;
        }

<<<<<<< HEAD
        update();

        textarea.addEventListener('input', update);
=======
        // Initial highlight
        update();

        // Update on input
        textarea.addEventListener('input', update);

        // Sync scrolling
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
        textarea.addEventListener('scroll', function() {
            pre.scrollTop = textarea.scrollTop;
            pre.scrollLeft = textarea.scrollLeft;
        });

<<<<<<< HEAD
        textarea.dataset.highlighted = 'true';
    }

=======
        // Mark as initialized
        textarea.dataset.highlighted = 'true';
    }

    /**
     * Initialize all textareas with class 'code'
     */
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
    function init() {
        var textareas = document.querySelectorAll('textarea.code');
        for (var i = 0; i < textareas.length; i++) {
            setupTextareaHighlighting(textareas[i]);
        }
    }

<<<<<<< HEAD
=======
    // Auto-initialize on page load
>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
<<<<<<< HEAD
=======

    // Expose for manual initialization if needed
    if (typeof Prism !== 'undefined') {
        Prism.highlightTextareas = init;
    }

>>>>>>> 58723a23cb (doc: Fix Copilot review issues for Prism.js integration)
})();
