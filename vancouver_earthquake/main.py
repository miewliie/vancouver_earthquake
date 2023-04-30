from vancouver_earthquake.core.earthquake import Earthquake
import vancouver_earthquake.core.network_manager as network_manager
from vancouver_earthquake.social.social_manager import social_manager
import vancouver_earthquake.storage.storage_manager as storage_manager

# test in_boundary() --> test_in_boundary.py ------ done
# test test_storage_manager.py
# test filter_out_duplicate_earthquake() --> test_filter_out_duplicate_earthquake.py
# test test_social_manager.py

# update workflow
# update README.md

TOP_BOUNDING_BOX = 53.7827
BOTTOM_BOUNDING_BOX = 44.7827
LEFT_BOUNDING_BOX = -132.2207
RIGHT_BOUNDING_BOX = -114.0207


def in_boundary(
    earthquakes: list[Earthquake],
    top: float = TOP_BOUNDING_BOX,
    bottom: float = BOTTOM_BOUNDING_BOX,
    left: float = LEFT_BOUNDING_BOX,
    right: float = RIGHT_BOUNDING_BOX
) -> list[Earthquake]:
    """ This function will return the list of earthquake, if the earthquake is in the boundary of Vancouver. """
    return [eq for eq in earthquakes if right > eq.longitude > left and top > eq.latitude > bottom]


def filter_out_duplicate_earthquake(old_eq: list[Earthquake], new_eq: list[Earthquake]) -> list[Earthquake]:
    """ This function will return earthquakes from new_eq not present in old_eq. """
    return [eq for eq in new_eq if eq not in old_eq]


def main():
    new_earthquakes: list[Earthquake] = network_manager.get_earthquake_data()
    new_earthquakes = in_boundary(earthquakes=new_earthquakes)

    if not new_earthquakes:
        print("No earthquake in Vancouver.")
        return

    old_earthquakes: list[Earthquake] = storage_manager.read_earthquake_data()
    storage_manager.write_earthquake_data(new_eq=new_earthquakes)
    filtered_earthquakes: list[Earthquake] = filter_out_duplicate_earthquake(old_eq=old_earthquakes,
                                                                             new_eq=new_earthquakes)

    if not filtered_earthquakes:
        print("No valid earthquake after filtered.")
        return

    social_manager(earthquakes=filtered_earthquakes)


if __name__ == '__main__':
    main()
