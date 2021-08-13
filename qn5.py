import pandas as pd

orders = pd.read_csv('data/orders.csv')
order_reviews = pd.read_csv('data/order_reviews.csv')
order_items = pd.read_csv('data/order_items.csv')
order_payments = pd.read_csv('data/order_payments.csv')
sellers = pd.read_csv('data/sellers.csv')
product_translation = pd.read_csv('data/product_category_name_translation.csv')
products = pd.read_csv('data/products.csv')

# List the top 10 sellers with the highest review score.
merged_first = (order_items.merge(
    order_reviews, on="order_id")
    .groupby("seller_id").mean()
    .sort_values(by="review_score", ascending=False))
print(merged_first['review_score'].head(10))


# Calculate the top 10 product categories with the highest sales and show their english name.
merged_second = (order_items.merge(
    products, on="product_id")
    .merge(product_translation, on="product_category_name")
    .groupby("product_category_name_english")
    .count()
    .sort_values(by="price", ascending=False))
print(merged_second['price'].head(10))

# Count the daily average revenue by the top 10 sellers with the highest total revenue.
merged_third = (order_items.merge(
    order_payments, on="order_id")
    .groupby("seller_id")
    .sum()
    .sort_values(by="payment_value", ascending=False))
orders['order_approved_at'] = orders['order_approved_at'].astype(
    'datetime64[ns]')
duration = (orders.order_approved_at.max() -
            orders.order_approved_at.min()).days
print(merged_third.head(10).payment_value/duration)

# Count the monthly revenue in each seller state.
merged_fourth = (merged_third.merge(
    sellers, on="seller_id")
    .groupby(by="seller_state")
    .sum()
    .sort_values(by="payment_value", ascending=False))
print(merged_fourth.payment_value/(round(duration/30)))


# If you are a seller, what kind of products you will sell? Where are you going to open your store? And why?
# i will sell furnitures and in Sao Paulo. From Part 2, we can deduce that the most frequently sold items come from the Bed Bath Tables category, wheras in Part 4 we can conclude people Sao Paulo tend to spend the most on purchases.
