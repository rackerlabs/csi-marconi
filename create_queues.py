from __future__ import print_function

import os
import sys
import pyrax
import pyrax.exceptions as exc

pyrax.set_environment('rackspace_cloud')
pyrax.set_default_region(sys.argv[1])
pyrax.auth_with_token(sys.argv[3], tenant_name=sys.argv[2])

with open(os.path.expanduser("~/.tsung/existingqueue.csv")) as names:
    for name in names:
        try:
            queue = pyrax.queues.create(name.rstrip())
        except exc.DuplicateQueue:
            pass
