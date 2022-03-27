# polarcape-test

потребна верзија на python: 3.10


потребни инсталации во терминал:
    -pip install django<br />
    -pip install django-debug-toolbar<br />
    -pip install drf-nested-routers<br />
    -pip install psycopg2<br />
    -pip install djangorestframework<br />
    -pip install django-filter<br />
    -pip install drf-writable-nested<br />
    -pip install django-routers

1. Направете датабаза со име store_app во postgres.

2. Променете ја лозинката во config/settings за датабазата пред да го стартувате проектот.

3. Направете миграции со командата py manage.py migrate.

4. Стартнете го проектот со py manage.py runserver.

5. Проектот е готов за користење со празна датабаза. Следно можете да ги користите еднпоинтите подолу. Пример модели се достапни во examples.txt

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
