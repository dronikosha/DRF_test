from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Resume
from .serializers import ResumeSerializer
from .views import ResumeAPICreate, ResumeAPIList, ResumeAPIUpdate


class ResumeAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.ru', 'test')
        self.resume = Resume.objects.create(
            owner=self.user,
            title='test',
            status='test',
            salary=123,
            speciality='test',
            grade='test',
            education='test',
            experience='test',
            portfolio='test',
            phone='test',
            email='test@test.ru',
        )
        self.serializer = ResumeSerializer(instance=self.resume)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
    def test_get(self):
        data = {
            "status": "321",
            "grade" : "1233",
            "speciality": "1223",
            "salary": 1223,
            "education": "1223",
            "experience": "123",
            "portfolio" : "123",
            "title": "nikitossssss",
            "phone": "123",
            "email": "root@root.ru"
        }
        response = self.client.get('/api/v1/resumes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [self.serializer.data])
        
    def test_post(self):
        data = {
            "status": "321",
            "grade" : "1233",
            "speciality": "1223",
            "salary": 1223,
            "education": "1223",
            "experience": "123",
            "portfolio" : "123",
            "title": "nikdghjssfghitossssss",
            "phone": "123",
            "email": "root@root.ru",
            "owner": self.user.id
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/v1/resumes/create/', data=data)
        self.assertEqual(response.status_code, 201)
        
    def test_patch(self):
        data = {
            "status": "321",
            "grade" : "1233",
            "speciality": "1223",
            "salary": 1223,
            "education": "1223",
            "experience": "123",
            "portfolio" : "123",
            "title": "nikitossssss",
            "phone": "123",
            "email": "root@root.ru"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch('/api/v1/resumes/1/', data=data)
        self.assertEqual(response.status_code, 200)
