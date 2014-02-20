from __future__ import absolute_import

from services import (Component,
                      REVISION_CURRENT,
                      REVISION_NEXT,
                      TYPE_ARTEFACT,
                      TYPE_SERVICE)


def get_running_services(services):
    """Returns set of services with state 'up'.

    - `services` - dict from service name to state
    """
    return set()


def get_next_artefacts(components):
    """Returns set of artefacts with REVISION_NEXT.

    - `components` - dict from name to Component.
    """
    return set()
