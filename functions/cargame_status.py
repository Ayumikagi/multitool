def accel_0():
    car_state = 'slow'
    print('Starting the car...')
    print('Going slowly!')
    return car_state


def accel_1():
    car_state = 'average'
    print('Speed ramping up!')
    return car_state


def accel_2():
    car_state = 'fast'
    print('Full steam ahead!')
    return car_state


def accel_3():
    car_state = 'max'
    print('What the hell are you doing?!')
    return car_state


def accel_4():
    print("Can't accelerate, you are already pushing it to the limit!")
    return


def stop_0():
    car_state = 'stop'
    print('Stopping the car...')
    return car_state


def stop_1():
    car_state = 'stop'
    print('Smooth braking!')
    return car_state


def stop_2():
    car_state = 'stop'
    print('Wild stop! Your tires are on fire!')
    return car_state


def stop_3():
    car_state = 'stop'
    print('Your brakes can be heard on mars...')
    return car_state


def stop_4():
    print("Can't stop, you are not moving!")
    return