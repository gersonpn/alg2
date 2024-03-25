info = [
    {
        "empresa": "ABC Corp",
        "cargo": "Analista de Dados",
        "salario": 5000.00,
        "beneficios": ["Plano de saúde", "Vale-refeição"],
        "requisitos": ("Formação em Ciência da Computação", "Experiência com Python"),
        "disponivel": True
    },
    {
        "empresa": "XYZ Ltda",
        "cargo": "Gerente de Vendas",
        "salario": 8000.00,
        "beneficios": ["Plano de saúde", "Vale-alimentação"],
        "requisitos": ("Experiência em vendas", "Habilidades de liderança"),
        "disponivel": False
    },
    {
        "empresa": "123 Inc",
        "cargo": "Designer Gráfico",
        "salario": 4000.00,
        "beneficios": ["Plano odontológico", "Vale-transporte"],
        "requisitos": ("Formação em Design", "Conhecimento de ferramentas Adobe"),
        "disponivel": True
    }
]

for i in info:
    print(i["cargo"], i["salario"], i["disponivel"])




