import re

def repair_latex_lists(input_filepath, output_filepath):
    """Reads a LaTeX file, attempts to fix common list structure issues, and writes to a new file."""
    try:
        with open(input_filepath, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        repaired_lines = []
        in_list_env = False
        list_stack = [] # To handle nested lists
        item_found_in_current_level = False

        for line in lines:
            stripped_line = line.strip()

            # Detect start of list environments
            if stripped_line.startswith("\begin{itemize}") or stripped_line.startswith("\begin{enumerate}"):
                list_env_type = "itemize" if stripped_line.startswith("\begin{itemize}") else "enumerate"
                list_stack.append(list_env_type)
                in_list_env = True
                item_found_in_current_level = False # Reset for new level
                repaired_lines.append(line)
                continue

            # Detect end of list environments
            if stripped_line.startswith("\end{itemize}") or stripped_line.startswith("\end{enumerate}"):
                if list_stack:
                    list_stack.pop()
                if not list_stack:
                    in_list_env = False
                item_found_in_current_level = True # Allow end tag even if no item was found (might be empty list)
                repaired_lines.append(line)
                continue

            # Inside a list environment
            if in_list_env:
                # Check if the line contains content but doesn't start with \item or another \begin
                if stripped_line and not stripped_line.startswith("\item") and not stripped_line.startswith("\begin{") and not stripped_line.startswith("\end{"):
                    # If we haven't found an \item yet at this level, prepend it
                    # This is a heuristic and might incorrectly add \item
                    if not item_found_in_current_level:
                         # Check if the previous line ended an item or the list started
                         prev_line_strip = repaired_lines[-1].strip() if repaired_lines else ""
                         if prev_line_strip.startswith("\begin{") or prev_line_strip.startswith("\item") or prev_line_strip == "":
                              repaired_lines.append("  \item " + line.lstrip()) # Add item and indent slightly
                              item_found_in_current_level = True
                         else:
                              repaired_lines.append(line) # Assume it's part of the previous item
                    else:
                         repaired_lines.append(line) # Assume it's part of the previous item
                elif stripped_line.startswith("\item"):
                    item_found_in_current_level = True # Mark that we found an item at this level
                    repaired_lines.append(line)
                else:
                    repaired_lines.append(line) # Append other lines (like nested begin/end, or blank lines)
            else:
                repaired_lines.append(line) # Append lines outside list environments

        # Final check for unclosed environments (basic)
        if list_stack:
            print(f"Warning: Unclosed list environments detected: {list_stack}")
            # Attempt to close them at the end
            # for env_type in reversed(list_stack):
            #     repaired_lines.append(f"\end{{{env_type}}}\n")

        with open(output_filepath, "w", encoding="utf-8") as outfile:
            outfile.writelines(repaired_lines)
        print(f"LaTeX lists repaired and saved to {output_filepath}")

    except Exception as e:
        print(f"Error repairing LaTeX lists: {e}")

# Define file paths
input_tex = "/home/ubuntu/report_cleaned_v3.tex"
output_tex = "/home/ubuntu/report_cleaned_v4.tex"

# Run the repair function
repair_latex_lists(input_tex, output_tex)

