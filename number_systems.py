"""
Number Systems Module
Handles conversions between Binary, Octal, Decimal, and Hexadecimal number systems.
"""


class NumberSystemConverter:
    """Converts numbers between different number systems."""
    
    @staticmethod
    def decimal_to_binary(decimal):
        """Convert decimal to binary."""
        if decimal == 0:
            return "0"
        binary = ""
        num = abs(decimal)
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary if decimal >= 0 else "-" + binary
    
    @staticmethod
    def decimal_to_octal(decimal):
        """Convert decimal to octal."""
        if decimal == 0:
            return "0"
        octal = ""
        num = abs(decimal)
        while num > 0:
            octal = str(num % 8) + octal
            num //= 8
        return octal if decimal >= 0 else "-" + octal
    
    @staticmethod
    def decimal_to_hexadecimal(decimal):
        """Convert decimal to hexadecimal."""
        if decimal == 0:
            return "0"
        hex_chars = "0123456789ABCDEF"
        hexadecimal = ""
        num = abs(decimal)
        while num > 0:
            hexadecimal = hex_chars[num % 16] + hexadecimal
            num //= 16
        return hexadecimal if decimal >= 0 else "-" + hexadecimal
    
    @staticmethod
    def binary_to_decimal(binary):
        """Convert binary to decimal."""
        binary = binary.replace(" ", "")
        if binary.startswith("-"):
            sign = -1
            binary = binary[1:]
        else:
            sign = 1
        
        decimal = 0
        for i, digit in enumerate(reversed(binary)):
            if digit not in "01":
                raise ValueError(f"Invalid binary digit: {digit}")
            decimal += int(digit) * (2 ** i)
        return sign * decimal
    
    @staticmethod
    def octal_to_decimal(octal):
        """Convert octal to decimal."""
        octal = octal.replace(" ", "")
        if octal.startswith("-"):
            sign = -1
            octal = octal[1:]
        else:
            sign = 1
        
        decimal = 0
        for i, digit in enumerate(reversed(octal)):
            if digit not in "01234567":
                raise ValueError(f"Invalid octal digit: {digit}")
            decimal += int(digit) * (8 ** i)
        return sign * decimal
    
    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
        """Convert hexadecimal to decimal."""
        hexadecimal = hexadecimal.replace(" ", "").upper()
        if hexadecimal.startswith("-"):
            sign = -1
            hexadecimal = hexadecimal[1:]
        else:
            sign = 1
        
        hex_chars = "0123456789ABCDEF"
        decimal = 0
        for i, char in enumerate(reversed(hexadecimal)):
            if char not in hex_chars:
                raise ValueError(f"Invalid hexadecimal digit: {char}")
            decimal += hex_chars.index(char) * (16 ** i)
        return sign * decimal
    
    def convert(self, value, from_base, to_base):
        """
        Convert a number from one base to another.
        
        Args:
            value: The number to convert (as string)
            from_base: Source base (2, 8, 10, or 16)
            to_base: Target base (2, 8, 10, or 16)
        
        Returns:
            Converted number as string
        """
        # First convert to decimal
        if from_base == 10:
            decimal = int(value)
        elif from_base == 2:
            decimal = self.binary_to_decimal(value)
        elif from_base == 8:
            decimal = self.octal_to_decimal(value)
        elif from_base == 16:
            decimal = self.hexadecimal_to_decimal(value)
        else:
            raise ValueError(f"Unsupported base: {from_base}")
        
        # Then convert from decimal to target base
        if to_base == 10:
            return str(decimal)
        elif to_base == 2:
            return self.decimal_to_binary(decimal)
        elif to_base == 8:
            return self.decimal_to_octal(decimal)
        elif to_base == 16:
            return self.decimal_to_hexadecimal(decimal)
        else:
            raise ValueError(f"Unsupported base: {to_base}")
