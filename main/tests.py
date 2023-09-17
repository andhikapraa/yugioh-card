from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from .models import Item

# Create your tests here.
class MainTestCase(TestCase):
    def test_index(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Yu-Gi-Oh! Card Collection")
        self.assertContains(response, "Muhammad Andhika Prasetya")
        self.assertContains(response, "2206031302")
        self.assertContains(response, "PBP C")
        
class ItemTestCase(TestCase):
    def test_item(self):
        item = Item.objects.create(
            name="Blue-Eyes White Dragon",
            amount=3,
            description="This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.",
            card_type="Monster",
            passcode=89631139,
            attribute="LIGHT",
            types="Dragon/Normal",
            level=8,
            atk=3000,
            deff=2500,
            effect_type="Normal",
            card_property="Normal",
            rulings="This card is treated as a 'Blue-Eyes' monster.",
            image=SimpleUploadedFile(
                name='BlueEyesWhiteDragon.webp',
                content=open('static/images/BlueEyesWhiteDragon.webp', 'rb').read(),
                content_type='image/webp'
            ),
        )
        self.assertEqual(item.name, "Blue-Eyes White Dragon")
        self.assertEqual(item.amount, 3)
        self.assertEqual(item.description, "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.")
        self.assertEqual(item.card_type, "Monster")
        self.assertEqual(item.passcode, 89631139)
        self.assertEqual(item.attribute, "LIGHT")
        self.assertEqual(item.types, "Dragon/Normal")
        self.assertEqual(item.level, 8)
        self.assertEqual(item.atk, 3000)
        self.assertEqual(item.deff, 2500)
        self.assertEqual(item.effect_type, "Normal")
        self.assertEqual(item.card_property, "Normal")
        self.assertEqual(item.rulings, "This card is treated as a 'Blue-Eyes' monster.")
        self.assertEqual(item.image.name, "images/BlueEyesWhiteDragon.webp")
        item.image.delete() # delete image after test to avoid cluttering the media folder