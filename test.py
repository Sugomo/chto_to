from requests import get, post

'''
print(get('http://localhost:5000/api/news').json())

print(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе
'''
print(post('http://localhost:5000/api/news').json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())