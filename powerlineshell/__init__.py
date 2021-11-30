import os

def eval(pl, command, format='%s', highlight_groups=['powerline_shell'], divider_highlight_group='background:divider'):
    p = os.popen(command)
    result = p.read().strip()

    if p.close() or len(result) == 0:
        return None

    return [
        {
            'contents': format % result,
            'highlight_groups': highlight_groups,
            'divider_highlight_group': divider_highlight_group
        }
    ]
