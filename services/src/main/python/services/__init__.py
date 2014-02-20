TYPE_ARTEFACT = 'artefact'
TYPE_SERVICE = 'service'

REVISION_NEXT = 'next'
REVISION_CURRENT = 'current'


class Component(object):

    def __init__(self, typ, revision=None):
        self.typ = typ
        self.revision = revision
