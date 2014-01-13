from imhotep.tools import Tool
from collections import defaultdict
import re


class JSL(Tool):
    regex = re.compile(
        r'^(?P<type>[WE]) '
        r'(?P<filename>.*?) L(?P<line_number>\d+): (?P<message>.*)$')

    def invoke(self, dirname, filenames=set()):
        retval = defaultdict(lambda: defaultdict(list))

        cmd = 'find %s -name "*.js" | xargs jsl' % dirname
        output = self.executor(cmd)
        for line in output.split('\n'):
            match = self.regex.search(line)
            if match is None:
                continue
            message = '%s: %s' % (match.group('type'), match.group('message'))
            filename = match.group('filename')[len(dirname) + 1:]
            retval[filename][match.group('line_number')].append(message)
        return retval
