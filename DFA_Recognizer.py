from IPython.display import display, HTML


# Output formatting
def bold_word_with_colour(word, code, i):
    css_colors = [
        ('teal', '#008080'),
        ('navy', '#000080'),
        ('olive', '#808000'),
        ('blue', '#0000FF'),
        ('green', '#00FF00'),
        ('magenta', '#FF00FF'),
        ('bright_black', '#666666'),
        ('yellow', '#FFFF00'),
        ('red', '#FF0000'),
        ('orange', '#FFA500'),
        ('purple', '#800080'),
        ('pink', '#FFC0CB'),
        ('brown', '#A52A2A'),
        ('gold', '#FFD700'),
        ('maroon', '#800000'),
    ]

    font_size = 0
    font_large = 24
    font_normal = 18
    font_bold = ""

    color_code = ""
    if i == -1:
        if code == "title":
            colour_code = 'black'
            font_size = font_large
            font_bold = "font-weight:bold;"
        elif code == "success":
            color_code = 'green'
            font_size = font_normal
            font_bold = "font-weight:bold;"
        elif code == "error":
            color_code = 'red'
            font_size = font_normal
            font_bold = "font-weight:bold;"
        elif code == "normal_bold":
            color_code = 'black'
            font_size = font_normal
            font_bold = "font-weight:bold;"
        else:
            color_code = 'black'
            font_size = font_normal
    else:
        if code == "result":
            color_code = css_colors[i][1]
            font_size = font_normal
            font_bold = "font-weight:bold;"

    html_text = f'<span style="font-size:{font_size}px; {font_bold} color:{color_code};">{word}</span>'
    return html_text


def display_HTML(text):
    return display(HTML(text))


class State:
    def __init__(self, is_final=False):
        self.transitions = {}
        self.is_final = is_final

    def add_transition(self, char, state):
        self.transitions[char] = state


class DFA:
    def __init__(self, patterns):
        self.start_state = State()
        self.build_dfa(patterns)

    def build_dfa(self, patterns):
        # Create the DFA structure based on the patterns input
        for pattern in patterns:
            current_state = self.start_state
            for char in pattern:
                if char not in current_state.transitions:
                    current_state.transitions[char] = State()
                current_state = current_state.transitions[char]
            current_state.transitions['$'] = State()
            current_state = current_state.transitions['$']
            current_state.is_final = True

    def search(self, text, patterns):
        # Search each pattern throughout the sample text
        matches = {pattern: [] for pattern in patterns}
        for idx in range(len(text)):
            current_state = self.start_state
            for j, char in enumerate(text[idx:]):
                if char in current_state.transitions:
                    current_state = current_state.transitions[char]

                    # End of string checking
                    if '$' in current_state.transitions:
                        check_state = current_state.transitions['$']
                        if check_state.is_final and not text[idx + j + 1].isalnum():
                            pattern = text[idx:idx + j + 1]
                            matches[pattern].append((idx, idx + j + 1))
                else:
                    break
        return matches

    # DFA building class structure
    def visualize_matches(self, text, matches, patterns_dict):
        result = text
        sorted_matches = sorted(
            ((pattern, start, end) for pattern, positions in matches.items() for start, end in positions),
            key=lambda x: x[1],
            reverse=True
        )
        for pattern, start, end in sorted_matches:
            formatted_pattern = bold_word_with_colour(pattern, "result", patterns_dict[pattern])
            result = result[:start] + formatted_pattern + result[end:]

        return result


# Function to write and format output
def show_DFA_output(text, dfa, matches, patterns_dict):
    result_str = ""

    result_str += bold_word_with_colour("Text used for demo:", "title", -1) + "<br>"
    result_str += text.replace("\n", "<br>") + "<br><br>"

    result_str += bold_word_with_colour("Results:", "title", -1) + "<br>"

    total_occurrences = sum(len(v) for v in matches.values())
    if total_occurrences > 0:

        for pattern, positions in matches.items():
            result_str += bold_word_with_colour("Pattern:", "normal_bold", -1) + " " + bold_word_with_colour(pattern,
                                                                                                             "",
                                                                                                             -1) + "<br>"
            if len(positions) == 0:
                result_str += bold_word_with_colour("Status:", "", -1) + " " + bold_word_with_colour("Reject", "error",
                                                                                                     -1) + "<br>"
                result_str += bold_word_with_colour("Found:", "", -1) + " " + ":" + " " + bold_word_with_colour(
                    str(len(positions)), "normal_bold", -1) + "<br>"
            else:
                result_str += bold_word_with_colour("Status:", "", -1) + " " + bold_word_with_colour("Accept",
                                                                                                     "success",
                                                                                                     -1) + "<br>"
                result_str += bold_word_with_colour("Found:", "", -1) + " " + ":" + " " + bold_word_with_colour(
                    str(len(positions)), "normal_bold", -1) + "<br>"
                result_str += bold_word_with_colour("Positions:", "normal_bold", -1) + "<br>"
                for start, end in positions:
                    result_str += bold_word_with_colour(f"({start}, {end})", "", -1) + "<br>"
            result_str += "<br>"

        result_str += bold_word_with_colour("Total occurrences:", "", -1) + " " + bold_word_with_colour(
            total_occurrences, "normal_bold", -1) + "<br><br>"

        result_str += bold_word_with_colour("Visualization of patterns in the text:", "title", -1) + "<br>"
        result_str += dfa.visualize_matches(text, matches, patterns_dict) + "<br>"

    else:
        result_str += bold_word_with_colour("All patterns are not found in the given text.", "", -1)

    return result_str


# The core function between front end and the DFA Recognizer, accept text (sample text) and patterns (patterns to be
# searched) from user Return output to front end
def process_text(text, patterns):
    patterns_dict = {patterns[i]: i for i in range(len(patterns))}
    dfa = DFA(patterns)
    matches = dfa.search(text, patterns)
    results = show_DFA_output(text, dfa, matches, patterns_dict)
    return results

# def main():
#     #============================ Sample Text ===================================#
#
#     # Upload text file
#     uploaded = files.upload()
#     file_name = next(iter(uploaded))
#
#     with open(file_name, 'r') as file:
#         text = file.read()
#
#     # # Demo text from a user input
#     # text = str(input())
#
#     #============================ Patterns to Search ============================#
#
#     # Demo patterns to search from an initialized list of words
#     patterns = ["Jason", "Mr. Lim", "Dr Tan", "Chee Meng", "Ahmad"]  # max 10
#
#     # # Demo patterns to search from a user input
#     # patterns = str(input("Enter a list of patterns to search (max 10, separated with comma): ")).split(",")
#
#     patterns_dict = {patterns[i]: i for i in range(len(patterns))}
#
#     clear_output(wait=True)
#
#     #============================ DFA Building ==================================#
#
#     # Build the DFA using the defined patterns
#     dfa = DFA(patterns)
#
#     # Search for patterns
#     matches = dfa.search(text, patterns)
#
#     #============================ Show DFA Search Results =======================#
#
#     show_DFA_output(text, dfa, matches, patterns_dict)
