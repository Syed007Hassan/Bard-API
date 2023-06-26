
import google.generativeai as palm

palm.configure(api_key='AIzaSyCiEx4VJELwnAjCmGfgZ4ovTKz50pIRJWQ')

models = [m for m in palm.list_models(
) if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)


data = [
    {
        "itemCode": "014d1cd8-fe11-4841-a13c-5ac72e2e4765",
        "itemName": "Gear Assembly",
        "itemDesc": "Gear Assembly",
        "type": None,
        "isTaxable": None,
        "taxRate": None,
        "taxVendorID": None,
        "costPrice": 10000.0,
        "sellingPrice": 30000.0,
        "rackNo": "",
        "rackSection": "",
        "reorderQty": None,
        "qty": None,
        "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
        "serviceId": "bee5d15c-81d1-4d17-a53f-8bfb19f6a2ee",
        "services": [
            {
                "serviceId": "bee5d15c-81d1-4d17-a53f-8bfb19f6a2ee",
                "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
                "serviceName": "Non-Inv",
                "serviceCategory": None
            }
        ],
        "serviceCategory": [
            {
                "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
                "categoryName": "Parts",
                "services": None
            }
        ],
        "dontUpdQty": True,
        "salesTaxId": "",
        "incomeAccountId": "",
        "cogsAccountId": "",
        "assetAccountId": "",
        "companyId": None,
        "company": []
    },
    {
        "itemCode": "01a62358-a6d4-425e-bdbe-3ebe0e74d6a3",
        "itemName": "Spark Plug ",
        "itemDesc": "Spark Plug ",
        "type": None,
        "isTaxable": None,
        "taxRate": None,
        "taxVendorID": None,
        "costPrice": 1450.0,
        "sellingPrice": 2000.0,
        "rackNo": "",
        "rackSection": "",
        "reorderQty": None,
        "qty": None,
        "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
        "serviceId": "bee5d15c-81d1-4d17-a53f-8bfb19f6a2ee",
        "services": [
            {
                "serviceId": "bee5d15c-81d1-4d17-a53f-8bfb19f6a2ee",
                "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
                "serviceName": "Non-Inv",
                "serviceCategory": None
            }
        ],
        "serviceCategory": [
            {
                "serviceCatId": "783038e1-7176-44f4-8272-bd9d242a9e43",
                "categoryName": "Parts",
                "services": None
            }
        ],
        "dontUpdQty": True,
        "salesTaxId": "",
        "incomeAccountId": "",
        "cogsAccountId": "",
        "assetAccountId": "",
        "companyId": None,
        "company": []
    }
]

model = models[0].name
# print(model)


prompt = "from the data list provided above, generate a list of items with their respective Selling prices."

completion = palm.generate_text(
    model=model,
    prompt=str(data) + prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=1000,
)

print(completion.result)
