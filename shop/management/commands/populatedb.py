"""
This is a custom command that populates the database scraped data

https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/

Parsed data is from the website "avtopoliv.com.ua"
Parser by Oleksandr Podynihlazov (private project)
"""

import json
import uuid
import os
import requests
from urllib.parse import urlparse
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from shop.models import Product, Category, ControlMechanism
from django.conf import settings 

class Command(BaseCommand):
    help = "Populate the database with products from scrapped data"

    def handle(self, *args, **kwargs):
        json_file_path = os.path.join(settings.BASE_DIR, 'cleaned_data.json')
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for item in data:
            category_name = None
            try:
                category_name = item.get("Section").lower()
                category_name = "Sensors" if "sensors" in category_name or "timers" in category_name else category_name
                category_name = "Drip Systems" if "drip" in category_name else category_name
                category_name = "Sprinkler Systems" if "cannons" in category_name or "guns" in category_name else category_name
                category_name = "Subsurface Systems" if "underground" in category_name else category_name
                category = Category.objects.filter(name=category_name).first()
                control_mechanism = ControlMechanism.objects.filter(name="Manual").first()

                product = Product(
                    id=uuid.uuid4(),
                    name=item["Name"],
                    brand=item["Brand"],
                    description=item["Description"],
                    category=category,
                    control_mechanism=control_mechanism,
                    price=item["Price"],
                    stock=10 if item.get("Availability") == "In stock" else 0,
                    available=True if item.get("to display") == "Yes" else False,
                )

                img_name = urlparse(item["Image"]).path.split("/")[-1]
                if item.get("Image"):
                    if not default_storage.exists(f'product/{img_name}'):
                        response = requests.get(item["Image"])
                        if response.status_code == 200:
                            img_name = urlparse(item["Image"]).path.split("/")[-1]
                            product.image.save(img_name, ContentFile(response.content), save=False)
                    else:
                        product.image = f'product/{img_name}'

                product.save()

                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error adding product {item['Name']}: {e}"))
