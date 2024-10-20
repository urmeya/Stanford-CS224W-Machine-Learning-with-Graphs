import os
from glob import glob
from pdf2image import convert_from_path
from pathlib import Path

def check_dir_path(dirpath):
    if not Path(dirpath).exists():
        Path(dirpath).mkdir(parents=True)

all_lects = glob("CS224W_slides/*")
lect_titles = ['1. Introduction; Machine Learning for Graphs',
 '2. Traditional Methods for ML on Graphs',
 '3. Node Embeddings',
 '4. Link Analysis: PageRank',
 '5. Label Propagation for Node Classification',
 '6. Graph Neural Networks 1: GNN Model',
 '7. Graph Neural Networks 2: Design Space',
 '8. Applications of Graph Neural Networks',
 '9. Theory of Graph Neural Networks',
 '10. Knowledge Graph Embeddings',
 '11. Reasoning over Knowledge Graphs',
 '12. Frequent Subgraph Mining with GNNs',
 '13. Community Structure in Networks',
 '14. Traditional Generative Models for Graphs',
 '15. Deep Generative Models for Graphs',
 '16. Advanced Topics on GNNs',
 '17. Scaling Up GNNs',
 '19. GNNs for Science',
 'Bonus Guest Lecture: Industrial Applications of GNNs',
 '18. Guest Lecture: GNNs for Computational Biology'
 ]

with open("lects_main.md", "w") as fw:
    for idx, (lect_name, lect_pdf) in enumerate(zip(lect_titles, all_lects)):
        check_dir_path("lect_slides")
        fw.write(f"[{lect_name}](lect_slides/lect_{idx}.md)\n")
        images = convert_from_path(lect_pdf)
        check_dir_path(f"lect_slides/lect_{idx}")
        with open(f"lect_slides/lect_{idx}.md", "w") as fw2:
            for i in range(len(images)):
                slidepath = f"lect_slides/lect_{idx}/"+'page'+ str(i) +'.jpg'
                rel_slidepath = f"lect_{idx}/"+'page'+ str(i) +'.jpg'
                images[i].save(slidepath, 'JPEG')
                fw2.write(f'<img src={rel_slidepath}></br>\n')