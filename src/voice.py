import subprocess

class Voice():

    def __init__(self):
        pass

    def say(self, text):
        cmd = [
            'say',
            '-v',
            'Karen',
            '--rate=35',
            text,
        ]
        p = subprocess.Popen(cmd)
        p.wait()
