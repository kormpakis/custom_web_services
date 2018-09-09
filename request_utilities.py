from urllib.parse import urljoin

import requests


def get_wordpress_posts(base_url):
    """
    Using that function we get all the wordpress posts
    :param base_url:
    :return:
    """
    result = requests.get(base_url).json()
    return result


def get_post_image(media_id, media_url):
    """
    Returns the image url
    :param media_id: image id
    :param media_url: media url
    :return:
    """
    endpoint = urljoin(media_url, str(media_id))
    response = requests.get(endpoint)
    if response.status_code == 200:
        image_url = response.json()["guid"]["rendered"]
    else:
        image_url = ""
    return image_url


def get_wordpress_post_info(post_id, base_url, media_url):
    """
    Using that function we are able to get info about the current requested post
    :param post_id: post id
    :param base_url: base url
    :param media_url: media url
    :return: post info
    """
    endpoint = urljoin(base_url, str(post_id))
    response = requests.get(endpoint)
    if response.status_code == 200:
        result = response.json()
        title = result["title"]["rendered"]
        link = result["link"]
        featured_media = int(result["featured_media"])
        if featured_media != 0:
            image_url = get_post_image(featured_media, media_url)
        else:
            image_url = ""
        return [title, link, image_url]
    else:
        return []
