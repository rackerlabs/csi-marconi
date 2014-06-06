import os
import sys
import pyrax
import pyrax.exceptions as exc

pyrax.auth_with_token(sys.argv[2], tenant_name=sys.argv[1])

with open(os.path.expanduser("~/.tsung/existingqueue.csv")) as names:
    for name in names:
        try:
            queue = pyrax.queues.create(name.rstrip())
        except exc.DuplicateQueue:
            pass
