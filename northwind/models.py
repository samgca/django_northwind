from django.db import models
from django.utils.translation import ugettext as _


class Region(models.Model):
    region_id = models.PositiveSmallIntegerField(
        _('Region id'),
        db_column='RegionID',
        primary_key=True
    )
    region_description = models.CharField(
        _('Region description'),
        db_column='RegionDescription',
        max_length=50
    )

    class Meta:
        db_table = 'region'


class Territories(models.Model):
    territory_id = models.CharField(
        _('Territory id'),
        db_column='TerritoryID',
        primary_key=True,
        max_length=20
    )
    territory_description = models.CharField(
        _('Territory description'),
        db_column='TerritoryDescription',
        max_length=50
    )
    region_id = models.ForeignKey(
        Region,
        db_column='RegionID',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'territories'


class Employees(models.Model):
    employee_id = models.AutoField(
        _('Employee id'),
        db_column='EmployeeID',
        primary_key=True,
    )
    last_name = models.CharField(
        _('Last name'),
        db_column='LastName',
        max_length=20,
        db_index=True
    )
    first_name = models.CharField(
        _('First name'),
        db_column='FirstName',
        max_length=10
    )
    title = models.CharField(
        _('title'),
        db_column='Title',
        max_length=30,
        blank=True,
        null=True
    )
    title_of_courtesy = models.CharField(
        _('Title of Courtesy'),
        db_column='TitleOfCourtesy',
        max_length=25,
        blank=True,
        null=True
    )
    birth_date = models.DateTimeField(
        _('Birth date'),
        db_column='BirthDate',
        blank=True,
        null=True
    )
    hire_date = models.DateTimeField(
        _('Hire date'),
        db_column='HireDate',
        blank=True,
        null=True
    )
    address = models.CharField(
        _('address'),
        db_column='Address',
        max_length=60,
        blank=True,
        null=True
    )
    city = models.CharField(
        _('City'),
        db_column='City',
        max_length=15,
        blank=True,
        null=True
    )
    region = models.CharField(
        _('Region'),
        db_column='Region',
        max_length=15,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        _('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=True,
        db_index=True
    )
    country = models.CharField(
        _('Country'),
        db_column='Country',
        max_length=15,
        blank=True,
        null=True
    )
    home_phone = models.CharField(
        _('Home phone'),
        db_column='HomePhone',
        max_length=24,
        blank=True,
        null=True
    )
    extension = models.CharField(
        _('Extension'),
        db_column='Extension',
        max_length=4,
        blank=True,
        null=True
    )
    photo = models.BinaryField(
        _('Photo'),
        db_column='Photo',
        blank=True,
        null=True
    )
    notes = models.TextField(
        _('Notes'),
        db_column='Notes',
        blank=True,
        null=True
    )
    reports_to = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        db_column='ReportsTo',
        on_delete=models.PROTECT,
    )
    photo_path = models.CharField(
        _('Photo path'),
        db_column='PhotoPath',
        max_length=255,
        blank=True,
        null=True
    )
    territories = models.ManyToManyField(
        Territories,
        verbose_name=_('Territories'),
        db_table='EmployeeTerritories',
        blank=True,
    )

    class Meta:
        db_table = 'employees'


class Shippers(models.Model):
    shipper_id = models.AutoField(
        _('Shipper ID'),
        db_column='ShipperID',
        primary_key=True
    )
    company_name = models.CharField(
        _('Company name'),
        db_column='CompanyName',
        max_length=40
    )
    phone = models.CharField(
        _('Phone'),
        db_column='Phone',
        max_length=24,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'shippers'


class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(
        _('Customer typeID'),
        db_column='CustomerTypeID',
        primary_key=True,
        max_length=5
    )
    customer_desc = models.TextField(
        _('Customer description'),
        db_column='CustomerDesc',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'customerdemographics'


class Customers(models.Model):
    customer_id = models.CharField(
        _('Customer ID'),
        db_column='CustomerID',
        primary_key=True,
        max_length=5
    )
    company_name = models.CharField(
        _('Company name'),
        db_column='CompanyName',
        max_length=40
    )
    contact_name = models.CharField(
        _('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=True,
        null=True
    )
    contact_title = models.CharField(
        _('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=True,
        null=True
    )
    address = models.CharField(
        _('Address'),
        db_column='Address',
        max_length=60,
        blank=True,
        null=True
    )
    city = models.CharField(
        _('City'),
        db_column='City',
        max_length=15,
        blank=True,
        null=True
    )
    region = models.CharField(
        _('Region'),
        db_column='Region',
        max_length=15,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        _('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=True,
        null=True
    )
    country = models.CharField(
        _('Country'),
        db_column='Country',
        max_length=15,
        blank=True,
        null=True
    )
    phone = models.CharField(
        _('Phone'),
        db_column='Phone',
        max_length=24,
        blank=True,
        null=True
    )
    fax = models.CharField(
        _('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    customer_customer_demo = models.ManyToManyField(
        CustomerDemographics,
        verbose_name=_('Customer customer demo'),
        db_table='CustomerCustomerDemo',
        blank=True,
    )

    class Meta:
        db_table = 'customers'


class Categories(models.Model):
    category_id = models.AutoField(
        _('Category ID'),
        db_column='CategoryID',
        primary_key=True
    )
    category_name = models.CharField(
        _('Category name'),
        db_column='CategoryName',
        max_length=15,
        db_index=True
    )
    description = models.TextField(
        _('Description'),
        db_column='Description',
        blank=True,
        null=True
    )
    picture = models.BinaryField(
        _('Picture'),
        db_column='Picture',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'categories'


class Suppliers(models.Model):
    supplier_id = models.AutoField(
        _('Supplier ID'),
        db_column='SupplierID',
        primary_key=True
    )
    company_name = models.CharField(
        _('Company name'),
        db_column='CompanyName',
        max_length=40
    )
    contact_name = models.CharField(
        _('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=True,
        null=True
    )
    contact_title = models.CharField(
        _('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=True,
        null=True
    )
    address = models.CharField(
        _('Address'),
        db_column='Address',
        max_length=60,
        blank=True,
        null=True
    )
    city = models.CharField(
        _('City'),
        db_column='City',
        max_length=15,
        blank=True,
        null=True
    )
    region = models.CharField(
        _('Region'),
        db_column='Region',
        max_length=15,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        _('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=True,
        null=True
    )
    country = models.CharField(
        _('Country'),
        db_column='Country',
        max_length=15,
        blank=True,
        null=True
    )
    phone = models.CharField(
        _('Phone'),
        db_column='Phone',
        max_length=24,
        blank=True,
        null=True
    )
    fax = models.CharField(
        _('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    homepage = models.TextField(
        _('HomePage'),
        db_column='HomePage',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'suppliers'


class Products(models.Model):
    product_id = models.AutoField(
        _('Product ID'),
        db_column='ProductID',
        primary_key=True
    )
    product_name = models.CharField(
        _('Product name'),
        db_column='ProductName',
        max_length=40,
        db_index=True,
    )
    supplier_id = models.ForeignKey(
        Suppliers,
        db_column='SupplierID',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_index=True,
    )
    category_id = models.ForeignKey(
        Categories,
        db_column='CategoryID',
        db_index=True,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    quantity_per_unit = models.CharField(
        _('Quantity per Unit'),
        db_column='QuantityPerUnit',
        max_length=20,
        blank=True,
        null=True
    )
    unit_price = models.DecimalField(
        _('Unit price'),
        db_column='UnitPrice',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4
    )
    units_in_stock = models.SmallIntegerField(
        _('Units in Stock'),
        db_column='UnitsInStock',
        blank=True,
        null=True
    )
    units_on_order = models.SmallIntegerField(
        _('Units on Order'),
        db_column='UnitsOnOrder',
        blank=True,
        null=True
    )
    reorder_level = models.SmallIntegerField(
        _('Reorder level'),
        db_column='ReorderLevel',
        blank=True,
        null=True
    )
    discontinued = models.IntegerField(
        _('Discontinued'),
        db_column='Discontinued'
    )

    class Meta:
        db_table = 'products'


class Orders(models.Model):
    order_id = models.AutoField(
        _('Order ID'),
        db_column='OrderID',
        primary_key=True
    )
    customer = models.ForeignKey(
        Customers,
        blank=True,
        null=True,
        db_column='CustomerID',
        on_delete=models.CASCADE,
        db_index=True
    )
    employee = models.ForeignKey(
        Employees,
        blank=True,
        null=True,
        db_column='EmployeeID',
        on_delete=models.CASCADE,
        db_index=True
    )
    order_date = models.DateField(
        _('Order date'),
        db_column='OrderDate',
        blank=True,
        null=True,
        db_index=True
    )
    required_date = models.DateField(
        _('Required_date'),
        db_column='RequiredDate',
        blank=True,
        null=True
    )
    shipped_date = models.DateField(
        _('Shipped date'),
        db_column='ShippedDate',
        blank=True,
        null=True,
        db_index=True
    )
    ship_via = models.ForeignKey(
        Shippers,
        blank=True,
        null=True,
        db_column='ShipVia',
        on_delete=models.CASCADE,
        db_index=True
    )
    freight = models.DecimalField(
        _('Freight'),
        db_column='Freight',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4
    )
    ship_name = models.CharField(
        _('Ship name'),
        db_column='ShipName',
        max_length=40,
        blank=True,
        null=True
    )
    ship_address = models.CharField(
        _('Ship address'),
        db_column='ShipAddress',
        max_length=60,
        blank=True,
        null=True
    )
    ship_city = models.CharField(
        _('Ship city'),
        db_column='ShipCity',
        max_length=15,
        blank=True,
        null=True
    )
    ship_region = models.CharField(
        _('Ship region'),
        db_column='ShipRegion',
        max_length=15,
        blank=True,
        null=True
    )
    ship_postal_code = models.CharField(
        _('Ship postal code'),
        db_column='ShipPostalCode',
        max_length=10,
        blank=True,
        null=True,
        db_index=True
    )
    ship_country = models.CharField(
        _('Shipped country'),
        db_column='ShipCountry',
        max_length=15,
        blank=True,
        null=True
    )
    order_details = models.ManyToManyField(
        Products,
        verbose_name=_('Products'),
        blank=True,
        through='OrderDetails'
    )

    class Meta:
        db_table = 'orders'


class OrderDetails(models.Model):
    order_id = models.ForeignKey(
        Orders,
        db_column='OrderID',
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Products,
        db_column='ProductID',
        on_delete=models.CASCADE
    )
    unit_price = models.DecimalField(
        _('Unit price'),
        db_column='UnitPrice',
        max_digits=19,
        decimal_places=4
    )
    quantity = models.SmallIntegerField(
        _('Quantity'),
        db_column='Quantity'
    )
    discount = models.FloatField(
        _('Discount'),
        db_column='Discount'
    )

    class Meta:
        db_table = 'order_details'
