import unittest

from services import (Component,
                      TYPE_ARTEFACT,
                      TYPE_SERVICE,
                      REVISION_CURRENT,
                      REVISION_NEXT)
from services.services import (get_next_artefacts,
                               get_running_services)


class ServicesTests(unittest.TestCase):

    def test_get_running_services_should_return_services_with_state_up(self):
        services = {
            'foo': 'down',
            'bar': 'up'
        }
        self.assertSetEqual(get_running_services(services), set(['bar']))

    def test_get_running_services_should_not_return_services_when_all_are_down(self):
        services = {
            'foo': 'down',
            'bar': 'down'
        }
        self.assertSetEqual(get_running_services(services), set([]))


class ArtefactsTests(unittest.TestCase):

    def test_get_next_artefacts_should_return_artefacts_with_revision_next(self):
        components = {}
        components['artefact://tomcat/current'] = Component(TYPE_ARTEFACT, REVISION_CURRENT)
        components['service://berweb42/httpd'] = Component(TYPE_SERVICE)
        # TODO add assertions and tests
