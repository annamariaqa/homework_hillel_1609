import pytest

from app_ctrl import AppCtrl

app_ctrl = AppCtrl()

@pytest.mark.app
@pytest.mark.parametrize('filename', ['post_image.jpg'])
def test_delete_image(filename):
    response = app_ctrl.image_delete(filename=filename)
    
    assert response.status_code == 200, f'Expected status code 200, but actual is {response.status_code}'
    
    