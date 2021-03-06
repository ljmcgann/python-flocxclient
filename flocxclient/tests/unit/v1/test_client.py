import mock

from flocxclient.common import http
from flocxclient.tests.unit import utils
from flocxclient.v1 import client


@mock.patch.object(http, '_construct_http_client', autospec=True)
class ClientTest(utils.BaseTestCase):

    def test_client_user_api_version(self, http_client_mock):
        os_flocx_api_version = '1.15'
        session = mock.Mock()

        client.Client(session=session,
                      os_flocx_api_version=os_flocx_api_version)

        http_client_mock.assert_called_once_with(
            session=session,
            os_flocx_api_version=os_flocx_api_version)

    def test_client_initialized_managers(self, http_client_mock):
        session = mock.Mock()
        cl = client.Client(session=session,
                           os_flocx_api_version='1')

        self.assertIsInstance(cl.offer, client.offer.OfferManager)

    def test_client_no_session(self, http_client_mock):
        self.assertRaises(TypeError, client.Client, os_flocx_api_version='1')

    def test_client_session_via_posargs(self, http_client_mock):
        session = mock.Mock()
        client.Client(session)
        http_client_mock.assert_called_once_with(
            session,
            os_flocx_api_version=client.DEFAULT_VER)

    def test_client_session_via_kwargs(self, http_client_mock):
        session = mock.Mock()
        client.Client(session=session)
        http_client_mock.assert_called_once_with(
            session,
            os_flocx_api_version=client.DEFAULT_VER)
