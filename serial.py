"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize a Serial Generator object with a starter and value 
        attribute, which will be incremented."""

        self.start = start
        self.value = start

    def __repr__(self):
        return f'SerialGenerator(start={self.start}, value={self.value})'

    def generate(self):
        """Assign current value to a serial. Return that variable
        and increment the value."""
        serial = self.value
        self.value += 1
        return serial

    def reset(self):
        """Reset value to the original start value"""

        self.value = self.start 