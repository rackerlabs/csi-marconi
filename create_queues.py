from __future__ import print_function

import os
import pyrax
import pyrax.exceptions as exc

pyrax.set_environment('rackspace_cloud')
pyrax.set_default_region('hkg')
pyrax.auth_with_token(my_token, tenant_name="0728829")

with open(os.path.expanduser("~/.tsung/existingqueue.csv")) as names:
    for name in names:
        try:
            queue = pyrax.queues.create(name.rstrip())
        except exc.DuplicateQueue:
            pass
