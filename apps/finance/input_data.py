currency_instances = {'COP': 'Pesos Colombianos', 'USD': 'US Dollar'}

account_type_instaces = {
    'Cuenta corriente': {
        'description': 'Esta cuenta se utiliza generalmente para administrar los ingresos y gastos diarios de una empresa o persona. Se puede acceder fácilmente a los fondos, lo que la hace ideal para transacciones frecuentes.',
        'icon': 'bi bi-wallet2',
    },
    'Tarjeta de crédito': {
        'description': 'Una tarjeta de crédito es una forma de financiamiento que permite a los usuarios realizar compras y pagarlas más tarde. Los usuarios pueden pagar el saldo en su totalidad cada mes o pueden optar por pagar un monto mínimo y pagar intereses sobre el saldo restante.',
        'icon': 'bi bi-credit-card',
    },
    'Activo': {
        'description': 'Un activo es un recurso que posee una empresa o persona, como bienes raíces, inversiones o inventario. Los activos pueden ser tangibles o intangibles y se utilizan para generar ingresos.',
        'icon': 'bi bi-bar-chart-line',
    },
    'Pasivo': {
        'description': 'Un pasivo es una obligación financiera que tiene una empresa o persona, como préstamos, facturas pendientes o deudas. Los pasivos son una responsabilidad financiera y pueden afectar la capacidad de una empresa o persona para obtener financiamiento adicional o cumplir con sus obligaciones financieras existentes.',
        'icon': 'bi bi-bank',
    },
}

expense_categories = [
    {
        'name': 'Transporte',
        'description': 'Gastos relacionados con el transporte',
        'icon': 'bi bi-car',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Formación',
        'description': 'Gastos relacionados con la educación y la formación',
        'icon': 'bi bi-mortarboard',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Hogar',
        'description': 'Gastos relacionados con el hogar y la decoración',
        'icon': 'bi bi-house',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Servicios públicos',
        'description': 'Gastos relacionados con los servicios públicos como agua, luz, gas, etc.',
        'icon': 'bi bi-lightbulb',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Alimentos',
        'description': 'Gastos relacionados con la compra de alimentos',
        'icon': 'bi bi-basket',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Suscripciones',
        'description': 'Gastos relacionados con suscripciones a servicios y productos',
        'icon': 'bi bi-journal-bookmark',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Vestimenta',
        'description': 'Gastos relacionados con la ropa y la vestimenta',
        'icon': 'bi bi-shirt',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Impuestos',
        'description': 'Gastos relacionados con impuestos y tributos',
        'icon': 'bi bi-receipt',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Salud',
        'description': 'Gastos relacionados con la salud y los cuidados médicos',
        'icon': 'bi bi-heart-pulse',
        'type': 'EX',
        'is_global': True,
    },
    {
        'name': 'Entretenimiento',
        'description': 'Gastos relacionados con el entretenimiento y los pasatiempos',
        'icon': 'bi bi-controller',
        'type': 'EX',
        'is_global': True,
    },
]

income_categories = [
    {
        'name': 'Salario',
        'description': 'Ingresos provenientes de salario o nómina',
        'icon': 'bi bi-cash-stack',
        'type': 'IN',
        'is_global': True,
    },
    {
        'name': 'Inversiones',
        'description': 'Ingresos provenientes de inversiones',
        'icon': 'bi bi-graph-up',
        'type': 'IN',
        'is_global': True,
    },
    {
        'name': 'Regalos',
        'description': 'Ingresos provenientes de regalos recibidos',
        'icon': 'bi bi-gift',
        'type': 'IN',
        'is_global': True,
    },
    {
        'name': 'Venta',
        'description': 'Ingresos por venta de objetos personales o propiedades',
        'icon': 'bi bi-tag',
        'type': 'IN',
        'is_global': True,
    },
]

both_categories = [
    {
        'name': 'Ajuste',
        'description': 'Ajustes de cuentas',
        'icon': 'bi bi-sliders',
        'type': 'BO',
        'is_global': True,
    },
]

all_transaction_categories = expense_categories + income_categories + both_categories
