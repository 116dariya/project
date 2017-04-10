import requests 
session = requests.Session()

r = session.get('http://manga-sushi.kz/menu')

# get YII_CSRF_TOKEN
csrf = '9faba25d4f58832d22622faa2e0f88f7d0fb772d'

order = {
	'basket':{
		32768: 2,
		32885: 5
	},
	'name': 'Dariya',
	'address': 'user_address',
	'phone' : 'user_phone',
	'email' : 'user_email'

}

for item_id in order['basket']:
		amount = order['basket'][item_id]
		url = "http://manga-sushi.kz/basket/add/%d/%d" % (item_id, amount)
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36' ,
			'X-Requested-With': 'XMLHttpRequest'
		}
		form_data = {
			'use_ajax':'true',
			'client_system': 'true',
			'YII_CSRF_TOKEN': csrf
		}
		r = session.post(url, data = form_data, headers = headers)
		response = r.json()



form_data = {
	'use_ajax':'true',
	'client_system': 'true',
	'YII_CSRF_TOKEN': csrf,
	'OrderForm[delivery_type]': 'Курьер',
	'OrderForm[restraunt]': 167,
	'OrderForm[city]': 30,
	'OrderForm[name]': order['name'],
	'OrderForm[address]': order['address'],
	'OrderForm[phone]': order['phone'],
	'OrderForm[email]': order['email'],
	'OrderForm[prefered_time]':'',
	'OrderForm[sum]': '',
	'OrderForm[comments]': 'Не забудьте жевачку!',
	'OrderForm[save_data]': 0

}
print(form_data)