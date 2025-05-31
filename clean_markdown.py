import re
import unicodedata

def clean_markdown_for_latex(input_filepath, output_filepath):
    """Reads a markdown file, cleans it for better LaTeX compatibility, and writes to a new file."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Replace common problematic Unicode characters with ASCII or LaTeX equivalents
        replacements = {
            '°': r'$^\circ$',  # Degree symbol
            '−': '-',          # Minus sign (different from hyphen)
            '×': r'\times',    # Multiplication sign
            '→': r'$\rightarrow$', # Right arrow
            'η': r'$\eta$',      # Greek eta
            'Δ': r'$\Delta$',    # Greek Delta
            'δ': r'$\delta$',    # Greek delta
            'β': r'$\beta$',     # Greek beta
            'θ': r'$\theta$',    # Greek theta
            'γ': r'$\gamma$',    # Greek gamma
            'ρ': r'$\rho$',      # Greek rho
            'π': r'$\pi$',      # Greek pi
            'μ': r'$\mu$',      # Greek mu
            'ν': r'$\nu$',      # Greek nu
            'Σ': r'$\Sigma$',    # Greek Sigma
            '≤': r'$\leq$',     # Less than or equal to
            '≥': r'$\geq$',     # Greater than or equal to
            '≈': r'$\approx$',  # Approximately equal to
            # Add more replacements as needed
        }

        for unicode_char, latex_equiv in replacements.items():
            content = content.replace(unicode_char, latex_equiv)

        # Normalize Unicode characters to their closest ASCII representation where possible
        # This helps with subtle variations like different types of hyphens or quotes
        content = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore').decode('ascii')

        # Remove potentially problematic LaTeX commands inserted by markdown converters if necessary
        # Example: content = re.sub(r'\tightlist', '', content)

        # Ensure math environments are properly handled (basic check)
        # Pandoc usually handles this well, but sometimes inline math needs escaping
        # Example: Replace single $...$ with \(...\) if needed, though pandoc prefers $

        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"Markdown cleaned and saved to {output_filepath}")

    except Exception as e:
        print(f"Error cleaning markdown: {e}")

# Define file paths
input_md = '/home/ubuntu/combined_solutions.md'
output_md = '/home/ubuntu/combined_solutions_cleaned.md'

# Run the cleaning function
clean_markdown_for_latex(input_md, output_md)

