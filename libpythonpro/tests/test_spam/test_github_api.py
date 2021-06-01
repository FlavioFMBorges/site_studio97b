from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()  # assumiu os valores para responder offline
    resp_mock.json_return_value = {
        'login': 'renzo', 'id': 402714,
        'avatar_url': 'https://avatars.githubusercontent.com/u/402714?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
