from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
import requests
from bs4 import BeautifulSoup

from places.models import Place, PlaceImage


def fetch_json_urls(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    grid_selector = '.js-navigation-item a'
    links_to_json = soup.select(grid_selector)
    return [f"https://raw.githubusercontent.com/{link['href'].replace('/blob', '')}" for link in links_to_json][4:]


def create_place(url):
    response = requests.get(url)
    response.raise_for_status()
    json_response = response.json()
    new_place = Place.objects.get_or_create(
        title=json_response['title'],
        short_description=json_response['description_short'],
        long_description=json_response['description_long'],
        latitude=json_response['coordinates']['lat'],
        longitude=json_response['coordinates']['lng'],
    )
    new_place_object = new_place[0]
    add_images(new_place_object, json_response['imgs'])


def add_images(new_place, img_urls):
    for index, img_url in enumerate(img_urls, 1):
        response = requests.get(img_url)
        new_placeimg = PlaceImage.objects.create(place=new_place)
        new_img = ContentFile(response.content)
        new_placeimg.image.save(f'image{index}.jpg', new_img, save=True)


class Command(BaseCommand):
    help = 'Download places from GH and save them into BD, boi'

    def add_arguments(self, parser):
        parser.add_argument('download_url', nargs='+', type=str)

    def handle(self, *args, **options):
        download_url = options['download_url'][0]
        urls_to_jsons = fetch_json_urls(download_url)
        for url_to_json in urls_to_jsons:
            create_place(url_to_json)
