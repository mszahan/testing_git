users = [
    {
        'name': 'sojib',
        'username': 'sojib-ali',
        'authenticated': True
     },
    {
        'name': 'sarwar',
        'username': 'mszahan',
        'authenticated': True
     },
    {
        'name': 'Tonmoy',
        'username': 'tonmoy3270',
        'authenticated': False
     },
    {
        'name': 'Josephine Langford Ali',
        'username': 'jlali',
        'authenticated': True
     },
]

for user in users:
    if user['authenticated']:
        print(f"{user['name']} is authenticated")
    else:
        print(f"{user['name']} is not authenticated")
