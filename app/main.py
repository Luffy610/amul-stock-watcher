from app.stock_checker import check_product_availability
from app.send_email import send_email_notification
import os

BASE_URL = "https://shop.amul.com/en/product/"
PRODUCTS_LIST = [
    "amul-kool-protein-milkshake-or-kesar-180-ml-or-pack-of-8",
    "amul-high-protein-buttermilk-200-ml-or-pack-of-30",
    "amul-high-protein-milk-250-ml-or-pack-of-8",
    "amul-high-protein-rose-lassi-200-ml-or-pack-of-30",
    "amul-chocolate-whey-protein-34-g-or-pack-of-30-sachets",
    "amul-high-protein-paneer-400-g-or-pack-of-2"
]
PINCODE = "411036"

def main():
    try:
        success_email_recipient = os.getenv('EMAIL_RECIPIENT')
        failure_email_recipient = os.getenv('FAILURE_RECIPIENT', 'dhruvkotwani@outlook.com')
        if not success_email_recipient:
            raise ValueError("Email recipient environment variables are not set.")
        available_products = check_product_availability(BASE_URL, PRODUCTS_LIST, PINCODE)
        if available_products:
            subject = "Product Availability Alert"
            body = "The following products are available:\n" + "\n".join(available_products)
            send_email_notification(subject, body, success_email_recipient)
        else:
            print("No products are currently available.")
    except Exception as e:
        print(f"An error occurred: {e}")
        send_email_notification("Stock Checker Error", str(e), failure_email_recipient)


if __name__ == "__main__":
    main()