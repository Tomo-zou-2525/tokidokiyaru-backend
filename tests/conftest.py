import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, ".."))
sys.path.append(os.path.join(current_dir, "../src/sql_app"))
