from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker import HierarchicalChunker

conv_res = DocumentConverter().convert("https://arxiv.org/pdf/2206.01062")
doc = conv_res.document
chunks = list(HierarchicalChunker().chunk(doc))

print(chunks[10])
