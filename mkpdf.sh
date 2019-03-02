cat \
ch00_cover.asciidoc \
ch01_introduction.asciidoc \
ch02_installation.asciidoc \
ch03_python.asciidoc \
ch04_database.asciidoc \
ch05_rdkit.asciidoc \
ch06_similarity.asciidoc \
ch07_graph.asciidoc \
ch08_visualization.asciidoc \
ch09_qsar.asciidoc \
ch10_deeplearning.asciidoc \
ch11_dlqsar.asciidoc \
ch12_generativemodels.asciidoc > py4c.asciidoc
asciidoctor-pdf -r asciidoctor-pdf-cjk -o pdf/py4chemoinformatics.pdf py4c.asciidoc
