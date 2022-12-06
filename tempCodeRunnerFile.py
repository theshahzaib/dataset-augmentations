if aug_ == 'add_sun_flare':
        image = am.add_sun_flare(image, flare_center=(100, 100), angle= -(math.pi)/4)

    if aug_ == 'add_speed':
        image = am.add_speed(image, speed_coeff=0.9)