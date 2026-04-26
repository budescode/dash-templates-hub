import pandas as pd

def loadDataSet(df_name):
    if df_name == "customers":
        return pd.read_csv('data/raw/customers.csv')
    elif df_name == "products":
        return pd.read_csv('data/raw/products.csv')
    elif df_name == 'orders':
        return pd.read_csv('data/raw/orders.csv')
    elif df_name == 'geo_location':
        return pd.read_csv('data/raw/geolocation.csv')
    elif df_name == "sellers":
        return pd.read_csv('data/raw/sellers.csv')
    elif df_name == 'order_reviews':
        return pd.read_csv('data/raw/order_reviews.csv')
    elif df_name == 'order_payments':
        return pd.read_csv('data/raw/order_payments.csv') 

    order_items_df = pd.read_csv('data/raw/order_items.csv')
    
    
    
    
    
    product_category_name_translation_df = pd.read_csv('data/raw/product_category_name_translation.csv')
    return None
    # return {
    #     "customers": customer_df,
    #     "geolocation": geolocation_df,
    #     "order_items": order_items_df,
    #     "order_payments": order_payments_df,
    #     "order_reviews": order_reviews_df,
    #     "orders": orders_df,
    #     "products": products_df,
    #     "sellers": sellers_df,
    #     "product_category_name_translation": product_category_name_translation_df
    # }