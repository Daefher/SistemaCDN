from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

#automated
# new / blank db
from proyectos.models import proyecto
User = get_user_model
class proyectosPostAPITestCase(APITestCase):
    def setUp(self):
        user        = User.objects.create(username = 'testuser', email="test@test.com")
        user.set_password("blabla")
        user.save()
        # proyecto    =
