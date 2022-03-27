# polarcape-test

1. Направете датабаза со име store_app во postgres.

2. Променете ја лозинката во settings за датабазата пред да го стартувате проектот

3. Направете миграции.

4. 

5. Достапни ендпоинти:
    -GET store/customers (прикажување на сите customers)
    -POST store/customers (додавање customers)

    -GET store/customers/int (прикажување на еден customer)
    -DELETE store/customers/int (бришење на еден customer)
    -PUT store/customers/int (update на еден customer)

    -GET store/products (прикажување на сите продукти, со можност за филтрирање според цена, според категорија, според големина и можност за сите заедно.)
        http://127.0.0.1:8000/store/products/?category=T&ordering=price&size=M / пример за филтер 
    -POST store/products (додавање на продукт)

    -GET store/products/int (прикажување на еден продукт)
    -DELETE store/products/int (бришење на еден продукт)
    -PUT store/products/int (update на еден продукт)

    -POST store/addProductToCustomer/ (додавање на продукт на одреден customer - параметри се праќаат во body )
    
    -DELETE store/deleteProductFromCustomer/int (бришење на одреден продукт од одреден customer - дополнителни параметри се праќаат во body)

6. Во examples.txt се достапни модели/примери за секој ендпоинт
