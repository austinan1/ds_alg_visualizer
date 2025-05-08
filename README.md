# ds_alg_visualizer
data structure and algorithm visualizer

todo 
- arrays
- queues
- stacked
- linked list
- hash table
- tree
- graph


target data structure:
ds_visualizer/
├── main.py                         # Entry point
├── config/
│   └── settings.py                 # Colors, fonts, screen size
├── core/
│   ├── visualizer.py               # Main rendering/loop manager
│   ├── ui.py                       # Buttons, sliders, user input
│   └── events.py                   # Key/mouse event handling
├── algorithms/
│   ├── __init__.py
│   ├── sorting/
│   │   ├── bubble_sort.py
│   │   ├── quick_sort.py
│   │   └── ...
│   ├── trees/
│   │   ├── bst.py
│   │   └── avl.py
│   └── graph/
│       ├── bfs.py
│       └── dijkstra.py
├── assets/
│   ├── fonts/
│   ├── icons/
│   └── images/
├── utils/
│   ├── drawing.py                  # Arrows, labels, node rendering
│   └── timer.py                    # Frame timing or delays
├── styles/
│   └── themes.py                   # Color schemes or light/dark mode
├── requirements.txt
└── README.md