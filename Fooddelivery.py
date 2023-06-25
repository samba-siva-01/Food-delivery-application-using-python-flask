from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for restaurants and menu items
restaurants = [
    {
        'id': 1,
        'name': 'Restaurant A',
        'menu': [
            {'id': 1, 'name': 'Item 1', 'price': 10},
            {'id': 2, 'name': 'Item 2', 'price': 15},
            {'id': 3, 'name': 'Item 3', 'price': 8}
        ]
    },
    {
        'id': 2,
        'name': 'Restaurant B',
        'menu': [
            {'id': 4, 'name': 'Item 4', 'price': 12},
            {'id': 5, 'name': 'Item 5', 'price': 9},
            {'id': 6, 'name': 'Item 6', 'price': 14}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)

@app.route('/menu/<int:restaurant_id>')
def menu(restaurant_id):
    restaurant = None
    for r in restaurants:
        if r['id'] == restaurant_id:
            restaurant = r
            break
    if not restaurant:
        return 'Restaurant not found'
    return render_template('menu.html', restaurant=restaurant)

@app.route('/order', methods=['POST'])
def order():
    # Process the order
    order_details = request.form.getlist('item')
    total_price = 0
    for item_id in order_details:
        for restaurant in restaurants:
            for item in restaurant['menu']:
                if item['id'] == int(item_id):
                    total_price += item['price']
                    break

    return f'Order placed successfully! Total price: ${total_price}'

if __name__ == '__main__':
    app.run(debug=True)
