"""Creates VS Code snippetsfrom a text file.

Uses a structures text file to generate a json file suitable for importing as a VS Code snippet.
Allows the body of the snippet to be multi line and to include double qualte without them being escaped.
Note: single quotes should not be used.

Each snippet shoule have the following form:
    snippet
    name: A shoert name for the snippet
    prefix: one or more comma separated snippet prefixes
    body: the bodyof the snippet which will be added to the code. This may include
        multi-line strings
    descritpion: a short description of the snippet.

Examples:
    for example input file see snippet.py
    for example output see snippet.json
"""
import json

def generate_snippet_json(in_filename, out_filename):
    """generates a VSCode snippet as a json file.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        in_filename (str): filename of the text input file defining the snippet.
        out_filename (str): filename of the json output file defining the snippet.

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        No errors.
    """

    with open(in_filename, 'r') as infile:
        snippet = infile.readlines()

    with open(out_filename, 'w') as outfile: # change to output filename
        outfile.write("{\n")
        for i, line in enumerate(snippet):
            if line[:6] == "name: ":
                outfile.write(f' "{line[6:].strip()}" : {{\n')

            if line[:8] == "prefix: ":
                prefix_list = (line[8:].strip().split(', '))
                prefix_str = ", ".join(prefix_list).join(['"','"'])
                outfile.write(f'  "prefix": {prefix_str},\n')

            if line[:6] == "body: ":
                body_str_list = [line[6:].strip()]
                body_lines = iter(snippet[i:],)
                body_line = next(body_lines, '')
                ctr = 0
                while body_line[:12] != 'description:':
                    ctr += 1
                    body_line = next(body_lines, '')
                body_str_list.extend([i.strip("\n") for i in snippet[i+1:i+ctr]])
                outfile.write('  "body": ')
                json.dump(body_str_list, outfile)
                outfile.write(',\n')

            if line[:12] == "description:":
                description = line[12:].strip()
                outfile.write(f'  "description": "{description}"\n }},\n')

            if '!snippet' in line:
                outfile.write('\n')

        outfile.write("}\n")

if __name__ == "__main__":
    generate_snippet_json('assets/snippets.txt', 'assets/snippets.json')