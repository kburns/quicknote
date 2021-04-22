#!/usr/bin/env python3

import jinja2
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", metavar='filename', type=str, help="Name of the file.")
    parser.add_argument("-d", "--doctype", dest='doctype', help="Type of note.", default="default")
    parser.add_argument("-t", "--title", dest='title', help="Title of note.", default='(filename)')
    args = parser.parse_args()

    latex_jinja_env = jinja2.Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = False,
        autoescape = False,
        loader = jinja2.PackageLoader('quicknote', 'templates'))

    filename = args.filename
    doctype = args.doctype
    title = args.title
    if title == '(filename)':
        title = filename
    if not filename.endswith('.tex'):
        filename += '.tex'
    if not doctype.endswith('.tex'):
        doctype += '.tex'

    template = latex_jinja_env.get_template(doctype)
    out_text = template.render(title=title)
    with open(filename, 'w') as outfile:
        outfile.write(out_text)
