import os

def eval(pl, command, format='%s'):
    result = os.popen(command).read().strip()

    return [
        {
            'contents': format % result,
            'highlight_groups': ['powerline_shell']
        }
    ]
