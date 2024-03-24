info = [
    {
        "país": "Senegal",
        "povo": "Serer",
        "contribuicao": "Destaque para a música, dança e tradições religiosas",
        "personagens": ["Sunjata Keita", "Aline Sitoé Diatta"],
        "eventos": ["Festival de Dakar", "Festival de Saint Louis Jazz"],
        "sítios": ["Ilha de Gorée", "Reserva de Fauna de Bandia"],
    },
    {
        "país": "Angola",
        "povo": "Bantu",
        "contribuicao": "Influência na música, dança, culinária e artes visuais",
        "personagens": ["Rainha Nzinga", "António Agostinho Neto"],
        "eventos": ["Festival Nacional da Cultura", "Festival Internacional de Música do Sumbe"],
        "sítios": ["Cidade de M'banza-Kongo", "Parque Nacional da Kissama"],
    },
    {
        "país": "Haiti",
        "povo": "Afro-haitiano",
        "contribuicao": "Cultura influente na música, dança, religião e arte",
        "personagens": ["Toussaint Louverture", "Marie Laveau"],
        "eventos": ["Carnaval", "Festival Rara"],
        "sítios": ["Citadelle Laferrière", "Museu do Panteão Nacional Haitiano"],
    }
]

eventos = []
for i in info:
    print(i["povo"])
    print(i["contribuicao"])
    print(i["eventos"])
    print(" ")
