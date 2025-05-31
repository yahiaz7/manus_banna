import re

def repair_latex_tables(input_filepath, output_filepath):
    """Reads a cleaned LaTeX file, simplifies tables, removes unsupported commands, and writes to a new file."""
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Remove hypertarget commands
        content = re.sub(r'\\hypertarget{[^}]*}{%\n', '', content)
        content = re.sub(r'\\label{[^}]*}\n', '', content) # Also remove associated labels if they cause issues

        # Simplify longtable environments
        # Replace longtable preamble with basic tabular preamble (adjust column spec if needed)
        # This is a basic replacement, might need refinement based on specific table structures
        content = re.sub(r'\\begin{longtable}\[\]{@{}\{(.*?)@{}\}', r'\begin{tabular}{\1}', content)
        content = content.replace('\begin{longtable}', '\begin{tabular}') # Catch cases without specific preamble
        content = content.replace('\end{longtable}', '\end{tabular}')

        # Remove unsupported table rules and headers
        content = content.replace('\toprule', '\hline') # Replace with basic hline
        content = content.replace('\midrule', '\hline') # Replace with basic hline
        content = content.replace('\bottomrule', '\hline') # Replace with basic hline
        content = re.sub(r'\\endhead\n', '', content) # Remove endhead command

        # Remove minipage environments within tabular environments as they often cause issues with &
        # This is aggressive and might break layout, but aims to fix the '&' error
        # A more sophisticated approach would parse the table structure
        content = re.sub(r'\\begin{minipage}\[t\]{[^}]*}\raggedright(.*?)\\strut\n\\end{minipage}', r'\1', content, flags=re.DOTALL)

        # Ensure basic document structure remains
        if '\documentclass' not in content:
            # Add a basic document class if missing (unlikely but safe check)
            content = '\documentclass{article}\n' + content
        if '\begin{document}' not in content:
            # Add begin document if missing
            content = content.split('\documentclass{article}')[0] + '\documentclass{article}\n\begin{document}\n' + content.split('\documentclass{article}')[1]
        if not content.strip().endswith('\end{document}'):
             if '\end{document}' in content:
                 content = content.split('\end{document}')[0] + '\end{document}'
             else:
                 content += '\n\end{document}'

        # Add booktabs package if using its commands (though we replaced them)
        # preamble = content.split('\begin{document}', 1)[0]
        # if r'\usepackage{booktabs}' not in preamble:
        #     content = content.replace(r'\documentclass', r'\documentclass\n\usepackage{booktabs}', 1)

        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"LaTeX tables repaired and saved to {output_filepath}")

    except Exception as e:
        print(f"Error repairing LaTeX tables: {e}")

# Define file paths
input_tex = '/home/ubuntu/report_cleaned.tex'
output_tex = '/home/ubuntu/report_cleaned_v2.tex'

# Run the repair function
repair_latex_tables(input_tex, output_tex)

