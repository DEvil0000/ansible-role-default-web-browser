import pytest


def test_mimeapps_file_permissions(host):
    config = host.file('/etc/xdg/ansible-default-web-browser/mimeapps.list')

    assert config.exists
    assert config.is_file
    assert config.user == 'root'
    assert config.group == 'root'
    assert oct(config.mode) == '0o644'


@pytest.mark.parametrize('expected', [
    'text/html=google-chrome.desktop',
    'x-scheme-handler/http=google-chrome.desktop',
    'x-scheme-handler/https=google-chrome.desktop',
    'x-scheme-handler/about=google-chrome.desktop',
    'x-scheme-handler/unknown=google-chrome.desktop'
])
def test_mimeapps_file(host, expected):
    config = host.file('/etc/xdg/ansible-default-web-browser/mimeapps.list')

    assert config.exists
    assert config.is_file
    assert config.contains(expected)
