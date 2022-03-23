import sys

sys.path.insert(0, '../../../')
from src.database.migrations import upgrade

if __name__ == "__main__":
    upgrade()
