# polarcape-test

1. Направете датабаза со име store_app во postgres.

2. Променете ја лозинката во settings за датабазата пред да го стартувате проектот

3. Направете миграции.

4. 

5. Достапни ендпоинти:
    -GET store/customers (прикажување на сите customers)<br />
    -POST store/customers (додавање customers)<br />

    -GET store/customers/int (прикажување на еден customer)<br />
    -DELETE store/customers/int (бришење на еден customer)<br />
    -PUT store/customers/int (update на еден customer)<br />

    -GET store/products (прикажување на сите продукти, со можност за филтрирање според цена, според категорија, според големина и можност за сите заедно.)<br />
        http://127.0.0.1:8000/store/products/?category=T&ordering=price&size=M / пример за филтер<br /> 
    -POST store/products (додавање на продукт)

    -GET store/products/int (прикажување на еден продукт)<br />
    -DELETE store/products/int (бришење на еден продукт)<br />
    -PUT store/products/int (update на еден продукт)<br />

    -POST store/addProductToCustomer/ (додавање на продукт на одреден customer - параметри се праќаат во body )
    
    -DELETE store/deleteProductFromCustomer/int (бришење на одреден продукт од одреден customer - дополнителни параметри се праќаат во body)

6. Во examples.txt се достапни модели/примери за секој ендпоинт
