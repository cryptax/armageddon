import logging
import subprocess
import io

logger = logging.getLogger('default')


def execute_command(command):
    proc = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    debug = True
    if debug is True:
        my_stdout = io.open(proc.stdout.fileno(), mode='r', encoding="utf-8")
        for l in my_stdout:
            print(l)
        my_stderr = io.open(proc.stderr.fileno(), mode='r', encoding="utf-8")
        for l in my_stderr:
        #for l in io.TextIOWrapper(my_stderr, encoding='utf-8'):
            print(l)
    else:
        proc.communicate()
