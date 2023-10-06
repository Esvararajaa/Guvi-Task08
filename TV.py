# Parent class
class TV:
    # constructor
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.price = 65000  # You can set the price as needed
        self.inches = 32  # You can set the inches as needed
        self.on = False
        self.volume = 50  # Default volume is 50

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def increase_volume(self):
        if self.on and self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.on and self.volume > 0:
            self.volume -= 1

    def set_channel(self, new_channel):
        if self.on and 1 <= new_channel <= 50:
            self.channel = new_channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        if self.on:
            return f"{self.brand} at channel {self.channel}, volume {self.volume}"
        else:
            return "Please switch ON the TV"


# Child class inherited the parent class
class LED(TV):
    # Inherited the parent class properties using super()
    def __init__(self, brand):
        super().__init__(brand)
        self.screen_thickness = "4 inches"
        self.energy_usage = "50 watts"
        self.lifespan = "10 yrs"
        self.refresh_rate = "120 hz"
        self.viewing_angle = "360 degree"
        self.backlight = "Philips"

    def display_details(self):
        # Displaying the details of the LED TV
        return f'\n Screen Thickness: {self.screen_thickness},\n Energy usage: {self.energy_usage}, ' \
               f'\n Life Span: {self.lifespan}, \n Refresh Rate:{self.refresh_rate}, ' \
               f'\n Viewing Angle: {self.viewing_angle},\n Back light: {self.backlight}'


# Child class inherited the parent class
class Plasma(TV):
    # Inherited the parent class properties using super()
    def __init__(self, brand):
        super().__init__(brand)
        self.screen_thickness = "3.5 inches"
        self.energy_usage = "50 watts"
        self.lifespan = "6.8 yrs"
        self.refresh_rate = "120 hz"
        self.viewing_angle = "360 degree"
        self.backlight = "LG"

    def display_details(self):
        # Displaying the details of the PlasmaTV
        return f'\n Screen Thickness: {self.screen_thickness},\n Energy usage: {self.energy_usage}, ' \
               f'\n Life Span: {self.lifespan}, \n Refresh Rate:{self.refresh_rate}, ' \
               f'\n Viewing Angle: {self.viewing_angle},\n Back light: {self.backlight}'


# Function usage with TV on
led_tv = LED("Panasonic")
led_tv.turn_on()
led_tv.decrease_volume()
led_tv.decrease_volume()
led_tv.decrease_volume()
led_tv.increase_volume()
led_tv.set_channel(8)
led_tv.set_channel(64)
led_tv.set_channel(41)
led_tv.reset_tv()

# Function usage with TV off
plasma_tv = Plasma("LG")
plasma_tv.turn_off()
plasma_tv.decrease_volume()
plasma_tv.reset_tv()

# displaying the status of the LED TV
print(led_tv.status())
print(f"Display Details: {led_tv.display_details()}\n")

# displaying the status of the Plasma TV
print(plasma_tv.status())
print(f"Display Details: {plasma_tv.display_details()}")
