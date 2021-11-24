import os

def eval(pl, command, format='%s', highlight_groups=['powerline_shell']):
    p = os.popen(command)
    result = p.read().strip()

    if p.close():
        return None

    return [
        {
            'contents': format % result,
            'highlight_groups': highlight_groups
        }
    ]
