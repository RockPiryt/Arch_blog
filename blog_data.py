import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_data = response.json()
print(blog_data)

#     [{'id': 1, 'body': 'Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. 
# Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.', 'title': 'The Life of Cactus', 'subtitle': 'Who knew that cacti lived such interesting lives.'}, {'id': 2, 
# 'body': 'Chase ball of string e......] 
