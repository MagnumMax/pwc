import re

file_path = 'index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Replacements
replacements = [
    (r'PwC Advisor AI', 'Advisor AI'),
    (r'text-pwc-orange', 'text-brand-orange'),
    (r'bg-pwc-orange', 'bg-brand-orange'),
    (r'border-pwc-orange', 'border-brand-orange'),
    (r'ring-pwc-orange', 'ring-brand-orange'),
    (r'hover:text-pwc-orange', 'hover:text-brand-orange'),
    (r'hover:border-pwc-orange', 'hover:border-brand-orange'),
    (r'focus:border-pwc-orange', 'focus:border-brand-orange'),
    (r'focus:ring-pwc-orange', 'focus:ring-brand-orange'),
    (r'pwc: \{', 'brand: {'),
    (r'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/PwC_2025_Logo.svg/500px-PwC_2025_Logo.svg.png', 'https://placehold.co/120x40?text=LOGO'),
    (r'alt="PwC Logo"', 'alt="Logo"'),
    (r'alt="PwC"', 'alt="Logo"'),
    (r'Official PwC global', 'Official global'),
    (r'PwC has assembled', 'We have assembled'),
    (r'PwC is pleased', 'We are pleased'),
    (r'PwC global', 'Global'),
    (r'john.doe@pwc.com', 'john.doe@example.com'),
    (r'PricewaterhouseCoopers Limited', 'Consulting Firm Limited'),
    (r'Internal Distribution Only.', 'Internal Distribution Only.'), # No change needed but checking context
    (r'PwC', 'The Firm'), # Generic fallback for remaining PwC, might be risky
]

# Apply specific replacements first
for old, new in replacements[:-1]:
    content = re.sub(old, new, content)

# Handle "PwC" specifically to avoid breaking things not covered (though I covered most classes)
# We need to be careful not to replace it if it's part of a word that wasn't covered, but "pwc" is mostly used in classes or text.
# The class names like 'pwc-orange' are already replaced by 'brand-orange'.
# So remaining 'PwC' or 'pwc' are likely text content or variable names if any.
# Let's check for remaining 'PwC' in text.
content = re.sub(r'\bPwC\b', 'The Firm', content)

# Fix the tailwind config color object if needed
# The previous replacement  ->  should handle the key.
# But let's make sure we didn't miss  in other places.

# Re-read to check for any missed "pwc" (case insensitive)
# content = re.sub(r'(?i)pwc', 'firm', content) # This is too aggressive.

with open(file_path, 'w') as f:
    f.write(content)

print("Replacements complete.")
