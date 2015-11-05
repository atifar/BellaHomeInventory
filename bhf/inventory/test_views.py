__author__ = 'Ati'

import pytest

from .factories import CategoryFactory, ImageFactory


# ################# Test authentication requirement #################

def test_homepage_anonymous_user(client):
    """
    Loading the homepage before authenticating should redirect to the login
    page.
    :param client:
    :return:
    """
    response = client.get('/', follow=True)

    # The redirect chain should contain only HTTP redirect status codes
    for redir in response.redirect_chain:
        assert redir[-1] == 301 or redir[-1] == 302

    # Finally loaded login page
    assert response.status_code == 200


def test_homepage_authenticated_user(admin_client):
    """
    Loading the homepage following authenticating should return the home
    page.
    :param client:
    :return:
    """
    response = admin_client.get('/')

    assert response.status_code == 200

    # The context from the list_products() view should include a 'product_list'
    assert 'product_list' in response.context


def test_homepage_after_logging_out(client, admin_user):
    """
    Loading the homepage following logging out from an authenticated session
    should redirect to the login page.
    :param client:
    :param admin_user:
    :return:
    """
    # Log in using an admin account
    client.login(username=admin_user.username, password='password')

    # Home page should load now
    response = client.get('/')
    assert response.status_code == 200

    # Log out of the authenticated
    client.logout()

    # Requesting the home page should redirect to login page
    response = client.get('/')
    assert response.status_code == 302 or response.status_code == 301


# ################# Test list_categories() #################
# Accessing all views requires an authenticated user. Therefore, test client
# simulates an authenticated session using the test admin user.

pytestmark = pytest.mark.django_db


@pytest.fixture(scope="module")
def images(request):
    """
    This fixture generates Image model instances for the same set of colors
    that the ImageFactory iterator uses (see factories.py).
    :return:
    """
    colors = ['tan', 'blue', 'green', 'gray', 'red', 'black', 'aqua', 'beige',
              'coral', 'indigo', 'lime', 'plum', 'olive', 'peru', 'teal',
              'orange']
    images = {}

    for color in colors:
        images[color] = ImageFactory()


    @request.addfinalizer
    def fin(images_dict=images):
        print("Deleting generated structures.")
        del images_dict
    return images


def test_list_no_category(admin_client):
    """
    If no category exists, list_categories() should return a zero-length list.
    :param admin_client:
    :return:
    """
    response = admin_client.get('/inventory/category/')
    assert len(response.context['category_list']) == 0


def test_list_one_category(images, admin_client):
    """
    With a single category in the database, list_categories() should return
    this category in the context.
    :param images:
    :param admin_client:
    :return:
    """
    CategoryFactory(
        image=(images['blue'], images['gray']))

    response = admin_client.get('/inventory/category/')

    assert len(response.context['category_list']) == 1
    assert response.context['category_list'][0].name.startswith('Quilts #')


def test_list_three_categories(images, admin_client):
    """
    With three categories in the database, list_categories() should return
    them in the context.
    :param images:
    :param admin_client:
    :return:
    """
    number_of_categories = 3
    CategoryFactory(image=(images['blue'], images['gray']))
    CategoryFactory(image=(images['tan'], images['green'], images['blue']))
    CategoryFactory(image=(images['red'], images['tan'], images['blue']))

    response = admin_client.get('/inventory/category/')

    assert len(response.context['category_list']) == number_of_categories
    for category in response.context['category_list']:
        assert category.name.startswith('Quilts #')





