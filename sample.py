from BepopControl import *

# Example usage
if __name__ == "__main__":
    Devices = load_bebop_api()
    bebop = connect_to_bebop(Devices)
    if bebop:
        if check_connection(bebop):
            get_wavelength_bandwidth(bebop)
            if set_filter_positions(bebop, 600, 605):
                check_filters_position(bebop)
            disconnect_from_bebop(bebop)
