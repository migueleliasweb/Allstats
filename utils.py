def dict_keys_to_lower(x):
    if isinstance(x, list):
        return [dict_keys_to_lower(v) for v in x]
    elif isinstance(x, dict):
        return dict((k.lower(), dict_keys_to_lower(v)) for k, v in x.items())
    else:
        return x