import os
import pyrax
import pyrax.exceptions as exc

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.credentials.conf")
pyrax.set_credential_file(creds_file)

with open("existingqueue.csv") as names:
    for name in names:
        try:
            queue = pyrax.queues.create(name)
        except exc.DuplicateQueue:
            pass
