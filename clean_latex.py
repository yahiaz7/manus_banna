import re
import unicodedata

def clean_latex_source(input_filepath, output_filepath):
    """Reads a LaTeX file, attempts to fix common encoding/character issues, and writes to a new file."""
    try:
        # Read with utf-8 encoding, replacing errors initially to avoid read failures
        with open(input_filepath, 'r', encoding='utf-8', errors='replace') as infile:
            content = infile.read()

        # Replace specific Unicode characters often causing issues, ensuring they are in math mode if needed
        replacements = {
            # Common math symbols that might be outside math mode or using Unicode directly
            '°': r'$^\circ$',  # Degree symbol
            '×': r'\times',    # Multiplication sign (ensure in math mode later if needed)
            '→': r'$\rightarrow$', # Right arrow
            '≤': r'$\leq$',     # Less than or equal to
            '≥': r'$\geq$',     # Greater than or equal to
            '≈': r'$\approx$',  # Approximately equal to
            '−': '-',          # Ensure EN dash or similar is replaced by hyphen
            '–': '--',         # EN dash to LaTeX EN dash
            '—': '---',        # EM dash to LaTeX EM dash
            # Greek letters (ensure they end up in math mode)
            'η': r'$\eta$',
            'Δ': r'$\Delta$',
            'δ': r'$\delta$',
            'β': r'$\beta$',
            'θ': r'$\theta$',
            'γ': r'$\gamma$',
            'ρ': r'$\rho$',
            'π': r'$\pi$',
            'μ': r'$\mu$',
            'ν': r'$\nu$',
            'Σ': r'$\Sigma$',
            # Smart quotes
            '“': '``',
            '”': "''",
            '‘': '`',
            '’': "'",
            # Other potentially problematic symbols (like the replacement character itself)
            '': '', # Remove Unicode replacement character if it appeared
        }

        for unicode_char, latex_equiv in replacements.items():
            content = content.replace(unicode_char, latex_equiv)

        # Ensure standard LaTeX document structure
        if not content.strip().endswith('\end{document}'):
            if '\end{document}' in content:
                 # If \end{document} exists but isn't at the end, truncate after it
                 content = content.split('\end{document}')[0] + '\end{document}'
            else:
                # If it's missing entirely, add it
                content += '\n\end{document}'

        # Add necessary packages to preamble if missing (check first few lines)
        # Ensure proper escaping for backslashes in Python strings
        preamble = content.split('\begin{document}', 1)[0]
        if r'\usepackage[utf8]{inputenc}' not in preamble:
            content = content.replace(r'\documentclass', r'\documentclass\n\usepackage[utf8]{inputenc}', 1)
        if r'\usepackage[T1]{fontenc}' not in preamble:
            content = content.replace(r'\documentclass', r'\documentclass\n\usepackage[T1]{fontenc}', 1)
        if r'\usepackage{amsmath}' not in preamble:
             content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{amsmath}', 1)
        if r'\usepackage{amssymb}' not in preamble:
             content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{amssymb}', 1)
        if r'\usepackage{graphicx}' not in preamble:
             content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{graphicx}', 1)
        if r'\usepackage{longtable}' not in preamble:
             content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{longtable}', 1)
        if r'\usepackage{hyperref}' not in preamble:
             content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{hyperref}', 1)

        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"LaTeX source cleaned and saved to {output_filepath}")

    except Exception as e:
        print(f"Error cleaning LaTeX source: {e}")

# Define file paths
input_tex = '/home/ubuntu/report.tex'
output_tex = '/home/ubuntu/report_cleaned.tex'

# Run the cleaning function
clean_latex_source(input_tex, output_tex)

