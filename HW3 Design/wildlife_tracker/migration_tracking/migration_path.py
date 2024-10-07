from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, start_location: Habitat,
                    destination: Habitat, 
                    species: str,
                    path_id: int,
                    duration: Optional[int] = None):
        pass
    pass