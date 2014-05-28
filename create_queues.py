from __future__ import print_function

import os
import pyrax
import pyrax.exceptions as exc

pyrax.set_environment('rackspace_cloud')
pyrax.set_default_region('hkg')
creds_file = os.path.expanduser("~/.credentials.conf")
pyrax.set_credential_file(creds_file)

with open(os.path.expanduser("~/.tsung/existingqueue.csv")) as names:
    for name in names:
        try:
            queue = pyrax.queues.create(name.rstrip())
        except exc.DuplicateQueue:
            pass
