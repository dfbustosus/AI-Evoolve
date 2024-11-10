from docling.document_converter import DocumentConverter

converter = DocumentConverter()

source = "https://arxiv.org/pdf/2410.23335"

result = converter.convert(source)

# Convert Document into JSON
import json

result_dict = result.document.export_to_dict()

print(json.dumps(result_dict, indent=2))
