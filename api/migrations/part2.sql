ALTER TABLE orders
    ADD COLUMN customer_id INT NULL,
    ADD COLUMN promotion_id INT NULL,
    ADD INDEX ix_orders_customer_id (customer_id),
    ADD INDEX ix_orders_promotion_id (promotion_id),
    ADD CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers (id),
    ADD CONSTRAINT fk_orders_promotion FOREIGN KEY (promotion_id) REFERENCES promotions (id);
