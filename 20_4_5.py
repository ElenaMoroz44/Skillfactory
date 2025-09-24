import json
from collections import Counter
from collections import defaultdict


with open("translator.json", "r") as my_file:
    translator = json.load(my_file)

max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in translator.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

max_quantity = 0
max_order = ''
for order_num, orders_data in translator.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'Номер заказа с самым большим количеством: {max_order}, количество: {max_quantity}')

dates = [order["date"] for order in translator.values()]
date_counts = Counter(dates)
max_count = max(date_counts.values())
most_orders_dates = [date for date, count in date_counts.items() if count == max_count]
print(f'Больше всего заказов было сделано: {most_orders_dates}')

user_counts = Counter(v["user_id"] for v in translator.values())
max_order = max(user_counts.values())
top_users = [user for user, count in user_counts.items() if count == max_order]
print(f'Больше всего заказов сделал пользователь: {top_users}, количество: {max_order}')

user_sums = defaultdict(int)

for order in translator.values():
    user_sums[order["user_id"]] += order["price"] * order["quantity"]
richest_user = max(user_sums.values())
top_order_users = [user for user, count in user_sums.items() if count == richest_user]
print(f'Самая большая суммарная стоимость заказов у пользователя: {top_order_users}, сумма: {richest_user}')

order_totals = [v["price"] * v["quantity"] for v in translator.values()]
#Под «стоимость заказа» подразумеваем цена × количество для каждого заказа
avg_order_price = sum(order_totals) / len(order_totals)
print("Средняя стоимость заказа в июле:", avg_order_price)

total_price = sum(order_totals)
#Подразумеваем «средняя цена за одну штуку товара»
total_qty = sum(v["quantity"] for v in translator.values())
avg_item_price = total_price / total_qty
print("Средняя стоимость товара в июле:", avg_item_price)
