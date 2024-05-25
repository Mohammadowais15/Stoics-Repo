class Motor:
    def __init__(self, motor_id):
        self.motor_id = motor_id
        self.speed = 0.0  # in RPM
        self.temperature = 25.0  # in Celsius
        self.power_consumption = 0.0  # in kW

    def update_speed(self, speed):
        self.speed = speed
        print(f"Motor {self.motor_id}: Speed updated to {self.speed} RPM")

    def update_temperature(self, temperature):
        self.temperature = temperature
        print(f"Motor {self.motor_id}: Temperature updated to {self.temperature} °C")

    def update_power_consumption(self, power):
        self.power_consumption = power
        print(f"Motor {self.motor_id}: Power consumption updated to {self.power_consumption} kW")

    def get_status(self):
        return {
            'motor_id': self.motor_id,
            'speed': self.speed,
            'temperature': self.temperature,
            'power_consumption': self.power_consumption
        }


class EVMonitor:
    def __init__(self):
        self.motors = {}

    def add_motor(self, motor):
        self.motors[motor.motor_id] = motor
        print(f"Motor {motor.motor_id} added to the monitor system.")

    def update_motor(self, motor_id, speed=None, temperature=None, power=None):
        if motor_id not in self.motors:
            print(f"Motor {motor_id} not found.")
            return

        if speed is not None:
            self.motors[motor_id].update_speed(speed)
        if temperature is not None:
            self.motors[motor_id].update_temperature(temperature)
        if power is not None:
            self.motors[motor_id].update_power_consumption(power)

    def get_motor_status(self, motor_id):
        if motor_id not in self.motors:
            print(f"Motor {motor_id} not found.")
            return None
        return self.motors[motor_id].get_status()

    def monitor_all_motors(self):
        for motor_id, motor in self.motors.items():
            status = motor.get_status()
            print(f"Status of Motor {motor_id}: Speed={status['speed']} RPM, "
                  f"Temperature={status['temperature']} °C, "
                  f"Power Consumption={status['power_consumption']} kW")


# Example usage
if __name__ == "__main__":
    motor1 = Motor(motor_id=1)
    motor2 = Motor(motor_id=2)

    ev_monitor = EVMonitor()
    ev_monitor.add_motor(motor1)
    ev_monitor.add_motor(motor2)

    ev_monitor.update_motor(motor_id=1, speed=1500, temperature=30, power=5.2)
    ev_monitor.update_motor(motor_id=2, speed=2000, temperature=35, power=7.4)

    ev_monitor.monitor_all_motors()
