from django.test import TestCase
from .models import TreeType, Tree
# Create your tests here.
class TreeTest(TestCase):

	@classmethod
	def test_database_and_models(self):
		test_tree_type = TreeType.objects.create(
			tree_picture= r'C:\Users\Pc\Downloads\chess_pieces.bmp',
			flower_picture= r'C:\Users\Pc\Downloads\chess_pieces.bmp',
			common_name= 'Test Plant',
			latin_name= 'Aberumtus Spinula',
			max_height= 9,
			max_age= 21,
			company= 'TestCompany',)
		test_tree = Tree.objects.create(
			tree_type = test_tree_type,
			age = 5,
			height = 34, 
			in_flower = True,
			latitude = 2345.01,
			longtitude = 23431.12,
			sponsor = 'TestSponsor',
			) 