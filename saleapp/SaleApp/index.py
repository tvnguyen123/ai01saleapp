from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    products = [
        {
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        },
        {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        },
        {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAM: 6GB",
            "price": 24000000,
            "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
            "category_id": 1
        }
    ]

    # Lọc sản phẩm theo từ khóa
    kw = request.args.get("kw", "").strip()
    if kw:
        products = [
            p for p in products
            if kw.lower() in p["name"].lower()
        ]

    # Lọc sản phẩm theo danh mục
    cate_id = request.args.get("category_id")
    if cate_id:
        try:
            cate_id = int(cate_id)
            products = [
                p for p in products
                if p["category_id"] == cate_id
            ]
        except ValueError:
            products = []

    return render_template("saleapp.html", product=products)


if __name__ == "__main__":
    app.run(debug=True)