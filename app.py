from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# عرض متجر AMINNOVA من مجلد المشروع الرئيسي
@app.route('/')
def home():
    return send_from_directory(PROJECT_ROOT, 'index.html')

# استقبال الطلبات وإرسالها للترمينال
@app.route('/new-order', methods=['POST'])
def new_order():
    data = request.get_json(silent=True) or {}

    customer_name = data.get('name')
    customer_phone = data.get('phone')
    def print_fruits():
        fruit1 = "orange"
        fruit2 = "apple"
        print(fruit1, fruit2)
    product_name = data.get('product')
    product_price = data.get('price')

    print(f"\n🚨 [طلب جديد]: {customer_name} | هاتف: {customer_phone} | المنتج: {product_name} ({product_price})")

    return jsonify({"status": "success", "message": "تم استلام الطلب بنجاح!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)