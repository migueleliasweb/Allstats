import platform
from multiprocessing import cpu_count
import json

# Linux distro
# Kernel Version
# CPU
# MEMORY
# HD
# Network


def host_stats():
    return {
        'linux': ''.join(platform.linux_distribution()),
        'kernel': platform.uname()[2],
        'cpu': {
            'cpu_count': cpu_count(),
            'model_name': cpu_model_name()
        },
        'memory': ram_stats()
    }


def ram_stats():
    _meminfo=dict()

    with open('/proc/meminfo') as f:
        for line in f:
            _meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return _meminfo


def cpu_model_name():
    with open('/proc/cpuinfo') as f:
        for line in f:
            # Ignore the blank line separating the information between
            # details about two processing units
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    return model_name