from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    phone_number = Column(String)
    role = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    

class Address(Base):
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("category.id"))
    brand_id = Column(Integer, ForeignKey("brand.id"))
    rating = Column(Float)
    created_at = Column(String)
    updated_at = Column(String)
    

class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    
class Brand(Base):
    __tablename__ = "brand"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    
class ProductImages(Base):
    __tablename__ = "product_images"
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))
    
class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))
    
class Cart(Base):
    __tablename__ = "cart"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(String)
    updated_at = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    

    class CartItem(Base):
        __tablename__ = "cart_items"
        
        id = Column(Integer, primary_key=True, index=True)
        cart_id = Column(Integer, ForeignKey("cart.id"))
        product_id = Column(Integer, ForeignKey("product.id"))
        quantity = Column(Integer)
        created_at = Column(String)
        updated_at = Column(String)
        

    class Order(Base):
        __tablename__ = "orders"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        order_status = Column(String)  # pending, shipped, delivered, cancelled
        total_price = Column(Float)
        payment_status = Column(String)  # pending, paid, failed
        shipping_address_id = Column(Integer, ForeignKey("address.id"))
        created_at = Column(String)
        updated_at = Column(String)
        

    class OrderItem(Base):
        __tablename__ = "order_items"
        
        id = Column(Integer, primary_key=True, index=True)
        order_id = Column(Integer, ForeignKey("orders.id"))
        product_id = Column(Integer, ForeignKey("product.id"))
        quantity = Column(Integer)
        price_at_purchase = Column(Float)
        created_at = Column(String)


    class Payment(Base):
        __tablename__ = "payments"
        
        id = Column(Integer, primary_key=True, index=True)
        order_id = Column(Integer, ForeignKey("orders.id"))
        user_id = Column(Integer, ForeignKey("user.id"))
        payment_method = Column(String)  # credit_card, paypal, stripe, etc.
        payment_status = Column(String)  # pending, completed, failed
        transaction_id = Column(String)
        created_at = Column(String)
        updated_at = Column(String)


    class Review(Base):
        __tablename__ = "reviews"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        product_id = Column(Integer, ForeignKey("product.id"))
        rating = Column(Integer)  # 1 to 5 stars
        comment = Column(String)
        created_at = Column(String)
        updated_at = Column(String)


    class Shipping(Base):
        __tablename__ = "shipping"
        
        id = Column(Integer, primary_key=True, index=True)
        order_id = Column(Integer, ForeignKey("orders.id"))
        tracking_number = Column(String)
        carrier = Column(String)  # e.g., FedEx, DHL, UPS
        estimated_delivery_date = Column(String)
        status = Column(String)  # in transit, delivered, delayed
        created_at = Column(String)
        updated_at = Column(String)


    class Coupon(Base):
        __tablename__ = "coupons"
        
        id = Column(Integer, primary_key=True, index=True)
        code = Column(String, unique=True)
        discount_type = Column(String)  # percentage, fixed
        discount_value = Column(Float)
        min_order_value = Column(Float)
        expires_at = Column(String)
        created_at = Column(String)
        updated_at = Column(String)


    class AppliedCoupon(Base):
        __tablename__ = "applied_coupons"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        order_id = Column(Integer, ForeignKey("orders.id"))
        coupon_id = Column(Integer, ForeignKey("coupons.id"))
        created_at = Column(String)


    class Wishlist(Base):
        __tablename__ = "wishlists"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        product_id = Column(Integer, ForeignKey("product.id"))
        created_at = Column(String)


    class Notification(Base):
        __tablename__ = "notifications"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        message = Column(String)
        is_read = Column(Boolean, default=False)
        created_at = Column(String)


    class Admin(Base):
        __tablename__ = "admins"
        
        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(Integer, ForeignKey("user.id"))
        role = Column(String)  # superadmin, moderator
        created_at = Column(String)
        updated_at = Column(String)