import subprocess

ANALYZER_BINARY = "/usr/bin/external-analyzer"

def run_analysis(args):
    result = subprocess.run([ANALYZER_BINARY] + args, capture_output=True)
    return result.returncode, result.stdout.decode()
