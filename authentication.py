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
]

for user in users:
    if user['authenticated'] == True:
        print(f"{user['name']} is authenticated")
    else:
        print(f"{user['name']} is not authenticated")
