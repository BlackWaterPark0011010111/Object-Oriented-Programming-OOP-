from bike_cab import BikeCab
def main():
    motorized_cab = BikeCab(is_motorized=True)
    non_motorized_cab = BikeCab(is_motorized=False)

    # Drive motorized bike cab
    while motorized_cab.travel(50):
        print(f"Motorized bike cab has {motorized_cab.max_distance} km left.")

    # Drive non-motorized bike cab
    while non_motorized_cab.travel(50):
        print(f"Non-motorized bike cab has {non_motorized_cab.max_distance} km left.")


if __name__ == "__main__":
    main()