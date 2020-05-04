from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
print(Task)