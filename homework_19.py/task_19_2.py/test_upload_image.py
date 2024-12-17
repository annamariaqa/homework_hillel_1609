import requests
import pytest
import json

from app_ctrl import AppCtrl

app_ctrl = AppCtrl()


@pytest.mark.app
@pytest.mark.parametrize('url, files', [('http://127.0.0.1:8080/upload', 'post_image.jpg')])
def test_post_image(url, files):
    with open('post_image.jpg', 'rb') as files:
        files = {'image': files}
        response = app_ctrl.image_upload(params={'url': url}, files=files)
        assert response.status_code == 201, f'Expected status code 200, but actual is {response.status_code}'
        