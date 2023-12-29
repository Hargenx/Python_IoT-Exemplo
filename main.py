import abc
from enum import Enum, auto
import logging
import re
from typing import Optional, Union

class ConnectionStatus(Enum):
    CONNECTED = auto()
    DISCONNECTED = auto()

class Connection:
    DEFAULT_PORT = 8080

    def __init__(self) -> None:
        self.name: Optional[str] = None
        self.ip: Optional[str] = None
        self.port: Optional[int] = None
        self.status = ConnectionStatus.DISCONNECTED
        self.connect()

    def _is_valid_ip(self, ip: str) -> bool:
        """Validate IP address format using regex."""
        ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        return bool(re.match(ip_regex, ip))

    def connect(self, name: str = '', ip: str = '', port: int = DEFAULT_PORT) -> None:
        """Connect to a device."""
        if not self._is_valid_ip(ip):
            raise ValueError("Invalid IP address format")
        self.name = name
        self.ip = ip
        self.port = port
        self.status = ConnectionStatus.CONNECTED

    def disconnect(self) -> None:
        """Disconnect from a device."""
        self.name = None
        self.ip = None
        self.port = None
        self.status = ConnectionStatus.DISCONNECTED

    def _send_message(self, message: str) -> None:
        """Send a message to the connected device."""
        if self.status == ConnectionStatus.CONNECTED:
            logging.info(f'Sent: {message}')
        else:
            logging.warning(f"Cannot send. The connection is {self.status.name.lower()}.")

    def send(self, message: Union[str, Enum]) -> None:
        """Send a message to the connected device."""
        if isinstance(message, Enum):
            message = message.value
        self._send_message(message)

    def receive(self) -> str:
        """Receive a message from the connected device."""
        if self.status == ConnectionStatus.CONNECTED:
            return f'Received: OK'
        else:
            logging.warning(f"Cannot receive. The connection is {self.status.name.lower()}.")
            return ""

class IOTDevice(abc.ABC):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def _handle_connection_error(self, error_message: str) -> None:
        """Handle connection errors."""
        logging.error(f"Connection error: {error_message}")

    def connect(self, name: str, ip: str, port: int) -> None:
        try:
            self.connection.connect(name, ip, port)
            logging.info(f"Connected to {name} at {ip}:{port}")
        except ValueError as e:
            self._handle_connection_error(str(e))

    def disconnect(self) -> None:
        self.connection.disconnect()
        logging.info("Disconnected")

    def send(self, message: Union[str, Enum]) -> None:
        self.connection.send(message)

    def receive(self) -> str:
        return self.connection.receive()

class LightMessage(Enum):
    TURN_ON = "Turn on"
    TURN_OFF = "Turn off"

class Light(IOTDevice):
    def send(self, message: LightMessage) -> None:
        super().send(message)

class MotionMessage(Enum):
    MOTION_DETECTED = "Motion detected!"
    NO_MOTION = "No motion detected."

class MotionSensor(IOTDevice):
    def send(self, message: MotionMessage) -> None:
        super().send(message)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    connection = Connection()

    try:
        connection.connect('user', '192.168.1.1')
    except ValueError as e:
        logging.error(f"An error occurred: {e}")

    light = Light(connection)
    light.send(LightMessage.TURN_ON)

    motion_sensor = MotionSensor(connection)
    motion_sensor.send(MotionMessage.MOTION_DETECTED)

    connection.disconnect()
