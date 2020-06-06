from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
import requests
from bs4 import BeautifulSoup

from places.models import Place, PlaceImage


def fetch_json_urls(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    links_to_json = soup.select('tbody a')
    links_to_json_raw = [f"https://raw.githubusercontent.com/{link['href'].replace('/blob', '')}" for link in links_to_json if '.json' in link['href']]
    return links_to_json_raw


def create_object(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    response_json = response.json()
    new_place = Place.objects.get_or_create(
        title=response_json['title'],
        description_short=response_json['description_short'],
        text=response_json['description_long'],
        coordinates_lat=response_json['coordinates']['lat'],
        coordinates_lng=response_json['coordinates']['lng'],
    )
    add_imgs(new_place[0], response_json['imgs'])


def add_imgs(new_place, img_urls):
    for index, img_url in enumerate(img_urls, 1):
        response = requests.get(img_url)
        new_placeimg = PlaceImage.objects.create(place=new_place)
        new_img = ContentFile(response.content)
        new_placeimg.image.save(f'image{index}.jpg', new_img, save=True)


class Command(BaseCommand):
    help = 'Insert link to dir in repo with jsons pls'

    def add_arguments(self, parser):
        parser.add_argument(
            'dir_url',
            nargs='+',
            type=str
        )

    def handle(self, *args, **options):
        url = options['dir_url'][0]
        urls_to_jsons = fetch_json_urls(url)
        for url_to_json in urls_to_jsons:
            create_object(url_to_json)
        self.stdout.write(self.style.SUCCESS('I think its all done!'))
