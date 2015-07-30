// Thanks to Leonard Pauli: http://stackoverflow.com/questions/566203/changing-css-values-with-javascript
// Usage example <div class="boxes" onmouseover="css('.boxes', 'color', 'green')">Mouseover Me!</div>
function css(selector, property, value) {
         for (var i=0; i<document.styleSheets.length;i++) {//Loop through all styles
             //Try add rule
             try { document.styleSheets[i].insertRule(selector+ ' {'+property+':'+value+'}', document.styleSheets[i].cssRules.length);
             } catch(err) {try { document.styleSheets[i].addRule(selector, property+':'+value);} catch(err) {}}//IE
         }
}
css('.animate-in', 'opacity', '0.1 !important');
css('.animate-out', 'opacity', '0.1 !important');
