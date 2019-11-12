import re


NUMBERS = list(map(str, range(0, 10)))


# The same filter is in the `vmware_vm_provisioning` role.
# If changing here, change it there as well.
def get_matching(data, path):
    """Search for matching field in a data structure using a path.

    Args:
        data (dict): Data structure.
        path (string): String describing the path to the matching field.
            The format of the string must be in dotted notation
            (e.g. networks.0.mac). Full path must exist in the `data`. The path
            can contain an extra notation in the following format:
                `{key[(==|=~)value]
            allowing to check for the existence of a key in a list of dicts and
            optionally compare the key value via string comparison or regexp.

    Return:
        dict: Matching field or `None`.
    """

    done = False

    for item in list(path.split('.')):
        if item[0] in NUMBERS:
            item = int(item)

        if isinstance(item, int):
            if isinstance(data, list) and len(data) > item:
                data = data[item]
            else:
                done = True
                break
        else:
            if item.startswith('{') and item.endswith('}'):
                if isinstance(data, list):
                    # Check if any item of the list contains dict with
                    # the key
                    tmp_list = []
                    expr = item[1:-1]

                    if '==' in expr:
                        expr_type = 'compare'
                        k, v = expr.split('==', 1)
                    elif '=~' in expr:
                        expr_type = 'regexp'
                        k, v = expr.split('=~', 1)
                    else:
                        expr_type = None
                        k = expr

                    for i in data:
                        if (
                                isinstance(i, dict) and ((
                                    expr_type == 'compare' and
                                    k in i and
                                    i[k] == v
                                ) or (
                                    expr_type == 'regexp' and
                                    k in i and
                                    re.search(v, i[k])
                                ) or (
                                    expr in i
                                ))):
                            tmp_list.append(i)

                    data = tmp_list
                else:
                    done = True
                    break
            elif item in data:
                data = data[item]
            else:
                done = True
                break

    if done:
        return
    else:
        return data


class FilterModule(object):
    """Custom Jinja2 filters"""

    def filters(self):
        return {
            'get_matching': get_matching,
        }
