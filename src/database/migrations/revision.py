import sys

sys.path.insert(0, '../../../')
from src.database.migrations import revision

if __name__ == "__main__":
    revision()
