"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

import json


fn = 'sandpit.txt'

with open(fn, 'r') as infile:
    snippet = infile.readlines()

with open('snippet.json', 'w') as outfile:
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
    pass