"""
Напиши функцію get_product_id(), яка:

Приймає рядок, що являє собою URL-адресу сторінки товару в Інтернет-магазині.
Повертає ідентифікатор товару з рядка.
Усі URL-адреси відформатовані однаково:

Спочатку є домен exampleshop.com.
Потім назва товару, розділена тире (-).
Потім буква p, що вказує на початок ідентифікатора товару.
Потім фактичний ідентифікатор (без обмеження довжини).
Потім 8-значне представлення дати, коли товар було додано.
І, нарешті, .html.
"""

def get_product_id(url: str) -> str:
    url_parts = url.split("-")
    return url_parts[-2]


if __name__ == "__main__":
    print(get_product_id("exampleshop.com/fancy-coffee-cup-p-90764-12052019.html") == "90764")
    print(get_product_id("exampleshop.com/dry-water-just-add-water-to-get-water-p-147-24122017.html") == "147")
    print(get_product_id("exampleshop.com/public-toilet-proximity-radar-p-942312798-01012020.html") == "942312798")

